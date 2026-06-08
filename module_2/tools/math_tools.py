from tools.registry import register_tool

@register_tool(
        name="add",
        description = "Add Two Numbers and return the result",
        parameters = {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"], 
        }
)
def add( a: int, b: int) -> int:
    try:
        if not isinstance(a, int):
            raise ValueError("Argument 'a' must be an integer.")
        if not isinstance(b,int):
            raise ValueError("Argument 'b' must be an integer.")
        return a+b
    
    except ValueError as ve:
        return f"Error: {str(ve)}"
    


@register_tool(
        name="divide",
        description = "Divide Two Numbers and return the result",
        parameters = {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"], 
        }
)
def divide( a: int, b: int) -> int:
    try:
        if not isinstance(a, int):
            raise ValueError("Argument 'a' must be an integer.")
        if not isinstance(b,int):
            raise ValueError("Argument 'b' must be an integer.")
        return a//b
    
    except ValueError as ve:
        return f"Error: {str(ve)}"