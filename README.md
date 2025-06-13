# Este é o meu primeiro projeto-teste de um chatbot inteligente!

Um chatbot desenvolvido com API Groq e modelo LLaMA3, capaz de responder inúmeras perguntas, manter seus históricos de conversas, interpretar comandos complexos e processar dados de arquivos CSV para gerar PDFs via IA.

# Funcionalidades

- Chat interativo com histórico de conversa.
- Interface web responsiva e amigável (`frontend/chat.html`)
- Backend em Flask integrando com API Groq (`backend/app.py`)
- Suporte para leitura de CSV e geração de PDFs por IA (a implementar)
- Envio de perguntas e respostas via API REST

# Tecnologias Usadas

- Frontend: HTML, CSS, JavaScript  
- Backend: Python, Flask, Flask-CORS  
- API: Groq LLM (modelo LLaMA3)  
- Variáveis de ambiente com dotenv.

# Pré-Requisitos

- Python 3.8 ou superior.
- Conta e API Key da Groq (defina `GROQ_API_KEY` em `.env` dentro de `backend`)
- Navegador moderno para acessar o frontend.

# Executação do Projeto

Clone o repositório:

```bash
git clone https://github.com/fioque/api-ia-groq.git
cd api-ia-groq


