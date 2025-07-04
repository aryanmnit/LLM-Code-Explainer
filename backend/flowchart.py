import openai
import os
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.a4f.co/v1"


def generate_flowchart(code, language):
    prompt = f"Generate a Mermaid.js flowchart for the following {language} code:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="provider-2/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=800
    )
    return response.choices[0].message.content
