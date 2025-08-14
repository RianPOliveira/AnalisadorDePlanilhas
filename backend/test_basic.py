#!/usr/bin/env python3
"""Teste básico para verificar se o agente está funcionando."""

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

def test_imports():
    """Testa se todos os imports estão funcionando."""
    try:
        from mangaba_ai import MangabaAgent
        from config import config
        from utils.logger import get_logger
        print("✅ Todos os imports funcionaram!")
        return True
    except ImportError as e:
        print(f"❌ Erro no import: {e}")
        return False

def test_config():
    """Testa se a configuração está funcionando."""
    try:
        from config import config
        print(f"✅ Configuração carregada: {config}")
        
        # Verifica se a API key está configurada
        if config.api_key and config.api_key != "cole_sua_chave_aqui":
            print("✅ API key configurada!")
            return True
        else:
            print("⚠️  API key não configurada. Configure no arquivo .env")
            return False
    except Exception as e:
        print(f"❌ Erro na configuração: {e}")
        return False

def test_agent_creation():
    """Testa se o agente pode ser criado."""
    try:
        from mangaba_ai import MangabaAgent
        
        # Verifica se a API key está configurada
        if not os.getenv('API_KEY') or os.getenv('API_KEY') == "cole_sua_chave_aqui":
            print("⚠️  Pulando teste do agente - API key não configurada")
            return True
        
        agent = MangabaAgent()
        print("✅ Agente criado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar agente: {e}")
        return False

def test_basic_chat():
    """Testa chat básico com contexto MCP"""
    try:
        from mangaba_ai import MangabaAgent
        
        if not os.getenv('API_KEY') or os.getenv('API_KEY') == "cole_sua_chave_aqui":
            print("⚠️  Pulando teste de chat - API key não configurada")
            return True
        
        agent = MangabaAgent()
        response = agent.chat("Olá!")
        
        if response and len(response) > 0:
            print(f"✅ Chat funcionando: {response[:50]}...")
            return True
        else:
            print("❌ Chat retornou resposta vazia")
            return False
    except Exception as e:
        print(f"❌ Erro no chat: {e}")
        return False

def test_analyze_text():
    """Testa análise de texto com contexto MCP"""
    try:
        from mangaba_ai import MangabaAgent
        
        if not os.getenv('API_KEY') or os.getenv('API_KEY') == "cole_sua_chave_aqui":
            print("⚠️  Pulando teste de análise - API key não configurada")
            return True
        
        agent = MangabaAgent()
        text = "Python é uma linguagem de programação versátil e poderosa."
        response = agent.analyze_text(text, "Resuma em uma frase")
        
        if response and len(response) > 0:
            print(f"✅ Análise de texto funcionando: {response[:50]}...")
            return True
        else:
            print("❌ Análise retornou resposta vazia")
            return False
    except Exception as e:
        print(f"❌ Erro na análise: {e}")
        return False

def test_translate():
    """Testa tradução com contexto MCP"""
    try:
        from mangaba_ai import MangabaAgent
        
        if not os.getenv('API_KEY') or os.getenv('API_KEY') == "cole_sua_chave_aqui":
            print("⚠️  Pulando teste de tradução - API key não configurada")
            return True
        
        agent = MangabaAgent()
        response = agent.translate("Hello world", "português")
        
        if response and len(response) > 0:
            print(f"✅ Tradução funcionando: {response[:50]}...")
            return True
        else:
            print("❌ Tradução retornou resposta vazia")
            return False
    except Exception as e:
        print(f"❌ Erro na tradução: {e}")
        return False

def main():
    """Executa todos os testes."""
    print("🧪 Executando testes básicos...\n")
    
    tests = [
        ("Imports", test_imports),
        ("Configuração", test_config),
        ("Criação do Agente", test_agent_creation),
        ("Chat Básico", test_basic_chat),
        ("Análise de Texto", test_analyze_text),
        ("Tradução", test_translate),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"🔍 Testando {test_name}...")
        result = test_func()
        results.append(result)
        print()
    
    # Resumo
    passed = sum(results)
    total = len(results)
    
    print("="*50)
    print(f"📊 Resumo: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! O projeto está pronto para uso.")
    else:
        print("⚠️  Alguns testes falharam. Verifique a configuração.")
    
    print("\n💡 Para usar o agente:")
    print("1. Configure sua API key no arquivo .env")
    print("2. Execute: python examples/basic_example.py")

if __name__ == "__main__":
    main()