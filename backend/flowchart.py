from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)


def generate_flowchart(code, language):
    prompt = f"Generate a Mermaid.js flowchart for the following {language} code and reply only the flowchart:\n\n{code}"
    response = client.chat.completions.create(
        model="provider-2/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=800
    )
    return response.choices[0].message.content
