from google.genai import types

# IMPORT TOOLS
import tools.math_tools
import tools.weather

from tools.registry import TOOLS_METADATA

tools = [
    types.Tool(
        function_declarations = TOOLS_METADATA
    )
]


print("Registered Tools:", tools)
print("Tools Map:", TOOLS_METADATA)

