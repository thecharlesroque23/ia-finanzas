from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def preguntar(pregunta: str) -> str:
    response = client.models.generate_content(
      model="gemini-2.0-flash-lite",
        contents=pregunta
    )
    return response.text

if __name__ == "__main__":
    respuesta = preguntar("¿Qué es el riesgo financiero? Explícalo en 2 líneas.")
    print(respuesta)