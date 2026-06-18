import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def generate_comment(code_snippet: str) -> str:
    user_prompt = f"""
Analyze the following code snippet and produce a clear, one-line comment or docstring describing its purpose:
{code_snippet}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        temperature=0.2,
        max_tokens=30,
        messages=[
            {"role": "user", "content": user_prompt} 
        ]
    )
    comment = response.choices[0].message.content
    print(comment)
    return comment

if __name__ == "__main__":
    test_snippet = """def calculate_area(length, width):
    return length * width"""
    generate_comment(test_snippet)
