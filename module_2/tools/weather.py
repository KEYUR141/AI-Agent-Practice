from tools.registry import register_tool


@register_tool(
        name="weather_info",
        description = "Get Current Weather Infomation for a location",
        parameters = {
            "type":"object",
            "properties": {
                "Location": {"type":"string"}
            },
            "required":["Location"]
        }
)
def weather_info(location: str) -> str:
    return f"The current weather in {location} is sunny with a temperature of 25°C."