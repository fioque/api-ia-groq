import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HISTORICO = []

@app.route("/perguntar", methods=["POST"])
def perguntar():
    global HISTORICO
    data = request.json
    pergunta = data.get("pergunta")
    if not pergunta:
        return jsonify({"erro": "Pergunta não fornecida"}), 400

    HISTORICO.append({"role": "user", "content": pergunta})

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": HISTORICO,
            "temperature": 0.7
        }
    )

    if response.status_code == 200:
        resposta = response.json()["choices"][0]["message"]["content"]
        HISTORICO.append({"role": "assistant", "content": resposta})
        return jsonify({"resposta": resposta})
    else:
        return jsonify({"erro": "Erro na API Groq"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
