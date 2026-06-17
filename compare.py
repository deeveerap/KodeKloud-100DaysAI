import os
from openai import OpenAI
# Initialize client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

def compare(item1: str, item2: str) -> str:
    system_prompt = """
You are a technical expert with knowledge of mobile phone chipsets.
""".strip()
    user_request = f"""
Please compare the chipsets of iPhone models {item1} and {item2}.
""".strip()
    model_name = "openai/gpt-4.1-mini"
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_request},
        ],
        temperature=0.5,
        max_tokens=100,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(compare("iPhone 13", "iPhone 17"))
