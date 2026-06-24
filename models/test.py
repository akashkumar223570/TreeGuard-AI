from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "what is python in consice way with example"
        }
    ]
)

print(response.choices[0].message.content)


