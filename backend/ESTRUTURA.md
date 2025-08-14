# 📁 Estrutura do Repositório - Mangaba AI

Este documento descreve a organização completa do repositório Mangaba AI.

## 🏗️ Visão Geral da Estrutura

```
mangaba_ai/
├── 📚 DOCUMENTAÇÃO
│   ├── README.md                    # Visão geral do projeto
│   ├── CURSO_BASICO.md             # 🎓 Curso completo para iniciantes
│   ├── SETUP.md                    # Guia de configuração
│   ├── PROTOCOLS.md                # Documentação dos protocolos
│   ├── SCRIPTS.md                  # Documentação dos scripts
│   ├── CHANGELOG.md                # Histórico de mudanças
│   ├── ESTRUTURA.md                # Este arquivo
│   └── LICENSE                     # Licença do projeto
│
├── 🔧 CONFIGURAÇÃO
│   ├── .env                        # Configurações do ambiente
│   ├── .env.template               # Template de configuração
│   ├── config.py                   # Sistema de configuração
│   ├── config_template.json        # Template JSON das configurações
│   └── .gitignore                  # Arquivos ignorados pelo Git
│
├── 🚀 SCRIPTS DE SETUP
│   ├── quick_setup.py              # Setup automático completo
│   ├── setup_env.py                # Setup alternativo
│   ├── validate_env.py             # Validação do ambiente
│   ├── example_env_usage.py        # Exemplo de uso das configurações
│   └── exemplo_curso_basico.py     # Exemplos práticos do curso
│
├── 🤖 CÓDIGO PRINCIPAL
│   ├── __init__.py                 # Inicialização do pacote
│   ├── mangaba_agent.py            # Agente principal
│   ├── protocols/                  # Protocolos de comunicação
│   │   ├── __init__.py
│   │   ├── mcp.py                  # Model Context Protocol
│   │   └── a2a.py                  # Agent-to-Agent Protocol
│   └── utils/                      # Utilitários
│       ├── __init__.py
│       └── logger.py               # Sistema de logging
│
├── 📖 EXEMPLOS
│   ├── basic_example.py            # Exemplo básico
│   ├── document_analysis_example.py # Análise de documentos
│   ├── task_automation_example.py  # Automação de tarefas
│   ├── api_integration_example.py  # Integração com APIs
│   ├── text_analysis_example.py    # Análise de texto
│   ├── translation_example.py      # Tradução
│   ├── finance_example.py          # Aplicações financeiras
│   ├── legal_example.py            # Aplicações jurídicas
│   ├── medical_example.py          # Aplicações médicas
│   ├── marketing_example.py        # Marketing e vendas
│   ├── administration_example.py   # Administração
│   └── ml_analytics_example.py     # Machine Learning e Analytics
│
├── 🧪 TESTES
│   ├── __init__.py
│   ├── conftest.py                 # Configurações do pytest
│   ├── test_mangaba_agent.py       # Testes do agente principal
│   ├── test_mcp_protocol.py        # Testes do protocolo MCP
│   ├── test_a2a_protocol.py        # Testes do protocolo A2A
│   └── test_integration.py         # Testes de integração
│
├── 📦 DEPENDÊNCIAS
│   ├── requirements.txt            # Dependências principais
│   ├── requirements-test.txt       # Dependências de teste
│   ├── setup.py                    # Configuração do pacote
│   └── pytest.ini                 # Configuração do pytest
│
├── 📁 ORGANIZAÇÃO
│   ├── docs/                       # Documentação organizada
│   │   └── README.md
│   └── scripts/                    # Scripts organizados
│       └── README.md
│
└── 🔍 OUTROS
    ├── test_basic.py               # Teste básico de funcionamento
    └── .pytest_cache/              # Cache do pytest (ignorado)
```

## 📋 Categorias de Arquivos

### 🎯 Para Iniciantes
- `CURSO_BASICO.md` - **Comece aqui!** Curso completo
- `README.md` - Visão geral e instalação
- `SETUP.md` - Configuração detalhada
- `examples/basic_example.py` - Primeiro exemplo

