import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def generate_commit(changes: str) -> str:
    prompt = f"""
Analyse the summary of code changes.
Choose commit type from: feat, fix, or docs.
Generate a concise subject (under 50 characters).
The output must be only the commit message in the exact format: <type>: <subject>
{changes}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        temperature=0.0,
        max_tokens=30,
        messages=[
            {"role": "user", "content": prompt} 
        ]
    )
    comment = response.choices[0].message.content
    print(comment)
    return comment

if __name__ == "__main__":
    test_snippet = "Added a new user registration endpoint and fixed a typo in the README file"
    generate_commit(test_snippet)
