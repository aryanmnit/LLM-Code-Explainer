import openai
import os
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.a4f.co/v1"


def generate_explanation(code, language):
    prompt = f"Explain this {language} code in a beginner-friendly way, line by line:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="provider-2/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=1000
    )
    return response.choices[0].message["content"]
