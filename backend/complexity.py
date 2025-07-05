from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)


def assess_complexity(code, language):
    prompt = f"Tell the time and space complexity of this {language} code and provide a rating from 1 (easy) to 5 (complex) for the given code:\n\n{code}"
    response = client.chat.completions.create(
        model="provider-2/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content
