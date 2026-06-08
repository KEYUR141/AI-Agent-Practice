from tools.registry import register_tool


@register_tool(
        name="weather_info",
        description = "Get Current Weather Infomation for a location",
        parameters = {
            "type":"object",
            "properties": {
                "location": {"type":"string"}
            },
            "required":["location"]
        }
)
def weather_info(location: str) -> str:
    return f"The current weather in {location} is sunny with a temperature of 25°C."


@register_tool(
        name="time_date_info",
        description = "Get time and date information of current",
        parameters = {
            "type":"object",
            "properties": {
                "location": {"type":"string"}
            },
            "required":["location"]
        }
)
def time_data_info(location: str) -> str:
    return f"The current time and data in {location} is 29th August 2005."