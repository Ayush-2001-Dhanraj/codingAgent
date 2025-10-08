import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)

    verbose = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose = True

    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )

    print(response.text)

    if response is None or response.usage_metadata is None:
        print("response is malformed")
        return

    if verbose:
        print("User prompt", prompt)
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"response Tokens: {response.usage_metadata.candidates_token_count}")


main()
