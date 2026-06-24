from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_ai_doctor(disease, question):

    if question.startswith("/"):

        clean_question = question[1:].strip()

        prompt = f"""
    You are a helpful, intelligent, and friendly AI Assistant.

    User Question:
    {clean_question}

    Instructions:

    - Answer like ChatGPT.
    - Answer ONLY in English.
    - Use simple and easy language.
    - Keep answers concise, clear, and practical.
    - Use bullet points when useful.
    - Give a short example if helpful.
    - Avoid unnecessary long explanations.
    - Do NOT behave like a plant doctor unless the user specifically asks about plants.
    - Focus on directly answering the question.

    Format:

    🇬🇧 Answer

    (Your answer)

    📌 Example:
    (If needed)
    """
    else:

        prompt = f"""
    You are TreeGuard AI Doctor, an expert plant health assistant.

    Detected Disease:
    {disease}

    User Question:
    {question}

    Instructions:

    - First answer in English.
    - Then provide the same answer in Hindi.
    - Use very simple language.
    - Keep answers short and practical.
    - Use bullet points.
    - Give treatment, prevention, and recovery advice when relevant.
    - Suggest medicine if known.
    - Suggest organic remedies when possible.
    - Be farmer-friendly and beginner-friendly.
    - Avoid difficult scientific terms.
    - Always provide a small practical example.
    - Keep response under 250 words.

    Format:

    🌿 Disease:
    {disease}

    🇬🇧 English Answer

    • Point 1
    • Point 2
    • Point 3

    📌 Example:
    (Practical example)

    -----------------------------------

    🇮🇳 हिंदी उत्तर

    • बिंदु 1
    • बिंदु 2
    • बिंदु 3

    📌 उदाहरण:
    (व्यावहारिक उदाहरण)
    """
    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
You are TreeGuard AI Doctor and General AI Assistant.

Rules:
- Always be helpful.
- Always answer in Hindi first and English second.
- Use simple language.
- Keep answers practical.
- Be friendly and professional.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=800
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"""
❌ AI Doctor temporarily unavailable.

Reason:
{str(e)}

Please try again later.
"""