# servidor_api.py (Versão final, completa e corrigida)

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

# --- CONFIGURAÇÃO E INICIALIZAÇÃO ---

# Carrega as variáveis do arquivo .env
load_dotenv()

# Crie a sua aplicação FastAPI
app = FastAPI()

# --- BLOCO DE CONFIGURAÇÃO DO CORS (A PARTE MAIS IMPORTANTE) ---
# Este bloco deve vir logo após a criação do app
origins = [
    "*"  # Permite todas as origens. Para produção, você pode restringir.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"], # Garante que OPTIONS seja permitido
    allow_headers=["*"],
)
# --- FIM DO BLOCO DE CONFIGURAÇÃO DO CORS ---


# Inicialize o modelo de IA
model = None
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERRO: GOOGLE_API_KEY não encontrada no arquivo .env")
    else:
        genai.configure(api_key=api_key)
        generation_config = {"max_output_tokens": 8192, "temperature": 0.9}
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        model = genai.GenerativeModel(
            os.getenv("MODEL_NAME", "gemini-1.5-flash-latest"),
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        print("✅ Modelo do Google Gemini inicializado com sucesso!")
except Exception as e:
    print(f"❌ Erro crítico ao inicializar o modelo de IA: {e}")


# Modelo de dados para a requisição que vem do frontend
class PlanilhaRequest(BaseModel):
    dados_planilha: str
    instrucao: str

# --- ENDPOINTS DA API ---

@app.get("/")
def rota_raiz():
    return {"mensagem": "Servidor do Agente de Análise de Planilhas está no ar!"}


@app.post("/analisar_planilha")
def analisar_planilha(request: PlanilhaRequest):
    if not model:
        raise HTTPException(status_code=503, detail="Modelo de IA não inicializado.")

    print(f"Recebida requisição com a instrução: '{request.instrucao}'")
    
    prompt_completo = f"""
    **Tarefa:** Você é um especialista em análise de dados e planilhas.
    **Instrução do Usuário:** {request.instrucao}
    **Dados da Planilha (em formato de texto/CSV):**
    ---
    {request.dados_planilha}
    ---
    **Sua Resposta:** Forneça uma análise clara e objetiva.
    """
    
    try:
        response = model.generate_content(prompt_completo)
        # Adicionamos uma verificação extra para garantir que a resposta não está bloqueada
        if not response.parts:
            print("❌ A resposta do modelo foi bloqueada ou veio vazia.")
            raise ValueError("A resposta da IA foi bloqueada, possivelmente por filtros de segurança ou outros motivos.")

        print("Análise gerada com sucesso pela API do Google.")
        return {"analise_concluida": True, "relatorio": response.text}
    except Exception as e:
        print(f"❌ Erro durante a comunicação com a API do Google: {e}")
        # Usamos HTTPException para retornar um erro de servidor adequado
        raise HTTPException(status_code=500, detail=str(e))
