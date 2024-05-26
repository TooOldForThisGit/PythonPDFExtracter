import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistan that output responses in strictly valid json objects"},
            {"role": "user", "content": prompt},
        ],
        model="gpt-4-turbo",
        temperature =  0.1,
        n = 1,
    )
    return response.choices[0].message.content