#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo Prático do Curso Básico - Mangaba AI

Este arquivo demonstra os conceitos apresentados no CURSO_BASICO.md
com exemplos funcionais que você pode executar.

Pré-requisitos:
- Ambiente configurado (execute: python validate_env.py)
- API Key do Google configurada no .env

Para executar:
    python exemplo_curso_basico.py
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório atual ao path para imports
sys.path.append(str(Path(__file__).parent))

try:
    from mangaba_agent import MangabaAgent
    from protocols.mcp import MCPProtocol
    from protocols.a2a import A2AProtocol
    from config import config
except ImportError as e:
    print(f"[ERROR] Erro ao importar módulos: {e}")
    print("[INFO] Execute 'python validate_env.py' para verificar a configuração")
    sys.exit(1)

def separador(titulo):
    """Cria um separador visual para organizar a saída"""
    print("\n" + "="*60)
    print(f"  {titulo}")
    print("="*60)

def exemplo_1_basico():
    """Exemplo 1: Uso básico do agente"""
    separador("EXEMPLO 1: USO BÁSICO")
    
    try:
        # Criar agente
        agent = MangabaAgent()
        print("[OK] Agente criado com sucesso!")
        
        # Primeira conversa
        print("\n[INFO] Enviando primeira mensagem...")
        resposta = agent.chat("Olá! Explique em 2 frases o que é inteligência artificial.")
        print(f"\n[RESPOSTA] {resposta}")
        
        # Segunda conversa (mantém contexto)
        print("\n[INFO] Enviando segunda mensagem...")
        resposta = agent.chat("Dê um exemplo prático de uso de IA no dia a dia.")
        print(f"\n[RESPOSTA] {resposta}")
        
    except Exception as e:
        print(f"[ERROR] Erro no exemplo básico: {e}")
        return False
    
    return True

def exemplo_2_mcp():
    """Exemplo 2: Uso do protocolo MCP para gerenciar contexto"""
    separador("EXEMPLO 2: PROTOCOLO MCP (CONTEXTO)")
    
    try:
        # Criar agente com MCP
        agent = MangabaAgent()
        mcp = MCPProtocol()
        agent.add_protocol(mcp)
        print("[OK] Agente com protocolo MCP criado!")
        
        # Adicionar contexto sobre o usuário
        print("\n[INFO] Adicionando contexto do usuário...")
        mcp.add_context(
            content="O usuário é um desenvolvedor Python iniciante interessado em IA",
            context_type="user_profile",
            priority=1
        )
        
        # Adicionar contexto sobre projeto
        mcp.add_context(
            content="Projeto atual: Sistema de chatbot para atendimento ao cliente",
            context_type="project_info",
            priority=2
        )
        
        print(f"[OK] Contextos adicionados. Total: {len(mcp.contexts)}")
        
        # Chat usando contexto
        print("\n[INFO] Fazendo pergunta que usa o contexto...")
        resposta = agent.chat("Que bibliotecas Python você recomenda para meu projeto?")
        print(f"\n[RESPOSTA] {resposta}")
        
        # Mostrar contextos relevantes encontrados
        contextos_relevantes = mcp.get_relevant_contexts("bibliotecas Python chatbot")
        print(f"\n[INFO] Contextos relevantes encontrados: {len(contextos_relevantes)}")
        
    except Exception as e:
        print(f"[ERROR] Erro no exemplo MCP: {e}")
        return False
    
    return True

def exemplo_3_analise_texto():
    """Exemplo 3: Análise de texto prática"""
    separador("EXEMPLO 3: ANÁLISE DE TEXTO")
    
    try:
        agent = MangabaAgent()
        
        # Texto de exemplo para análise
        texto_exemplo = """
        A inteligência artificial está transformando rapidamente diversos setores da economia.
        Empresas estão investindo bilhões em tecnologias de machine learning e deep learning.
        No entanto, existem preocupações sobre o impacto no mercado de trabalho e questões éticas.
        É fundamental que o desenvolvimento da IA seja feito de forma responsável e inclusiva.
        """
        
        print("[INFO] Analisando texto de exemplo...")
        print(f"\n[TEXTO] {texto_exemplo.strip()}")
        
        # Solicitar análise
        prompt_analise = f"""
        Analise o seguinte texto e forneça:
        1. Tema principal (1 linha)
        2. Pontos positivos mencionados (máximo 2)
        3. Preocupações levantadas (máximo 2)
        4. Tom do texto (objetivo/otimista/pessimista/neutro)
        
        Texto: {texto_exemplo}
        
        Formato da resposta:
        TEMA: [tema]
        POSITIVOS: [pontos]
        PREOCUPAÇÕES: [preocupações]
        TOM: [tom]
        """
        
        resposta = agent.chat(prompt_analise)
        print(f"\n[ANÁLISE]\n{resposta}")
        
    except Exception as e:
        print(f"[ERROR] Erro na análise de texto: {e}")
        return False
    
    return True

