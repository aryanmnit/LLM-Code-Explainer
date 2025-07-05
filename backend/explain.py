from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

def generate_explanation(code, language):
    prompt = f"Explain this {language} code in a beginner-friendly way, line by line:\n\n{code}"
    response = client.chat.completions.create(
        model="provider-2/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=1000
    )
    return response.choices[0].message.content
