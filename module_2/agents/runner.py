from google import genai
from google.genai import types
from config import API_KEY, MODEL
from .agents_registry import tools
from tools.math_tools import add 
from tools.weather import weather_info

client = genai.Client(api_key=API_KEY)

def run_agent(user_input):
    
    response = client.models.generate_content(
        model=MODEL,
        contents=user_input,
        config={"tools": tools}
    )

    print(response)
    for candidate in response.candidates:
        for part in candidate.content.parts:

            # If model wants to call a function
            if part.function_call:
                func_name = part.function_call.name
                args = part.function_call.args

                if func_name == "add":
                    result = add(**args)

                elif func_name == "weather_info":
                    result = weather_info(**args)

                # Send result back to model with proper Content format
                final_response = client.models.generate_content(
                    model=MODEL,
                    contents=[
                        types.Content(
                            role="user",
                            parts=[types.Part(text=user_input)]
                        ),
                        types.Content(
                            role="model",
                            parts=[part]
                        ),
                        types.Content(
                            role="user",
                            parts=[types.Part(text=str(result))]
                        )
                    ]
                )

                return final_response.text

            # If no tool call, just return text
            if part.text:
                return part.text