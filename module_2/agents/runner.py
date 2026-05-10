from google import genai
from google.genai import types
from config import API_KEY, MODEL
from .agents_registry import tools
from tools.math_tools import add 
from tools.weather import weather_info

client = genai.Client(api_key=API_KEY)


def execute_tool(func_name, args):
    if func_name == "add":
        return add(**args)
    elif func_name == "weather_info":
        return weather_info(**args)
    
    return "NO Tool Found"


def run_agent(user_input):
    
    messages = [user_input]

    while True:

        response = client.models.generate_content(
            model = MODEL,
            contents = messages,
            config = {"tools": tools},
        )
    

        tools_called = False

        for candidate in response.candidates:
            for part in candidate.content.parts:

                if part.function_call:
                    tools_called = True
                    func_name = part.function_call.name
                    args = part.function_call.args

                    print(f"Model wants to call {func_name} with args {args}")

                    result = execute_tool(func_name, args)

                    print(f"Tool Result: {result}")

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
                            parts=[types.Part(text=str(result))]
                        )
                    )

                elif part.text:
                    final_text = part.text
            if not tools_called:
                return final_text






# def run_agent(user_input):
    
#     response = client.models.generate_content(
#         model=MODEL,
#         contents=user_input,
#         config={"tools": tools}
#     )

#     print(response)
#     for candidate in response.candidates:
#         for part in candidate.content.parts:

#             # If model wants to call a function
#             if part.function_call:
#                 func_name = part.function_call.name
#                 args = part.function_call.args

#                 if func_name == "add":
#                     result = add(**args)

#                 elif func_name == "weather_info":
#                     result = weather_info(**args)

#                 # Send result back to model with proper Content format
#                 final_response = client.models.generate_content(
#                     model=MODEL,
#                     contents=[
#                         types.Content(
#                             role="user",
#                             parts=[types.Part(text=user_input)]
#                         ),
#                         types.Content(
#                             role="model",
#                             parts=[part]
#                         ),
#                         types.Content(
#                             role="user",
#                             parts=[types.Part(text=str(result))]
#                         )
#                     ]
#                 )

#                 return final_response.text

#             # If no tool call, just return text
#             if part.text:
#                 return part.text