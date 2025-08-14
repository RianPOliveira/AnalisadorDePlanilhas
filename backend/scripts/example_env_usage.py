#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso das configurações do arquivo .env

Este script demonstra como as variáveis de ambiente são utilizadas
no projeto Mangaba AI.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict, Any
import json


def load_environment_config() -> Dict[str, Any]:
    """
    Carrega e valida configurações do ambiente
    
    Returns:
        Dict com todas as configurações carregadas
    """
    # Carrega arquivo .env se existir
    env_file = Path('.env')
    if env_file.exists():
        load_dotenv(env_file)
        print(f"✅ Arquivo .env carregado: {env_file.absolute()}")
    else:
        print("⚠️ Arquivo .env não encontrado, usando variáveis do sistema")
    
    # Configurações obrigatórias
    required_config = {
        'google_api_key': os.getenv('GOOGLE_API_KEY'),
    }
    
    # Configurações opcionais com valores padrão
    optional_config = {
        # Configurações do modelo
        'model_name': os.getenv('MODEL_NAME', 'gemini-pro'),
        'model_temperature': float(os.getenv('MODEL_TEMPERATURE', '0.7')),
        'model_max_tokens': int(os.getenv('MODEL_MAX_TOKENS', '2048')),
        
        # Configurações do agente
        'agent_name': os.getenv('AGENT_NAME', 'MangabaAgent'),
        'agent_id': os.getenv('AGENT_ID', 'mangaba-001'),
        'agent_description': os.getenv('AGENT_DESCRIPTION', 'Agente de IA versátil'),
        
        # Configurações de protocolo
        'use_mcp': os.getenv('USE_MCP', 'true').lower() == 'true',
        'use_a2a': os.getenv('USE_A2A', 'true').lower() == 'true',
        'mcp_max_contexts': int(os.getenv('MCP_MAX_CONTEXTS', '100')),
        'mcp_context_ttl': int(os.getenv('MCP_CONTEXT_TTL', '3600')),
        'a2a_port': int(os.getenv('A2A_PORT', '8080')),
        'a2a_host': os.getenv('A2A_HOST', 'localhost'),
        
        # Configurações de logging
        'log_level': os.getenv('LOG_LEVEL', 'INFO'),
        'log_file': os.getenv('LOG_FILE', 'mangaba.log'),
        'log_format': os.getenv('LOG_FORMAT', 'detailed'),
        
        # Configurações de performance
        'max_concurrent_requests': int(os.getenv('MAX_CONCURRENT_REQUESTS', '10')),
        'request_timeout': int(os.getenv('REQUEST_TIMEOUT', '30')),
        'retry_attempts': int(os.getenv('RETRY_ATTEMPTS', '3')),
        'retry_delay': float(os.getenv('RETRY_DELAY', '1.0')),
        
        # Configurações de segurança
        'enable_rate_limiting': os.getenv('ENABLE_RATE_LIMITING', 'true').lower() == 'true',
        'rate_limit_requests': int(os.getenv('RATE_LIMIT_REQUESTS', '100')),
        'rate_limit_window': int(os.getenv('RATE_LIMIT_WINDOW', '3600')),
        'enable_input_validation': os.getenv('ENABLE_INPUT_VALIDATION', 'true').lower() == 'true',
        
        # Configurações de cache
        'enable_cache': os.getenv('ENABLE_CACHE', 'true').lower() == 'true',
        'cache_type': os.getenv('CACHE_TYPE', 'memory'),
        'cache_ttl': int(os.getenv('CACHE_TTL', '1800')),
        'cache_max_size': int(os.getenv('CACHE_MAX_SIZE', '1000')),
        
        # Configurações de desenvolvimento
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'debug_mode': os.getenv('DEBUG_MODE', 'false').lower() == 'true',
        'enable_metrics': os.getenv('ENABLE_METRICS', 'false').lower() == 'true',
        'metrics_port': int(os.getenv('METRICS_PORT', '9090')),
        
        # Configurações de rede
        'proxy_url': os.getenv('PROXY_URL'),
        'user_agent': os.getenv('USER_AGENT', 'MangabaAI/1.0'),
        'connection_pool_size': int(os.getenv('CONNECTION_POOL_SIZE', '10')),
    }
    
    # Combina configurações
    config = {**required_config, **optional_config}
    
    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Valida configurações carregadas
    
    Args:
        config: Dicionário de configurações
        
    Returns:
        True se válido, False caso contrário
    """
    errors = []
    warnings = []
    
    # Validações obrigatórias
    if not config.get('google_api_key'):
        errors.append("GOOGLE_API_KEY é obrigatória")
    elif config['google_api_key'] == 'your_google_api_key_here':
        errors.append("GOOGLE_API_KEY não foi configurada (ainda é o valor padrão)")
    
    # Validações de valores
    if config.get('model_temperature', 0) < 0 or config.get('model_temperature', 0) > 2:
        warnings.append("MODEL_TEMPERATURE deve estar entre 0 e 2")
    
    if config.get('model_max_tokens', 0) <= 0:
        warnings.append("MODEL_MAX_TOKENS deve ser maior que 0")
    
    if config.get('mcp_max_contexts', 0) <= 0:
        warnings.append("MCP_MAX_CONTEXTS deve ser maior que 0")
    
    if config.get('a2a_port', 0) < 1024 or config.get('a2a_port', 0) > 65535:
        warnings.append("A2A_PORT deve estar entre 1024 e 65535")
    
    # Validações de ambiente
    valid_environments = ['development', 'testing', 'staging', 'production']
    if config.get('environment') not in valid_environments:
        warnings.append(f"ENVIRONMENT deve ser um de: {', '.join(valid_environments)}")
    
    valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    if config.get('log_level') not in valid_log_levels:
        warnings.append(f"LOG_LEVEL deve ser um de: {', '.join(valid_log_levels)}")
    
    valid_cache_types = ['memory', 'redis', 'file']
    if config.get('cache_type') not in valid_cache_types:
        warnings.append(f"CACHE_TYPE deve ser um de: {', '.join(valid_cache_types)}")
    
    # Mostra resultados
    if errors:
        print("\n❌ Erros de configuração:")
        for error in errors:
            print(f"   • {error}")
    
    if warnings:
        print("\n⚠️ Avisos de configuração:")
        for warning in warnings:
            print(f"   • {warning}")
    
    if not errors and not warnings:
        print("\n✅ Todas as configurações são válidas!")
    
    return len(errors) == 0


def print_config_summary(config: Dict[str, Any]):
    """
    Imprime resumo das configurações
    
    Args:
        config: Dicionário de configurações
    """
    print("\n📋 Resumo das Configurações:")
    print("=" * 50)
    
    # Agrupa configurações por categoria
    categories = {
        '🤖 Modelo': {
            'Nome': config.get('model_name'),
            'Temperatura': config.get('model_temperature'),
            'Max Tokens': config.get('model_max_tokens'),
        },
        '👤 Agente': {
            'Nome': config.get('agent_name'),
            'ID': config.get('agent_id'),
            'Descrição': config.get('agent_description'),
        },
        '🔗 Protocolos': {
            'MCP Habilitado': config.get('use_mcp'),
            'A2A Habilitado': config.get('use_a2a'),
            'Max Contextos MCP': config.get('mcp_max_contexts'),
            'Porta A2A': config.get('a2a_port'),
        },
        '📊 Logging': {
            'Nível': config.get('log_level'),
            'Arquivo': config.get('log_file'),
            'Formato': config.get('log_format'),
        },
        '⚡ Performance': {
            'Max Requisições': config.get('max_concurrent_requests'),
            'Timeout': f"{config.get('request_timeout')}s",
            'Tentativas': config.get('retry_attempts'),
        },
        '🔒 Segurança': {
            'Rate Limiting': config.get('enable_rate_limiting'),
            'Validação Input': config.get('enable_input_validation'),
            'Limite Requisições': config.get('rate_limit_requests'),
        },
        '💾 Cache': {
            'Habilitado': config.get('enable_cache'),
            'Tipo': config.get('cache_type'),
            'TTL': f"{config.get('cache_ttl')}s",
            'Max Size': config.get('cache_max_size'),
        },
        '🛠️ Desenvolvimento': {
            'Ambiente': config.get('environment'),
            'Debug': config.get('debug_mode'),
            'Métricas': config.get('enable_metrics'),
        }
    }
    
    for category, settings in categories.items():
        print(f"\n{category}")
        for key, value in settings.items():
            # Mascarar API keys
            if 'key' in key.lower() and value:
                display_value = f"{value[:8]}..."
            else:
                display_value = value
            print(f"  {key}: {display_value}")


def demonstrate_usage():
    """
    Demonstra como usar as configurações no código
    """
    print("\n🎯 Exemplo de Uso no Código:")
    print("=" * 50)
    
    example_code = '''
# Exemplo de como usar as configurações
from mangaba_agent import MangabaAgent
from protocols.mcp import MCPProtocol
from protocols.a2a import A2AProtocol

# Carrega configurações
config = load_environment_config()

# Inicializa agente com configurações
agent = MangabaAgent(
    api_key=config['google_api_key'],
    model_name=config['model_name'],
    agent_name=config['agent_name'],
    temperature=config['model_temperature'],
    max_tokens=config['model_max_tokens']
)

# Configura protocolos se habilitados
if config['use_mcp']:
    mcp = MCPProtocol(
        max_contexts=config['mcp_max_contexts'],
        context_ttl=config['mcp_context_ttl']
    )
    agent.add_protocol(mcp)

if config['use_a2a']:
    a2a = A2AProtocol(
        host=config['a2a_host'],
        port=config['a2a_port']
    )
    agent.add_protocol(a2a)

# Usa o agente
response = agent.chat("Olá!")
print(response)
'''
    
    print(example_code)


def save_config_template():
    """
    Salva template de configuração em JSON
    """
    template = {
        "description": "Template de configuração para Mangaba AI",
        "required": {
            "GOOGLE_API_KEY": {
                "description": "Chave da API do Google Generative AI",
                "type": "string",
                "example": "AIza...",
                "required": True
            }
        },
        "optional": {
            "MODEL_NAME": {
                "description": "Nome do modelo a ser usado",
                "type": "string",
                "default": "gemini-pro",
                "options": ["gemini-pro", "gemini-pro-vision"]
            },
            "MODEL_TEMPERATURE": {
                "description": "Temperatura do modelo (criatividade)",
                "type": "float",
                "default": 0.7,
                "range": [0.0, 2.0]
            },
            "AGENT_NAME": {
                "description": "Nome do agente",
                "type": "string",
                "default": "MangabaAgent"
            },
            "LOG_LEVEL": {
                "description": "Nível de logging",
                "type": "string",
                "default": "INFO",
                "options": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
            },
            "ENVIRONMENT": {
                "description": "Ambiente de execução",
                "type": "string",
                "default": "development",
                "options": ["development", "testing", "staging", "production"]
            }
        }
    }
    
    with open('config_template.json', 'w', encoding='utf-8') as f:
        json.dump(template, f, indent=2, ensure_ascii=False)
    
    print("\n💾 Template salvo em: config_template.json")


def main():
    """
    Função principal
    """
    print("🥭 Mangaba AI - Exemplo de Uso das Configurações")
    print("=" * 60)
    
    try:
        # Carrega configurações
        print("\n🔄 Carregando configurações...")
        config = load_environment_config()
        
        # Valida configurações
        print("\n🔍 Validando configurações...")
        is_valid = validate_config(config)
        
        # Mostra resumo
        print_config_summary(config)
        
        # Demonstra uso
        demonstrate_usage()
        
        # Salva template
        save_config_template()
        
        # Status final
        if is_valid:
            print("\n✅ Configurações válidas! Pronto para usar.")
        else:
            print("\n❌ Problemas encontrados. Corrija antes de usar.")
            
        print("\n📚 Para mais informações:")
        print("   - .env.template (exemplo completo)")
        print("   - SETUP.md (guia de configuração)")
        print("   - validate_env.py (validação completa)")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())