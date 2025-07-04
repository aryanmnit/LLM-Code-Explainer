import openai
import os
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.a4f.co/v1"


def assess_complexity(code, language):
    prompt = f"Assess the complexity of this {language} code and provide a rating from 1 (easy) to 5 (complex):\n\n{code}"
    response = openai.ChatCompletion.create(
        model="provider-2/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message["content"]
