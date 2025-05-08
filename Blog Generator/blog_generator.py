# A simple blog generator using llama3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('llm_api_url')

if not BASE_URL:
    raise ValueError("API URL not found. Please set 'llm_api_url' in your .env file.")

def generate_blog(paragraph_topic):
    prompt = f"Write a paragraph about the following topic: {paragraph_topic}"

    try:
        response = requests.post(
            BASE_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False 
            }
        )
        data = response.json()
        return data['response']
    except requests.RequestException as e:
        return f"Error communication with LLM API: {e}"

print(generate_blog('Why meditation is important?'))

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no: ')
    if answer.upper() == 'Y':
        paragraph_topic = input('What should this paragraph talk about? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
