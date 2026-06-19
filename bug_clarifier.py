import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def clarify_bug(description: str) -> str:
    user_prompt = f"""
 transform below informal bug description reports into clear, structured, and professional issue summaries
{description}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        temperature=0.0,
        max_tokens=100,
        messages=[
            {"role": "user", "content": user_prompt} 
        ]
    )
    comment = response.choices[0].message.content
    print(comment)
    return comment

if __name__ == "__main__":
    test_snippet = "App keeps crashing when I click save."
    clarify_bug(test_snippet)
