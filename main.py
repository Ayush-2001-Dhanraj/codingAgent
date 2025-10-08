import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how AI works in a few words",
    )

    print(response.text)

    if response is None or response.usage_metadata is None:
        print("response is malformed")
        return

    print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
    print(f"response Tokens: {response.usage_metadata.candidates_token_count}")


main()
