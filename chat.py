import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_helper(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are HELPER, a productivity assistant."},
            {"role": "user", "content": message}
        ],
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

def save_chat(data):
    return {"status": "Chat saved", "data": data}