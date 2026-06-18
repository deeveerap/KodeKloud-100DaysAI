import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def rewrite_email(text: str) -> str:
    user_prompt=f"""
       Convert this text into a polite and professional email {text}
       """
    
    response = client.chat.completions.create (
        model="openai/gpt-4.1-mini",
        temperature=0.1,
        max_tokens=60,
        messages = [
            {"role":"user", "content":user_prompt}
        ]
    )
    print (response.choices[0].message.content)
    return response.choices[0].message.content
if __name__ == "__main__":
    input_msg="hey send me that report asap"
    rewrite_email(input_msg)
