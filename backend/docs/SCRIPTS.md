# 📋 Scripts de Configuração e Validação

Este documento descreve os scripts auxiliares disponíveis no projeto Mangaba AI para facilitar a configuração e validação do ambiente.

## 📁 Visão Geral dos Scripts

| Script | Descrição | Uso Principal |
|--------|-----------|---------------|
| `quick_setup.py` | Configuração automática completa | Primeiro uso |
| `validate_env.py` | Validação do ambiente | Verificação e diagnóstico |
| `setup_env.py` | Configuração básica | Configuração manual |

## 🚀 quick_setup.py

### Descrição
Script de configuração automática que executa todo o processo de setup inicial em um único comando.

### Funcionalidades
- ✅ Verifica versão do Python (3.8+)
- ✅ Cria ambiente virtual automaticamente
- ✅ Atualiza pip para versão mais recente
- ✅ Instala dependências principais e de teste
- ✅ Configura arquivo .env interativamente
- ✅ Testa instalação básica
- ✅ Executa validação final

### Uso

```bash
# Configuração completa (modo interativo)
python quick_setup.py

# Pular validação final
python quick_setup.py --skip-validation

# Modo não-interativo (em desenvolvimento)
python quick_setup.py --non-interactive
```

### Processo Passo a Passo

1. **Verificação do Python**: Confirma Python 3.8+
2. **Ambiente Virtual**: Cria `venv/` se não existir
3. **Atualização do pip**: Garante pip atualizado
4. **Dependências**: Instala de `requirements.txt` e `requirements-test.txt`
5. **Configuração .env**: 
   - Copia `.env.template` para `.env`
   - Solicita Google API Key
   - Configura opções básicas
6. **Teste de Instalação**: Verifica imports básicos
7. **Validação Final**: Executa `validate_env.py`

### Exemplo de Execução

```
============================================================
    MANGABA AI - CONFIGURAÇÃO RÁPIDA
============================================================
Este script irá configurar automaticamente o ambiente.
Pressione Ctrl+C a qualquer momento para cancelar.

🚀 Iniciando configuração automática...

🔄 Verificar Python...
✅ Verificar Python
   Python 3.11.0 OK

🔄 Criar ambiente virtual...
✅ Criar Ambiente Virtual
   Criado em venv

📝 Configuração do arquivo .env:
Pressione Enter para usar valores padrão.

🔑 Google API Key (obrigatório): AIza...
🤖 Nome do modelo [gemini-pro]: 
👤 Nome do agente [MangabaAgent]: 
📊 Nível de log [INFO]: 

✅ Configurar .env
   Arquivo .env configurado com sucesso

🎉 CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!
```

## 🔍 validate_env.py

### Descrição
Script de validação abrangente que verifica se o ambiente está configurado corretamente.

### Verificações Realizadas

#### ✅ Verificações Básicas
- **Python Version**: Confirma Python 3.8+
- **Required Files**: Verifica arquivos obrigatórios do projeto
- **Environment File**: Confirma existência e conteúdo do .env

#### ⚙️ Verificações de Configuração
- **Environment Variables**: Valida variáveis obrigatórias e opcionais
- **Dependencies**: Confirma pacotes instalados
- **Imports**: Testa imports dos módulos principais

#### 🌐 Verificações de Conectividade
- **API Connectivity**: Testa configuração da Google API
- **Test Environment**: Verifica ambiente de testes

### Uso

```bash
# Validação completa (modo visual)
python validate_env.py

# Salvar relatório em JSON
python validate_env.py --save-report

# Output apenas em JSON (para automação)
python validate_env.py --json-output
```

### Exemplo de Saída

```
============================================================
    MANGABA AI - VALIDAÇÃO DO AMBIENTE
============================================================
Verificando se o ambiente está configurado corretamente...

Executando verificações...

🔍 Versão do Python... OK
🔍 Arquivos obrigatórios... OK
🔍 Arquivo .env... OK
🔍 Variáveis de ambiente... OK
🔍 Dependências... OK
🔍 Imports... OK
🔍 Conectividade API... OK
🔍 Ambiente de testes... OK

============================================================
    RESUMO DA VALIDAÇÃO
============================================================
Total de verificações: 15
✅ Sucessos: 15
⚠️  Avisos: 0
❌ Erros: 0
⏭️  Pulados: 0

🎉 AMBIENTE TOTALMENTE CONFIGURADO!
Você pode começar a usar o Mangaba AI.
```

### Relatório JSON

Com `--save-report`, gera `validation_report.json`:

