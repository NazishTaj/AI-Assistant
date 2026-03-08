from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def suggest_chart(question, columns):

    prompt = f"""
You are a data visualization expert.

User question:
{question}

Dataset columns:
{columns}

Choose the best chart type.

Only return one of these:
bar
line
pie
scatter
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[{"role":"user","content":prompt}]
    )

    chart = response.choices[0].message.content.strip().lower()

    return chart