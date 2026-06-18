import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def extract_keywords(text: str) -> str:
    user_prompt = f"""
Analyze the following text and extract exactly 5 comma-separated keywords from the provided resume text
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        temperature=0,
        max_tokens=40,
        messages=[
            {"role": "user", "content": user_prompt} 
        ]
    )
    comment = response.choices[0].message.content
    print(comment)
    return comment

if __name__ == "__main__":
    test_snippet = """Experienced DevOps engineer skilled in Python, Kubernetes, Docker, CI/CD pipelines, and cloud automation."""
    extract_keywords(test_snippet)