```json
{
  "timestamp": "2024-01-15T10:30:00",
  "summary": {
    "total_tests": 15,
    "ok_count": 15,
    "warning_count": 0,
    "error_count": 0,
    "skip_count": 0
  },
  "results": [
    {
      "test": "Python Version",
      "status": "OK",
      "message": "Python 3.11.0",
      "details": "Versão completa: 3.11.0",
      "timestamp": "2024-01-15T10:30:01"
    }
  ],
  "environment": {
    "python_version": "3.11.0",
    "platform": "win32",
    "working_directory": "C:\\path\\to\\mangaba_ai"
  }
}
```

## 🛠️ setup_env.py

### Descrição
Script de configuração básica, mais simples que o `quick_setup.py`.

### Funcionalidades
- ✅ Verifica Python e pip
- ✅ Cria ambiente virtual
- ✅ Instala dependências básicas
- ✅ Configura .env a partir do template
- ✅ Teste básico de instalação

### Uso

```bash
python setup_env.py
```

## 🎯 Quando Usar Cada Script

### 🆕 Primeira Configuração
**Use: `quick_setup.py`**
- Configuração completa e automática
- Ideal para novos usuários
- Inclui validação final

### 🔧 Verificação de Problemas
**Use: `validate_env.py`**
- Diagnóstico de problemas
- Verificação após mudanças
- Relatórios para suporte

### ⚡ Configuração Rápida
**Use: `setup_env.py`**
- Configuração básica apenas
- Quando você sabe o que está fazendo
- Automação em CI/CD

## 🚨 Solução de Problemas

### Erro: "Python 3.8+ necessário"
```bash
# Verifique sua versão do Python
python --version

# Instale Python 3.8+ se necessário
# Windows: https://python.org/downloads/
# Linux: sudo apt install python3.8
# macOS: brew install python@3.8
```

### Erro: "Google API Key não configurada"
```bash
# 1. Obtenha uma chave em:
# https://makersuite.google.com/app/apikey

# 2. Configure no .env:
echo "GOOGLE_API_KEY=sua_chave_aqui" >> .env

# 3. Valide:
python validate_env.py
```

### Erro: "Dependências não instaladas"
```bash
# Reinstale dependências
pip install -r requirements.txt
pip install -r requirements-test.txt

# Ou use o setup automático
python quick_setup.py
```

### Erro: "Imports falhando"
```bash
# Verifique se está no diretório correto
pwd  # ou cd no Windows

# Verifique se os arquivos existem
ls mangaba_agent.py protocols/

# Reinstale se necessário
python quick_setup.py
```

## 📊 Códigos de Saída

| Código | Significado | Ação |
|--------|-------------|-------|
| 0 | Sucesso | Continuar |
| 1 | Erro geral | Verificar logs |
| 130 | Cancelado (Ctrl+C) | Normal |

## 🔄 Automação

### CI/CD
```yaml
# Exemplo para GitHub Actions
- name: Setup Mangaba AI
  run: |
    python quick_setup.py --non-interactive
    python validate_env.py --json-output
```

### Scripts de Deploy
```bash
#!/bin/bash
# deploy.sh
set -e

echo "Configurando Mangaba AI..."
python quick_setup.py --skip-validation

echo "Validando ambiente..."
if python validate_env.py --json-output | jq -r '.summary.valid' | grep -q true; then
    echo "✅ Ambiente válido"
else
    echo "❌ Ambiente inválido"
    exit 1
fi

echo "🚀 Deploy concluído!"
```

## 📝 Logs e Debugging

### Logs Detalhados
```bash
# Para debugging, use verbose
python quick_setup.py 2>&1 | tee setup.log
python validate_env.py --save-report 2>&1 | tee validation.log
```

### Variáveis de Debug
```bash
# Ative logs detalhados
export DEBUG=1
export LOG_LEVEL=DEBUG

python validate_env.py
```

## 🤝 Contribuindo

Para melhorar os scripts:

1. **Adicione novas verificações** em `validate_env.py`
2. **Melhore a experiência** em `quick_setup.py`
3. **Adicione testes** para os scripts
4. **Documente mudanças** neste arquivo

### Estrutura dos Scripts
```
scripts/
├── quick_setup.py      # Configuração automática
├── validate_env.py     # Validação completa
├── setup_env.py        # Configuração básica
└── SCRIPTS.md          # Esta documentação
```

---

💡 **Dica**: Sempre execute `validate_env.py` após fazer mudanças no ambiente para garantir que tudo está funcionando corretamente.