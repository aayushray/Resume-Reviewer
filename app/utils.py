import openai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_feedback(resume_text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt_text = resume_text + "\n Provide detailed Feedback to the above resume text and review how to improve the given resume for Software Development Profile:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": resume_text
            }
        ],
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    feedback = response["choices"][0]["message"]["content"]
    return feedback
