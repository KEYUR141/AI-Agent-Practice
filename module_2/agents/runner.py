from google import genai
from google.genai import types
from config import API_KEY, MODEL, AGENT_SYSTEM_PROMPT
from google.genai import types
from agents.tools_registry import tools
from tools.registry import TOOL_MAP as tools_map
import json
client = genai.Client(api_key=API_KEY)


def execute_tool(func_name, args):
    try:
        if not func_name in tools_map:
                return {"error": f"Error: Tool {func_name} not found."}
        
        func = tools_map.get(func_name)
        if not func:
            return {"error": f"Error: Function {func_name} not implemented."}
        return func(**args)
    except Exception as e:
        return {"error": f"Error: Failed to execute tool {func_name}. {str(e)}"}


def create_plan(user_input):

    response = client.models.generate_content(
            model = MODEL,
            contents = f"""
            Create a Execution Plan.

            Task:
            {user_input}

            return:
            - Step 1
            - Step 2

            """,
    )

    return response.text




def run_agent(user_input):
    
    # if not user_input.strip():
    #     continue

    plan = create_plan(user_input)

    print("=====Plan=====")
    print(plan)

    trace = []

    messages = [
        types.Content(
            role = "User",
            parts = [types.Part(text = user_input)]
        )
    ]



    while True:

        response = client.models.generate_content(
            model = MODEL,
            contents = messages,
            config = types.GenerateContentConfig(
                tools = tools,
                system_instruction= AGENT_SYSTEM_PROMPT
            ),
        )
    

        tools_called = False
        final_text = ""

        for candidate in response.candidates:
            for part in candidate.content.parts:

                if part.function_call:
                    tools_called = True
                    func_name = part.function_call.name
                    args = part.function_call.args

                    print(f"Model wants to call {func_name} with args {args}")

                    result = execute_tool(func_name, args)

                    print(f"Tool Result: {result}")

                    trace.append(
                        {
                            "tool": func_name,
                            "args": args,
                            "result": result
                        }
                    )
                    # Add model's function call to messages
                    messages.append(
                        types.Content(
                            role="model",
                            parts=[part]
                        )
                    )

                    # Add tool result back to messages
                    messages.append(
                        types.Content(
                            role="user",
                            parts=[
                                types.Part(
                                    text=f"""
                                Tool Execution Result

                                Tool: {func_name}

                                Output:
                                {result}
                                """
                                )
                            ]
                        )
                    )

                elif part.text:
                    final_text += part.text
        if not tools_called:
            return final_text




