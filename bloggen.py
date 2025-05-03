import requests

def generate_blog(paragraph_topic):
    prompt = f"Write a paragraph about the following topic: {paragraph_topic}"

    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False 
        }
    )
    data = response.json()
    return data['response']

print(generate_blog('Why meditation is important?'))

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no: ')
    if answer.upper() == 'Y':
        paragraph_topic = input('What should this paragraph talk about? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
