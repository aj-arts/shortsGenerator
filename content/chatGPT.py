import os
import requests
from dotenv import load_dotenv
load_dotenv()

def generate_req(prompt,tokens):
    '''
    Function to generate a chat GPT Response. Requires prompt and number of tokens to use. Suggestion: 200 for 150 words or less.
    '''
    
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.environ["OPENAI_API_KEY"]}'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        'max_tokens': tokens,
        'temperature': 1
    }
    print("Accessing OPEN AI...")
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    print("Used Tokens: " + str(response_data['usage']['total_tokens']))
    story = response_data['choices'][0]['message']['content']
    return story
