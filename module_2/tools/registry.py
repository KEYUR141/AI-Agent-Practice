from google.genai import types


TOOL_MAP = {}
TOOLS_METADATA = []

def register_tool(name, description, parameters):
    

    def decorator(func):
        TOOL_MAP[name] = func

        tools_declaration = types.FunctionDeclaration(
            name=name,
            description=description,
            parameters=parameters,
        )

        TOOLS_METADATA.append(tools_declaration)
        return func
    return decorator

