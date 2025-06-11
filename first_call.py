import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Fixed system prompt
system_prompt = {
    "role": "system",
    "content": "You are a helpful AI assistant."
}

# Take user input
user_input = input("Enter your prompt: ")
user_prompt = {
    "role": "user",
    "content": user_input
}

# Make API call
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[system_prompt, user_prompt]
    )

    reply = response.choices[0].message.content
    usage = response.usage

    print("\nAssistant's Response:")
    print(reply)
    print("\nToken Usage:")
    print(f"Prompt tokens: {usage.prompt_tokens}")
    print(f"Completion tokens: {usage.completion_tokens}")
    print(f"Total tokens: {usage.total_tokens}")

except Exception as e:
    print(f"\nError occurred:\n{e}")