### 🔧 Para Configuração
- `quick_setup.py` - Setup automático
- `validate_env.py` - Validação
- `.env.template` - Template de configuração
- `config.py` - Sistema de configuração

### 👩‍💻 Para Desenvolvedores
- `mangaba_agent.py` - Código principal
- `protocols/` - Protocolos MCP e A2A
- `tests/` - Testes unitários e integração
- `utils/` - Utilitários e helpers

### 📚 Para Aprendizado
- `examples/` - Exemplos práticos por área
- `exemplo_curso_basico.py` - Exemplos do curso
- `PROTOCOLS.md` - Documentação técnica

## 🎯 Fluxos de Uso

### 🆕 Novo Usuário
```
1. README.md → Visão geral
2. CURSO_BASICO.md → Aprender conceitos
3. quick_setup.py → Configurar ambiente
4. exemplo_curso_basico.py → Testar na prática
5. examples/ → Explorar casos de uso
```

### 🔧 Configuração
```
1. .env.template → Ver configurações disponíveis
2. quick_setup.py → Setup automático
3. validate_env.py → Validar configuração
4. example_env_usage.py → Testar configurações
```

### 👨‍💻 Desenvolvimento
```
1. mangaba_agent.py → Entender o agente principal
2. protocols/ → Estudar protocolos
3. tests/ → Executar testes
4. examples/ → Ver implementações
5. utils/ → Usar utilitários
```

## 📊 Métricas do Projeto

### 📁 Arquivos por Categoria
- **Documentação**: 8 arquivos
- **Código Principal**: 6 arquivos
- **Exemplos**: 12 arquivos
- **Testes**: 5 arquivos
- **Configuração**: 8 arquivos
- **Scripts**: 5 arquivos

### 📈 Linhas de Código (aproximado)
- **Código Python**: ~3000 linhas
- **Documentação**: ~2000 linhas
- **Testes**: ~1500 linhas
- **Exemplos**: ~2500 linhas

## 🎨 Convenções de Nomenclatura

### 📄 Arquivos
- **Documentação**: `MAIUSCULO.md`
- **Código**: `snake_case.py`
- **Exemplos**: `*_example.py`
- **Testes**: `test_*.py`
- **Scripts**: `*_setup.py`, `validate_*.py`

### 📁 Pastas
- **Código**: `snake_case/`
- **Documentação**: `docs/`
- **Organização**: `scripts/`, `examples/`, `tests/`

### 🏷️ Emojis nos Títulos
- 📚 Documentação
- 🔧 Configuração
- 🤖 Código Principal
- 📖 Exemplos
- 🧪 Testes
- 🎓 Educacional
- 🚀 Scripts

## 🔄 Manutenção

### 📅 Atualizações Regulares
- `CHANGELOG.md` - A cada versão
- `requirements.txt` - Quando dependências mudam
- `README.md` - Quando funcionalidades mudam
- `CURSO_BASICO.md` - Quando conceitos evoluem

### 🧹 Limpeza
- Cache do pytest: `.pytest_cache/`
- Logs temporários: `*.log`
- Arquivos de configuração pessoal: `.env`
- Bytecode Python: `__pycache__/`

## 🎯 Próximas Melhorias

### 📁 Estrutura
- [ ] Mover scripts para `scripts/`
- [ ] Organizar documentação em `docs/`
- [ ] Criar `tools/` para utilitários
- [ ] Adicionar `assets/` para recursos

### 📚 Documentação
- [ ] API Reference automática
- [ ] Tutoriais específicos
- [ ] Guias de contribuição
- [ ] Documentação de arquitetura

### 🔧 Automação
- [ ] CI/CD pipeline
- [ ] Testes automáticos
- [ ] Deploy automático
- [ ] Validação de código

---

## 🤝 Contribuição

Para contribuir com a organização do repositório:

1. **Siga as convenções** estabelecidas
2. **Atualize a documentação** quando necessário
3. **Mantenha a estrutura** consistente
4. **Use emojis** nos títulos para clareza visual

---

*Este documento é atualizado regularmente para refletir a estrutura atual do projeto.*