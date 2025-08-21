from together import Together
import os
from dotenv import load_dotenv

load_dotenv() 
api=os.getenv("api_key")
client = Together(api_key=api)

response = client.chat.completions.create(
    model="google/gemma-3n-E4B-it",
     messages=[
       {"role": "user","content": "What are some fun things to do in Lagos?"
        }, {
   "role":"system", "content":" You are to provide the location of fun places"
        },{"role":"assistant", "content":"You are a travel expert" }])

print(response.choices[0].message.content)