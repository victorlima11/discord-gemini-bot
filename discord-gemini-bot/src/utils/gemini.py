import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def query_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(contents=prompt)
        return getattr(response, "text", "Não foi possível obter resposta.")
    except Exception as e:
        return f"Não foi possível obter resposta da API: {str(e)}"
