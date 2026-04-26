import os
from pyexpat import model
from xmlrpc import client
from certifi import contents
from google import genai
from google.genai import types


def analyze_text(text):
    client = genai.Client(
        api_key=os.environ.get("google_api_key"),
    )

    model = "gemini-2.5-flash-lite"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=text),
            ],
        ),
    ]

    config = types.GenerateContentConfig(
            temperature=0,
            system_instruction="""
        You are a strict JSON generator.

        Return output in this format:
        {
        "summary": "...",
        "sentiment": "positive/negative/neutral",
        "keywords": ["...", "..."]
        }

        Do not return anything outside JSON.
        """
            )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=config
    )

    return response.text


if __name__ == "__main__":
    print(analyze_text("I hate you"))