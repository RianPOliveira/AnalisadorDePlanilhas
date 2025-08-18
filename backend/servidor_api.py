from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Importa o agente da Mangaba.ai
from mangaba_agent import MangabaAgent

# Carrega as variáveis do .env (GOOGLE_API_KEY e MODEL_NAME)
load_dotenv()

# --- Bloco de Inicialização ---
app = FastAPI()

# Adiciona CORS para permitir que o front-end em React acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua pelo domínio do seu front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = MangabaAgent()
print("✅ Servidor de API iniciado com o Agente Mangaba.ai pronto para uso!")
# --- Fim do Bloco de Inicialização ---


# Modelo de requisição esperado pelo endpoint
class PlanilhaRequest(BaseModel):
    dados_planilha: str
    instrucao: str


# Endpoint que o frontend vai chamar para análise
@app.post("/analisar_planilha")
def analisar_planilha(request: PlanilhaRequest):
    print(f"📩 Recebida requisição para analisar planilha com a instrução: '{request.instrucao}'")

    # Cria o prompt que será enviado ao agente
    prompt_completo = (
        f"Você é um assistente especializado em análise de planilhas."
        f" O usuário enviou os seguintes dados extraídos de uma planilha:\n\n"
        f"{request.dados_planilha}\n\n"
        f"Instrução do usuário: {request.instrucao}"
    )

    # Faz a chamada ao agente da Mangaba.ai
    try:
        resposta = agent.chat(prompt_completo)
        print("✅ Análise concluída com sucesso!")
        return {"analise_concluida": True, "relatorio": resposta}
    except Exception as e:
        print(f"❌ Erro ao processar a análise: {e}")
        return {"analise_concluida": False, "erro": str(e)}


# Endpoint de teste para saber se a API está no ar
@app.get("/")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

