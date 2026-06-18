import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def summarize(text: str) -> str:
    prompt=f"""
        You are a strict Summarization assistant.
        Transform the below text into concise, easy to understand, clear single line summary.
        '{text}':"""
    
    response = client.chat.completions.create (
        model="openai/gpt-4.1-mini",
        temperature=0.5,
        max_tokens=60,
        messages = [
            {"role":"user", "content":prompt}
        ]
    )
    print (response.choices[0].message.content)
    return response.choices[0].message.content
if __name__ == "__main__":
    input_msg="Artificial Intelligence enables machines to mimic human intelligence, performing tasks such as learning, problem-solving, and decision-making with increasing accuracy"
    summarize(input_msg)
