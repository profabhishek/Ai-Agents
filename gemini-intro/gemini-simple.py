# import os
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# prompt = """
# Translate these :

# Hello -> Hola
# Goodbye -> Adiós
# Thank you ->
# """

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents=prompt
# )

# print(response.text)

import os
import time

from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

contents = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(
                text="""
Tell me a long story about cricket on Mars.
"""
            )
        ]
    )
]

stream = client.models.generate_content_stream(
    model="gemini-3.5-flash",

    contents=contents,

    config=types.GenerateContentConfig(
        system_instruction="You are a cricketer.",
        temperature=1.3,
        top_p=1
    ),
)

for chunk in stream:

    if chunk.text:

        words = chunk.text.split()

        for word in words:
            print(word, end=" ", flush=True)
            time.sleep(0.1)