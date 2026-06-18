import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def generate_haiku(topic: str) -> str:
    user_prompt=f"""
        generates three-line haikus (5-7-5 syllable pattern) based on a given topic {topic}
       """
    
    response = client.chat.completions.create (
        model="openai/gpt-4.1-mini",
        temperature=0.0,
        max_tokens=60,
        messages = [
            {"role":"user", "content":user_prompt}
        ]
    )
    print (response.choices[0].message.content)
    return response.choices[0].message.content
if __name__ == "__main__":
    input_msg="sky"
    generate_haiku(input_msg)
