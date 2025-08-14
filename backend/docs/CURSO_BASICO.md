# 📚 Curso Básico - Mangaba AI

## 🎯 Bem-vindo ao Mangaba AI!

Este curso básico irá te guiar através dos conceitos fundamentais e uso prático do Mangaba AI, um sistema de agentes de IA versátil com protocolos avançados de comunicação.

---

## 📋 Índice

1. [Introdução](#1-introdução)
2. [Conceitos Fundamentais](#2-conceitos-fundamentais)
3. [Arquitetura do Sistema](#3-arquitetura-do-sistema)
4. [Configuração Inicial](#4-configuração-inicial)
5. [Primeiro Uso](#5-primeiro-uso)
6. [Protocolos Avançados](#6-protocolos-avançados)
7. [Exemplos Práticos](#7-exemplos-práticos)
8. [Troubleshooting](#8-troubleshooting)
9. [Próximos Passos](#9-próximos-passos)

---

## 1. Introdução

### O que é o Mangaba AI?

O **Mangaba AI** é um sistema de agentes de inteligência artificial que combina:

- 🤖 **Agente Principal**: Baseado no Google Generative AI (Gemini)
- 🔗 **Protocolo MCP**: Model Context Protocol para gerenciamento de contexto
- 🌐 **Protocolo A2A**: Agent-to-Agent para comunicação entre agentes
- ⚡ **Performance**: Otimizado para alta performance e escalabilidade

### Para que serve?

- Automação de tarefas complexas
- Análise de documentos e textos
- Comunicação entre múltiplos agentes
- Processamento de linguagem natural avançado
- Integração com APIs e sistemas externos

---

## 2. Conceitos Fundamentais

### 2.1 Agente de IA

Um **agente** é uma entidade autônoma que:
- Recebe entradas (prompts, dados)
- Processa informações usando IA
- Gera respostas ou executa ações
- Mantém contexto entre interações

### 2.2 Protocolos de Comunicação

#### MCP (Model Context Protocol)
- Gerencia contextos de conversação
- Mantém histórico e estado
- Permite recuperação de informações relevantes

#### A2A (Agent-to-Agent)
- Comunicação entre diferentes agentes
- Distribuição de tarefas
- Colaboração em tempo real

### 2.3 Contexto

O **contexto** inclui:
- Histórico de conversas
- Dados relevantes
- Configurações específicas
- Estado atual do agente

---

## 3. Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────┐
│                    MANGABA AI                           │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Agente    │  │     MCP     │  │     A2A     │     │
│  │  Principal  │  │  Protocol   │  │  Protocol   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Config    │  │   Logger    │  │   Utils     │     │
│  │   System    │  │   System    │  │   System    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│              Google Generative AI (Gemini)             │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Configuração Inicial

### 4.1 Pré-requisitos

- Python 3.8+
- Chave da API do Google Generative AI
- Ambiente virtual (recomendado)

### 4.2 Instalação Rápida

```bash
# 1. Clone o repositório
git clone <repository-url>
cd mangaba_ai

# 2. Execute o setup automático
python quick_setup.py
```

### 4.3 Configuração Manual

```bash
# 1. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar .env
cp .env.template .env
# Edite o .env com sua API key
```

### 4.4 Obter API Key do Google

1. Acesse: https://makersuite.google.com/app/apikey
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada
5. Cole no arquivo `.env`:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

### 4.5 Validação

```bash
# Verificar se tudo está funcionando
python validate_env.py
```

---

## 5. Primeiro Uso

### 5.1 Exemplo Básico

```python
# exemplo_basico.py
from mangaba_agent import MangabaAgent

# Criar agente
agent = MangabaAgent()

# Primeira conversa
resposta = agent.chat("Olá! Como você pode me ajudar?")
print(resposta)

# Continuar conversa
resposta = agent.chat("Explique sobre inteligência artificial")
print(resposta)
```

### 5.2 Executar Exemplo

```bash
python exemplo_basico.py
```

### 5.3 Resultado Esperado

```
Olá! Sou o Mangaba AI, um agente de inteligência artificial...

Inteligência Artificial (IA) é um campo da ciência da computação...
```

---

## 6. Protocolos Avançados

### 6.1 Usando MCP (Model Context Protocol)

```python
from mangaba_agent import MangabaAgent
from protocols.mcp import MCPProtocol

# Criar agente com MCP
agent = MangabaAgent()
mcp = MCPProtocol()
agent.add_protocol(mcp)

# Adicionar contexto
mcp.add_context(
    content="Usuário trabalha em uma empresa de tecnologia",
    context_type="user_info",
    priority=1
)

# Chat com contexto
resposta = agent.chat("Que tipo de projetos posso desenvolver?")
print(resposta)
```

### 6.2 Usando A2A (Agent-to-Agent)

```python
from mangaba_agent import MangabaAgent
from protocols.a2a import A2AProtocol

# Criar dois agentes
agent1 = MangabaAgent(agent_name="Analista")
agent2 = MangabaAgent(agent_name="Escritor")

# Configurar A2A
a2a1 = A2AProtocol(port=8080)
a2a2 = A2AProtocol(port=8081)

agent1.add_protocol(a2a1)
agent2.add_protocol(a2a2)

# Conectar agentes
a2a1.connect_to_agent("localhost", 8081)

# Comunicação
mensagem = "Analise este texto: 'Python é uma linguagem versátil'"
resposta = agent1.send_to_agent("Escritor", mensagem)
print(resposta)
```

---

## 7. Exemplos Práticos

### 7.1 Análise de Documentos

```python
# Exemplo: Analisar um documento
from mangaba_agent import MangabaAgent

agent = MangabaAgent()

# Ler arquivo
with open("documento.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Analisar
resposta = agent.chat(f"""
Analise este documento e forneça:
1. Resumo principal
2. Pontos importantes
3. Conclusões

Documento:
{texto}
""")

print(resposta)
```

### 7.2 Automação de Tarefas

```python
# Exemplo: Gerar relatório automático
from mangaba_agent import MangabaAgent
from datetime import datetime

agent = MangabaAgent()

# Dados de exemplo
vendas = {
    "janeiro": 15000,
    "fevereiro": 18000,
    "março": 22000
}

# Gerar relatório
resposta = agent.chat(f"""
Crie um relatório de vendas profissional com base nestes dados:
{vendas}

Incluir:
- Análise de tendências
- Comparações mensais
- Recomendações
- Formatação em markdown
""")

print(resposta)

# Salvar relatório
with open(f"relatorio_{datetime.now().strftime('%Y%m%d')}.md", "w") as f:
    f.write(resposta)
```

### 7.3 Processamento de Múltiplas Tarefas

```python
# Exemplo: Pipeline de processamento
from mangaba_agent import MangabaAgent
from protocols.mcp import MCPProtocol

agent = MangabaAgent()
mcp = MCPProtocol()
agent.add_protocol(mcp)

# Tarefa 1: Análise
analise = agent.chat("Analise as tendências do mercado de IA em 2024")
mcp.add_context(analise, "market_analysis")

# Tarefa 2: Estratégia (usando contexto da análise)
estrategia = agent.chat("Com base na análise anterior, sugira uma estratégia de negócios")
mcp.add_context(estrategia, "business_strategy")

# Tarefa 3: Plano de ação
plano = agent.chat("Crie um plano de ação detalhado baseado na estratégia")

print("=== ANÁLISE ===")
print(analise)
print("\n=== ESTRATÉGIA ===")
print(estrategia)
print("\n=== PLANO ===")
print(plano)
```

---

## 8. Troubleshooting

### 8.1 Problemas Comuns

#### Erro: "API_KEY não encontrada"
```bash
# Solução:
1. Verificar se o arquivo .env existe
2. Confirmar se GOOGLE_API_KEY está definida
3. Executar: python validate_env.py
```

#### Erro: "Module not found"
```bash
# Solução:
1. Ativar ambiente virtual
2. Reinstalar dependências: pip install -r requirements.txt
3. Verificar versão do Python: python --version
```

#### Erro de Unicode no Windows
```bash
# Solução:
1. Usar PowerShell em vez de CMD
2. Configurar encoding: chcp 65001
3. Usar Python 3.8+ com suporte UTF-8
```

### 8.2 Logs e Debug

```python
# Habilitar logs detalhados
import logging
logging.basicConfig(level=logging.DEBUG)

# Ou configurar no .env
LOG_LEVEL=DEBUG
DEBUG_MODE=true
```

### 8.3 Validação Completa

```bash
# Executar todos os testes
python validate_env.py

# Verificar configurações
python example_env_usage.py

# Testar funcionalidades básicas
python test_basic.py
```

---

## 9. Próximos Passos

### 9.1 Aprofundamento

1. **Leia a documentação completa**:
   - `README.md` - Visão geral
   - `PROTOCOLS.md` - Detalhes dos protocolos
   - `SETUP.md` - Configuração avançada

2. **Explore os exemplos**:
   - `examples/` - Casos de uso específicos
   - `tests/` - Testes e validações

3. **Experimente configurações avançadas**:
   - Cache personalizado
   - Rate limiting
   - Métricas e monitoramento

### 9.2 Desenvolvimento

```python
# Criar seu próprio agente especializado
class MeuAgente(MangabaAgent):
    def __init__(self):
        super().__init__()
        self.especialidade = "análise financeira"
    
    def analisar_financas(self, dados):
        prompt = f"""
        Como especialista em {self.especialidade}, 
        analise estes dados: {dados}
        """
        return self.chat(prompt)
```

### 9.3 Integração

- APIs REST
- Bancos de dados
- Sistemas de arquivos
- Serviços em nuvem
- Interfaces web

### 9.4 Comunidade

- Contribua com exemplos
- Reporte bugs
- Sugira melhorias
- Compartilhe casos de uso

---

## 🎉 Parabéns!

Você completou o curso básico do Mangaba AI! Agora você tem o conhecimento fundamental para:

✅ Configurar e usar o sistema  
✅ Criar agentes de IA funcionais  
✅ Implementar protocolos avançados  
✅ Desenvolver soluções práticas  
✅ Resolver problemas comuns  

### 📚 Recursos Adicionais

- **Documentação**: Consulte os arquivos `.md` do projeto
- **Exemplos**: Explore a pasta `examples/`
- **Testes**: Execute `pytest` para ver mais casos
- **Validação**: Use `python validate_env.py` sempre que precisar

### 🚀 Continue Aprendendo

O Mangaba AI é uma ferramenta poderosa. Quanto mais você experimentar, mais possibilidades descobrirá!

**Boa sorte em seus projetos com IA! 🤖✨**

---

*Última atualização: Dezembro 2024*