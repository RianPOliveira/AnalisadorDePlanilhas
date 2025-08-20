import os
import google.generativeai as genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# --- Bloco de Inicialização ---
try:
    # Configura a chave da API do Google Gemini
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    print("✅ API do Google Gemini configurada com sucesso!")
except Exception as e:
    print(f"❌ Erro ao configurar a API do Google Gemini: {e}")
    # O servidor irá rodar, mas as requisições para a IA falharão.

# Inicializa o modelo
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-pro-latest")
try:
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        # Você pode ajustar a configuração de geração, se necessário
        generation_config={
            "temperature": 0.5,
            "max_output_tokens": 800
        },
        # Configurações de segurança para bloquear conteúdo perigoso
        safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
    )
    print("✅ Modelo de IA inicializado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao inicializar o modelo de IA: {e}")

# Inicializa o servidor FastAPI
app = FastAPI()

# Configurar CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("✅ Servidor de API pronto para receber requisições.")
# --- Fim do Bloco de Inicialização ---

class PlanilhaRequest(BaseModel):
    dados_planilha: str
    instrucao: str

@app.post("/analisar_planilha")
def analisar_planilha(request: PlanilhaRequest):
    print(f"Recebida requisição para analisar planilha com a instrução: '{request.instrucao}'")
    
    # Montamos a instrução completa para a IA
    prompt_completo = f"""
    **Tarefa:** Você é um especialista em análise de dados e planilhas.
    
    **Instrução do Usuário:** {request.instrucao}
    
    **Dados da Planilha (em formato de texto/CSV):**
    ---
    {request.dados_planilha}
    ---
    
    **Sua Resposta:** Forneça uma análise clara e objetiva baseada na instrução e nos dados fornecidos.
    """
    
    try:
        # Chamada real para a API do Google Gemini
        response = model.generate_content(prompt_completo)
        analise = response.text
        
        print("Análise gerada pelo modelo de IA com sucesso.")
        return {"analise_concluida": True, "relatorio": analise}
    except Exception as e:
        print(f"❌ Erro durante a análise do modelo de IA: {e}")
        return {"analise_concluida": False, "erro": str(e)}

@app.get("/")
def rota_raiz():
    return {"mensagem": "Servidor do Agente de Análise de Planilhas está no ar!"}