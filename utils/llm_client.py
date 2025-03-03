import openai
import requests
from config import USE_LOCAL_OLLAMA, OLLAMA_MODEL, OPENAI_MODEL, OPENAI_API_KEY

def ask_llm(prompt):
    if USE_LOCAL_OLLAMA:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        return response.json()['response']
    else:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