def exemplo_4_configuracoes():
    """Exemplo 4: Demonstrar configurações do sistema"""
    separador("EXEMPLO 4: CONFIGURAÇÕES DO SISTEMA")
    
    try:
        print("[INFO] Configurações atuais do Mangaba AI:")
        print(f"  - Modelo: {config.model}")
        print(f"  - Log Level: {config.log_level}")
        print(f"  - API Key configurada: {'Sim' if config.api_key else 'Não'}")
        
        # Mostrar variáveis de ambiente relevantes
        env_vars = {
            'GOOGLE_API_KEY': 'Configurada' if os.getenv('GOOGLE_API_KEY') else 'Não configurada',
            'MODEL_NAME': os.getenv('MODEL_NAME', 'Padrão (gemini-pro)'),
            'LOG_LEVEL': os.getenv('LOG_LEVEL', 'Padrão (INFO)'),
            'USE_MCP': os.getenv('USE_MCP', 'Padrão (true)'),
            'USE_A2A': os.getenv('USE_A2A', 'Padrão (true)')
        }
        
        print("\n[INFO] Variáveis de ambiente:")
        for var, valor in env_vars.items():
            print(f"  - {var}: {valor}")
        
    except Exception as e:
        print(f"[ERROR] Erro ao mostrar configurações: {e}")
        return False
    
    return True

def main():
    """Função principal que executa todos os exemplos"""
    print("🎓 CURSO BÁSICO - MANGABA AI - EXEMPLOS PRÁTICOS")
    print("Este script demonstra os conceitos do curso básico na prática.")
    print("\n[INFO] Verificando configuração...")
    
    # Verificar se a configuração está OK
    try:
        config_test = config
        print("[OK] Configuração carregada com sucesso!")
    except Exception as e:
        print(f"[ERROR] Problema na configuração: {e}")
        print("[INFO] Execute 'python validate_env.py' para diagnosticar")
        return
    
    # Lista de exemplos para executar
    exemplos = [
        ("Uso Básico", exemplo_1_basico),
        ("Protocolo MCP", exemplo_2_mcp),
        ("Análise de Texto", exemplo_3_analise_texto),
        ("Configurações", exemplo_4_configuracoes)
    ]
    
    resultados = []
    
    # Executar cada exemplo
    for nome, funcao in exemplos:
        try:
            print(f"\n[INFO] Executando: {nome}...")
            sucesso = funcao()
            resultados.append((nome, sucesso))
            
            if sucesso:
                print(f"[OK] {nome} executado com sucesso!")
            else:
                print(f"[ERROR] {nome} falhou!")
                
        except KeyboardInterrupt:
            print("\n[INFO] Execução interrompida pelo usuário.")
            break
        except Exception as e:
            print(f"[ERROR] Erro inesperado em {nome}: {e}")
            resultados.append((nome, False))
    
    # Resumo final
    separador("RESUMO DOS EXEMPLOS")
    sucessos = sum(1 for _, sucesso in resultados if sucesso)
    total = len(resultados)
    
    print(f"Exemplos executados: {total}")
    print(f"Sucessos: {sucessos}")
    print(f"Falhas: {total - sucessos}")
    
    if sucessos == total:
        print("\n🎉 [SUCCESS] Todos os exemplos foram executados com sucesso!")
        print("\n📚 Próximos passos:")
        print("  1. Leia o CURSO_BASICO.md para entender os conceitos")
        print("  2. Explore os exemplos na pasta examples/")
        print("  3. Experimente criar seus próprios agentes")
        print("  4. Consulte PROTOCOLS.md para funcionalidades avançadas")
    else:
        print("\n⚠️ [WARN] Alguns exemplos falharam.")
        print("\n🔧 Soluções:")
        print("  1. Execute: python validate_env.py")
        print("  2. Verifique se a GOOGLE_API_KEY está configurada")
        print("  3. Consulte SETUP.md para configuração detalhada")
    
    print("\n[INFO] Obrigado por usar o Mangaba AI! 🤖")

if __name__ == "__main__":
    main()