import os
import re
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from mangaba_agent import MangabaAgent
import json

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

# Inicialize os dois agentes do Mangaba-ai
try:
    agente_relatorio = MangabaAgent(
        model=os.getenv("MODEL_NAME", "gemini-2.5-flash"),
        agent_id="analista_de_planilhas",
    )
    agente_grafico = MangabaAgent(
        model=os.getenv("MODEL_NAME", "gemini-2.5-flash"),
        agent_id="especialista_em_graficos",
    )
    print("✅ Agentes do Mangaba-ai inicializados com sucesso!")
except Exception as e:
    print(f"❌ Erro crítico ao inicializar os agentes de IA: {e}")
    agente_relatorio = None
    agente_grafico = None

class PlanilhaRequest(BaseModel):
    dados_planilha: str
    instrucao: str

# --- ENDPOINTS DA API ---

@app.get("/")
def rota_raiz():
    return {"mensagem": "Servidor do Agente de Análise de Planilhas está no ar!"}

@app.options("/analisar_planilha")
def cors_preflight_handler():
    return Response(status_code=200)

@app.post("/analisar_planilha")
def analisar_planilha(request: PlanilhaRequest):
    if not agente_relatorio or not agente_grafico:
        raise HTTPException(status_code=503, detail="Agentes de IA não inicializados.")

    print(f"Recebida requisição com a instrução: '{request.instrucao}'")
    
    # --- Passo 1: Gerar o Relatório de Análise (Agente 1) ---
    prompt_relatorio = f"""
    **Tarefa:** Você é um especialista em análise de dados e planilhas.
    **Instrução do Usuário:** {request.instrucao}
    **Dados da Planilha (em formato de texto/CSV):**
    ---
    {request.dados_planilha}
    ---
    **Sua Resposta:** Forneça uma análise clara e detalhada.
    """
    try:
        relatorio_analise = agente_relatorio.chat(prompt_relatorio)
        print("Análise gerada com sucesso pelo agente 'analista_de_planilhas'.")
    except Exception as e:
        print(f"❌ Erro na comunicação com o agente de relatório: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    # --- Passo 2: Gerar a Sugestão de Gráfico (Agente 2) ---
    prompt_grafico = f"""
    **Tarefa:** Com base na análise, gere uma resposta **EXCLUSIVAMENTE em formato JSON**, sem NENHUM texto adicional antes ou depois.
    **O JSON deve seguir este formato RIGOROSO:**
    {{
      "titulo": "Título do Gráfico",
      "tipo_grafico": "bar",
      "dados_grafico": [
        {{
          "label": "Nome da Categoria",
          "value": 100
        }},
        {{
          "label": "Outra Categoria",
          "value": 200
        }}
      ]
    }}
    
    **Análise de Dados:**
    ---
    {relatorio_analise}
    ---
    
    **Instrução:** Gere o JSON do gráfico mais relevante para a análise.
    """
    sugestao_grafico_json = {}
    try:
        sugestao_grafico_json_str = agente_grafico.chat(prompt_grafico)
        
        # Usa regex para encontrar o primeiro bloco JSON
        match = re.search(r'```json\s*(\{.*\})\s*```', sugestao_grafico_json_str, re.DOTALL)
        
        if match:
            cleaned_json_str = match.group(1)
            sugestao_grafico_json = json.loads(cleaned_json_str)
            print("Sugestão de gráfico gerada com sucesso pelo agente 'especialista_em_graficos'.")
        else:
            raise ValueError("Não foi encontrado um bloco de código JSON válido na resposta da IA.")

    except (json.JSONDecodeError, ValueError) as e:
        print(f"❌ Erro ao parsear a resposta do agente de gráficos: {e}")
        print(f"Resposta bruta da IA: {sugestao_grafico_json_str}")
        sugestao_grafico_json = {"error": "A IA retornou um JSON inválido."}
    except Exception as e:
        print(f"❌ Erro na comunicação com o agente de gráficos: {e}")
        sugestao_grafico_json = {"error": f"Erro na comunicação com a IA: {str(e)}"}

    return {
        "analise_concluida": True,
        "relatorio": relatorio_analise,
        "sugestao_grafico": sugestao_grafico_json
    }