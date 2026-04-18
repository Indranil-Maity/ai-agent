import os
import sys
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()
    key = os.environ.get("API_KEY")
    if not key:
        print(f"ERROR: API_KEY not set in environment", file=sys.stderr)
        sys.exit(1)
    client = genai.Client(api_key=key)
    
    parser = argparse.ArgumentParser(description="ChatBot")
    parser.add_argument("user_prompt", nargs="+", type=str, help="User Prompt")
    parser.add_argument("--model", default="gemini-2.5-flash", help="Model Name")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    prompt_text = " ".join(args.user_prompt)
    messages = [types.Content(role="user", parts=[types.Part(text=prompt_text)])]
    try:
        res = client.models.generate_content(
            model=args.model,
            contents=messages,
            )
    except Exception as e:
        print(f"API ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    if not res or not res.text:
        print("ERROR: No response received from API", file=sys.stderr)
        sys.exit(1)
    if res.usage_metadata and args.verbose:
        print(f"User prompt: {prompt_text}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
    print("Response: ")
    print(res.text)
if __name__ == "__main__":
    main()
