def add( a: int, b: int) -> int:
    try:
        if not isinstance(a, int):
            raise ValueError("Argument 'a' must be an integer.")
        if not isinstance(b,int):
            raise ValueError("Argument 'b' must be an integer.")
        return a+b
    
    except ValueError as ve:
        return f"Error: {str(ve)}"