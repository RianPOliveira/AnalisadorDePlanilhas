# servidor_api.py

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# A importação continua a mesma
from mangaba_agent import MangabaAgent

# Carrega as variáveis do .env (GOOGLE_API_KEY e MODEL_NAME)
load_dotenv()

# --- Bloco de Inicialização ---
app = FastAPI()
agent = MangabaAgent()
print("✅ Servidor de API iniciado com o Agente Mangaba.ai pronto para uso!")
# --- Fim do Bloco de Inicialização ---


# O nosso modelo de requisição já é perfeito para isso, não precisa mudar.
class PlanilhaRequest(BaseModel):
    dados_planilha: str
    instrucao: str


# O endpoint que o seu frontend vai chamar
@app.post("/analisar_planilha")
def analisar_planilha(request: PlanilhaRequest):
    print(f"Recebida requisição para analisar planilha com a instrução: '{request.instrucao}'")
    
    # --- LÓGICA DE PROMPT APRIMORADA (Inspirada no Exemplo) ---
    # Aqui montamos uma instrução completa e detalhada para a IA
    prompt_completo = f"""
    **Tarefa:** Você é um especialista em análise de dados e planilhas.
    
    **Instrução do Usuário:** {request.instrucao}
    
    **Dados da Planilha (em formato de texto/CSV):**
    ---
    {request.dados_planilha}
    ---
    
    **Sua Resposta:** Forneça uma análise clara e objetiva baseada na instrução e nos dados fornecidos.
    """
    # --- FIM DA LÓGICA DE PROMPT ---
    
    try:
        # Usamos o método .chat() que é o mais poderoso, como vimos no exemplo
        analise = agent.chat(prompt_completo)
        
        print("Análise gerada pelo agente com sucesso.")
        return {"analise_concluida": True, "relatorio": analise}
    except Exception as e:
        print(f"❌ Erro durante a análise do agente: {e}")
        return {"analise_concluida": False, "erro": str(e)}

@app.get("/")
def rota_raiz():
    return {"mensagem": "Servidor do Agente de Análise de Planilhas está no ar!"}