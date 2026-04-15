import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()
    key = os.environ.get("API_KEY")
    client = genai.Client(api_key=key)
    
    parser = argparse.ArgumentParser(description="ChatBot")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    res = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            )
    if res.usage_metadata:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
        print("Response: ")
        print(res.text)
    else:
        raise RuntimeError("Failed API requests")
if __name__ == "__main__":
    main()
