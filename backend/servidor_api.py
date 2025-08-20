# servidor_api.py (Versão final com handler OPTIONS manual)

import os
from fastapi import FastAPI, Response, HTTPException # Adicionamos Response aqui
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

# --- CONFIGURAÇÃO E INICIALIZAÇÃO ---
load_dotenv()
app = FastAPI()

# --- BLOCO DE CONFIGURAÇÃO DO CORS ---
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
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


class PlanilhaRequest(BaseModel):
    dados_planilha: str
    instrucao: str

# --- ENDPOINTS DA API ---

@app.get("/")
def rota_raiz():
    return {"mensagem": "Servidor do Agente de Análise de Planilhas está no ar!"}

# --- INÍCIO DA CORREÇÃO FINAL PARA O CORS ---
# Este endpoint manual irá capturar o pedido de permissão OPTIONS
# e responder que está tudo OK, antes que o pedido POST real chegue.
@app.options("/analisar_planilha")
def cors_preflight_handler():
    return Response(status_code=200)
# --- FIM DA CORREÇÃO FINAL PARA O CORS ---

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
        if not response.parts:
            raise ValueError("A resposta da IA foi bloqueada.")

        print("Análise gerada com sucesso pela API do Google.")
        return {"analise_concluida": True, "relatorio": response.text}
    except Exception as e:
        print(f"❌ Erro durante a comunicação com a API do Google: {e}")
        raise HTTPException(status_code=500, detail=str(e))
