# 🔧 Scripts de Configuração - Mangaba AI

Esta pasta contém todos os scripts de configuração e validação do projeto.

## 📋 Scripts Disponíveis

### 🚀 Configuração Inicial
- [quick_setup.py](../quick_setup.py) - Setup automático completo
- [setup_env.py](../setup_env.py) - Setup alternativo

### ✅ Validação
- [validate_env.py](../validate_env.py) - Validação completa do ambiente
- [example_env_usage.py](../example_env_usage.py) - Exemplo de uso das configurações

### 🎓 Exemplos Educacionais
- [exemplo_curso_basico.py](../exemplo_curso_basico.py) - Exemplos práticos do curso básico

## 🎯 Como Usar

### Para Novos Usuários
```bash
# Setup completo automático
python quick_setup.py

# Validar configuração
python validate_env.py

# Testar com exemplos
python exemplo_curso_basico.py
```

### Para Desenvolvedores
```bash
# Setup manual
python setup_env.py

# Verificar configurações
python example_env_usage.py

# Validação detalhada
python validate_env.py --verbose
```

## 📊 Fluxo de Configuração

```
1. quick_setup.py     → Configuração automática
   ↓
2. validate_env.py    → Validação do ambiente
   ↓
3. exemplo_curso_basico.py → Teste prático
```

## 🔍 Troubleshooting

Se algum script falhar:

1. **Verifique os pré-requisitos**:
   - Python 3.8+
   - Pip atualizado
   - Conexão com internet

2. **Execute a validação**:
   ```bash
   python validate_env.py
   ```

3. **Consulte a documentação**:
   - [SETUP.md](../SETUP.md) - Configuração detalhada
   - [SCRIPTS.md](../SCRIPTS.md) - Documentação dos scripts

## 📁 Estrutura

```
scripts/
├── README.md          # Este arquivo
├── setup/            # Scripts de configuração (futuro)
├── validation/       # Scripts de validação (futuro)
└── examples/         # Scripts de exemplo (futuro)
```

---

*Para mais informações, consulte [SCRIPTS.md](../SCRIPTS.md)*