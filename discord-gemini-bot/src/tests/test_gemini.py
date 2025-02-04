import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/Victor/Documents/discord-gemini-bot/src')))

from utils.queryGemini import query_gemini

class TesteGemini:
    @staticmethod
    def gemini(prompt: str) -> str:
        response = query_gemini(prompt)
        return response

if __name__ == "__main__":
    response = TesteGemini.gemini("Quanto é 2 + 2?")
    print(f"Resposta: {response}")
