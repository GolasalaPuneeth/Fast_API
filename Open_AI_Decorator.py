import os
from openai import OpenAI
def intell(text :str) -> str: 
  client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
  )
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= [
      {"role": "system", "content": "You are a helpful assistant named Cherry."},
      {"role": "user", "content": f"{text}"},
      ]
  )
  return(completion.choices[0].message.content)