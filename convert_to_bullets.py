import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)
def convert_to_bullets(text:str) -> str:
    system_prompt= """
     You are good in converting length texts 
     into precise bullet points for presentation.
     """
    user_prompt= f"""
      Convert the text {text} into bullet points
      """
    response = client.chat.completions.create(
        model = "openai/gpt-4.1-mini",
        temperature = 0.1,
        max_tokens = 150,
        messages = [
            {"role": "system", "content": system_prompt},
            {"role" : "user", "content": user_prompt}
        ]
     )
    return response.choices[0].message.content
if __name__ == "__main__":
    input_text="""
      Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and enabling new innovations across healthcare, finance, and education.
    """
    print (convert_to_bullets(input_text))  
