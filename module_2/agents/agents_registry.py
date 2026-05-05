from google.genai import types

tools = [
    types.Tool(
        function_declarations= [
            types.FunctionDeclaration(
                name = "add",
                description = "Add Two Numbers and return the result",
                parameters={
                    "type": "object",
                    "properties": {
                        "a": {"type": "integer"},
                        "b": {"type": "integer"},
                    },
                    "required": ["a", "b"],
                },
            ),
            types.FunctionDeclaration(
                name ="weather_info",
                description = "Get the current weather information for a given location",
                parameters = {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string"},
                    },
                    "required": ["location"],
                }
            )
        ]
    )
]

