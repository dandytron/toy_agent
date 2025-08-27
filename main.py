import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("Please provide a prompt in single or double quotes")
        sys.exit(1)
    elif len(sys.argv) > 2:
        if sys.argv[2] == '--verbose':
            verbose = True
            prompt = sys.argv[1]
        else:
            print("Invalid flag provided. Either type --verbose after your prompt for additional information or do not provide a flag to only see the response")
            sys.exit(1)
    else:
        verbose = False
        prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    print(response.text)
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    

if __name__ == "__main__":
    main()
