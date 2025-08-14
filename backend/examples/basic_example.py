#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo básico do agente Mangaba com protocolos A2A e MCP - super simples!
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangaba_agent import MangabaAgent
import time

def main():
    # Cria o agente com protocolos habilitados
    agent = MangabaAgent()
    
    print("🤖 Mangaba Agent iniciado com protocolos A2A e MCP!")
    print("Comandos especiais:")
    print("  /analyze <texto> - Analisa texto")
    print("  /translate <texto> - Traduz texto")
    print("  /context - Mostra resumo do contexto")
    print("  /broadcast <mensagem> - Envia broadcast")
    print("  /request <agent_id> <action> - Envia requisição para outro agente")
    print("  /help - Mostra esta ajuda")
    print("  /sair - Encerra o programa\n")
    
    while True:
        try:
            # Pega input do usuário
            user_input = input("Você: ").strip()
            
            if user_input.lower() in ['/sair', 'sair', 'exit', 'quit']:
                print("👋 Tchau!")
                break
            
            if not user_input:
                continue
            
            # Processa comandos especiais
            if user_input.startswith('/'):
                response = process_special_command(agent, user_input)
            else:
                # Chat normal com contexto MCP
                response = agent.chat(user_input)
            
            print(f"🤖 Mangaba: {response}\n")
            
        except KeyboardInterrupt:
            print("\n👋 Tchau!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}\n")

def process_special_command(agent: MangabaAgent, command: str) -> str:
    """Processa comandos especiais do usuário"""
    parts = command[1:].split(' ', 2)  # Remove '/' e divide
    cmd = parts[0].lower()
    
    if cmd == 'help':
        return """Comandos disponíveis:
/analyze <texto> - Analisa o texto fornecido
/translate <texto> - Traduz o texto para português
/context - Mostra resumo do contexto atual
/broadcast <mensagem> - Envia broadcast para outros agentes
/request <agent_id> <action> - Envia requisição para outro agente
/help - Mostra esta ajuda
/sair - Encerra o programa"""
    
    elif cmd == 'analyze':
        if len(parts) < 2:
            return "Uso: /analyze <texto a ser analisado>"
        text = ' '.join(parts[1:])
        return agent.analyze_text(text, "Faça uma análise detalhada deste texto")
    
    elif cmd == 'translate':
        if len(parts) < 2:
            return "Uso: /translate <texto a ser traduzido>"
        text = ' '.join(parts[1:])
        return agent.translate(text, "inglês")
    
    elif cmd == 'context':
        return agent.get_context_summary()
    
    elif cmd == 'broadcast':
        if len(parts) < 2:
            return "Uso: /broadcast <mensagem>"
        message = ' '.join(parts[1:])
        return agent.broadcast_message(message, ["example", "demo"])
    
    elif cmd == 'request':
        if len(parts) < 3:
            return "Uso: /request <agent_id> <action> [params]"
        agent_id = parts[1]
        action = parts[2]
        params = {"message": "Olá do exemplo básico!"} if action == "chat" else {}
        return agent.send_agent_request(agent_id, action, params)
    
    else:
        return f"Comando '{cmd}' não reconhecido. Digite /help para ver comandos disponíveis."

def demo_protocols():
    """Demonstração avançada dos protocolos A2A e MCP"""
    print("\n🚀 Demonstração dos Protocolos A2A e MCP\n")
    
    # Cria dois agentes para demonstrar comunicação A2A
    agent1 = MangabaAgent()
    agent2 = MangabaAgent()
    
    print(f"Agent 1 ID: {agent1.agent_id}")
    print(f"Agent 2 ID: {agent2.agent_id}")
    
    # Demonstra chat com contexto
    print("\n--- Chat com Contexto MCP ---")
    response1 = agent1.chat("Olá, meu nome é João")
    print(f"Agent 1: {response1}")
    
    response2 = agent1.chat("Qual é o meu nome?")
    print(f"Agent 1: {response2}")
    
    # Demonstra análise de texto
    print("\n--- Análise de Texto ---")
    text_to_analyze = "A inteligência artificial está revolucionando o mundo."
    analysis = agent1.analyze_text(text_to_analyze)
    print(f"Análise: {analysis[:100]}...")
    
    # Demonstra tradução
    print("\n--- Tradução ---")
    translation = agent1.translate("Hello, how are you?", "português")
    print(f"Tradução: {translation}")
    
    # Demonstra resumo do contexto
    print("\n--- Resumo do Contexto ---")
    context_summary = agent1.get_context_summary()
    print(f"Contexto: {context_summary}")
    
    # Demonstra comunicação A2A
    print("\n--- Comunicação A2A ---")
    broadcast_result = agent1.broadcast_message("Olá a todos os agentes!")
    print(f"Broadcast: {broadcast_result}")
    
    request_result = agent1.send_agent_request(agent2.agent_id, "chat", {"message": "Como você está?"})
    print(f"Requisição: {request_result}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_protocols()
    else:
        main()