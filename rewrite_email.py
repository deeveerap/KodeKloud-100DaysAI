import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def rewrite_email(text: str) -> str:
    system_prompt="""
       You are expert in writing polite and professional emails
       """
    user_prompt=f"""
       Convert this text into a polite and professional email {text}
       """
    
    response = client.chat.completions.create (
        model="openai/gpt-4.1-mini",
        temperature= 0.1,
        max_tokens= 60,
        messages = [
            {"role":"system", "content":system_prompt},
            {"role":"user", "content":user_prompt}
        ]
    )
    return response.choices[0].message.content
if __name__ == "__main__":
    input_msg="hey send me that report asap"
    print (rewrite_email(input_msg))
