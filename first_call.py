
from openai import OpenAI
from dotenv import load_dotenv
import os

def get_api_key():
    """Get OpenAI API key from environment variable."""
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable")
    return api_key

def main():

    client = OpenAI(api_key=get_api_key())
    system_prompt = "You are a helpful assistant."
    user_input = input("Enter your prompt: ")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )

        assistant_response = response.choices[0].message.content
        print("\nAssistant's response:")
        print(assistant_response)
        
        # Print token usage
        print("\nToken usage:")
        print(f"Total tokens: {response.usage.total_tokens}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Completion tokens: {response.usage.completion_tokens}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
