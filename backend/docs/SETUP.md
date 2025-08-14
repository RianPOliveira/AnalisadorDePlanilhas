# Configuração do Ambiente - Mangaba AI

Este guia explica como configurar o ambiente de desenvolvimento para o projeto Mangaba AI.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta no Google AI Studio para obter API key
- Git (opcional, para controle de versão)

## 🚀 Configuração Rápida

### 1. Clone o Repositório

```bash
git clone <repository-url>
cd mangaba_ai
```

### 2. Crie um Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
# Dependências principais
pip install -r requirements.txt

# Dependências de desenvolvimento (opcional)
pip install -r requirements-test.txt
```

### 4. Configure as Variáveis de Ambiente

```bash
# Copie o template
cp .env.template .env

# Edite o arquivo .env com seus valores
# No Windows, use: copy .env.template .env
```

### 5. Obtenha sua API Key do Google

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada
5. Cole no arquivo `.env` na variável `GOOGLE_API_KEY`

### 6. Teste a Instalação

```bash
# Teste básico
python -c "from mangaba_agent import MangabaAgent; print('✅ Instalação OK!')"

# Execute os testes (opcional)
python -m pytest tests/ -v

# Execute um exemplo
python examples/basic_example.py
```

## ⚙️ Configuração Detalhada

### Variáveis de Ambiente Obrigatórias

| Variável | Descrição | Exemplo |
|----------|-----------|----------|
| `GOOGLE_API_KEY` | Chave da API do Google Generative AI | `AIzaSyC...` |

### Variáveis de Ambiente Opcionais

| Variável | Padrão | Descrição |
|----------|--------|----------|
| `MODEL_NAME` | `gemini-pro` | Modelo do Google a ser usado |
| `AGENT_NAME` | `MangabaAgent` | Nome padrão do agente |
| `USE_MCP` | `true` | Habilitar protocolo MCP |
| `USE_A2A` | `true` | Habilitar protocolo A2A |
| `LOG_LEVEL` | `INFO` | Nível de logging |
| `MAX_CONTEXTS` | `1000` | Máximo de contextos MCP |

### Configuração para Desenvolvimento

```bash
# No arquivo .env
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG
VERBOSE=true
ENABLE_METRICS=true
```

### Configuração para Produção

```bash
# No arquivo .env
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=WARNING
VERBOSE=false
ENABLE_METRICS=true
ENABLE_CACHE=true
```

### Configuração para Testes

```bash
# No arquivo .env.test
ENVIRONMENT=testing
DEBUG=true
LOG_LEVEL=DEBUG
MAX_CONTEXTS=50
API_TIMEOUT=10
```

## 🔧 Configurações Avançadas

### Cache e Performance

```bash
# Habilitar cache
ENABLE_CACHE=true
CACHE_TTL=60
CACHE_MAX_SIZE=1000

# Configurações de API
API_TIMEOUT=30
MAX_RETRIES=3
RATE_LIMIT=60
```

### Segurança

```bash
# Validação de entrada
ENABLE_INPUT_VALIDATION=true
MAX_INPUT_SIZE=10000
ENABLE_OUTPUT_SANITIZATION=true

# Padrões bloqueados
BLOCKED_PATTERNS=spam,malware,virus
```

### Logging

```bash
# Configuração de logs
LOG_LEVEL=INFO
LOG_FORMAT=detailed
LOG_FILE=logs/mangaba.log
```

## 🐳 Docker (Opcional)

Se preferir usar Docker:

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "mangaba_agent.py"]
```

```bash
# Build e execução
docker build -t mangaba-ai .
docker run -p 8000:8000 --env-file .env mangaba-ai
```

## 🧪 Executando Testes

### Testes Básicos

```bash
# Todos os testes
python -m pytest

# Testes com cobertura
python -m pytest --cov=. --cov-report=html

# Testes específicos
python -m pytest tests/test_mangaba_agent.py -v
```

### Testes por Categoria

```bash
# Apenas testes unitários
python -m pytest -m unit

# Apenas testes de integração
python -m pytest -m integration

# Testes de performance
python -m pytest -m performance
```

## 📊 Monitoramento

### Métricas Básicas

```bash
# Habilitar métricas
ENABLE_METRICS=true
METRICS_INTERVAL=60

# URL de monitoramento
MONITORING_URL=https://your-monitoring-service.com
MONITORING_API_KEY=your_api_key
```

### Logs Estruturados

```bash
# Formato JSON para logs
LOG_FORMAT=json
LOG_FILE=logs/mangaba.json
```

## 🔍 Troubleshooting

### Problemas Comuns

#### 1. Erro de API Key

```
Erro: Invalid API key
```

**Solução:**
- Verifique se a API key está correta no arquivo `.env`
- Confirme se a API key está ativa no Google AI Studio
- Verifique se não há espaços extras na chave

#### 2. Erro de Importação

```
ModuleNotFoundError: No module named 'mangaba_agent'
```

**Solução:**
- Certifique-se de estar no diretório correto
- Ative o ambiente virtual
- Reinstale as dependências

#### 3. Erro de Permissão

```
PermissionError: [Errno 13] Permission denied
```

**Solução:**
- Execute com permissões adequadas
- Verifique se o diretório de logs existe
- Ajuste as permissões do arquivo `.env`

#### 4. Timeout de API

```
TimeoutError: Request timed out
```

**Solução:**
- Aumente o valor de `API_TIMEOUT`
- Verifique sua conexão com a internet
- Reduza o tamanho das requisições

### Debug Mode

```bash
# Habilitar debug completo
DEBUG=true
VERBOSE=true
LOG_LEVEL=DEBUG

# Executar com debug
python -u mangaba_agent.py
```

### Verificação de Saúde

```python
# health_check.py
from mangaba_agent import MangabaAgent
import os

def health_check():
    try:
        # Verifica variáveis de ambiente
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            return "❌ GOOGLE_API_KEY não configurada"
        
        # Testa criação do agente
        agent = MangabaAgent(api_key=api_key)
        
        # Testa chat básico
        response = agent.chat("Olá")
        
        if response:
            return "✅ Sistema funcionando corretamente"
        else:
            return "⚠️ Sistema parcialmente funcional"
            
    except Exception as e:
        return f"❌ Erro: {str(e)}"

if __name__ == "__main__":
    print(health_check())
```

## 📚 Próximos Passos

1. **Explore os Exemplos**: Veja a pasta `examples/` para casos de uso
2. **Leia a Documentação**: Consulte `PROTOCOLS.md` para detalhes técnicos
3. **Execute os Testes**: Garanta que tudo está funcionando
4. **Personalize**: Ajuste as configurações para suas necessidades
5. **Contribua**: Veja como contribuir no `README.md`

## 🆘 Suporte

Se encontrar problemas:

1. Consulte este guia de configuração
2. Verifique os logs de erro
3. Execute o health check
4. Consulte a documentação
5. Abra uma issue no repositório

---

**Nota**: Mantenha sempre suas chaves de API seguras e nunca as commite no controle de versão!