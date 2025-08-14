#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Integração com APIs Externas usando Mangaba Agent
Demonstra integração com diferentes tipos de APIs e serviços web
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangaba_agent import MangabaAgent
from protocols.mcp import ContextType, ContextPriority
import json
import time
from datetime import datetime
import random

class APIConnector:
    """Simulador de conexões com APIs externas"""
    
    def __init__(self, api_name, base_url):
        self.api_name = api_name
        self.base_url = base_url
        self.agent = MangabaAgent(agent_id=f"api_connector_{api_name.lower()}")
        self.request_count = 0
        self.cache = {}
    
    def make_request(self, endpoint, method="GET", data=None):
        """Simula requisição para API externa"""
        self.request_count += 1
        
        # Simula resposta baseada no tipo de API
        if self.api_name == "weather":
            return self._simulate_weather_response(endpoint)
        elif self.api_name == "finance":
            return self._simulate_finance_response(endpoint)
        elif self.api_name == "social":
            return self._simulate_social_response(endpoint)
        elif self.api_name == "ecommerce":
            return self._simulate_ecommerce_response(endpoint, data)
        else:
            return {"status": "success", "data": "Generic API response"}
    
    def _simulate_weather_response(self, endpoint):
        """Simula resposta da API de clima"""
        if "current" in endpoint:
            return {
                "status": "success",
                "data": {
                    "location": "São Paulo, SP",
                    "temperature": random.randint(18, 32),
                    "humidity": random.randint(40, 80),
                    "condition": random.choice(["sunny", "cloudy", "rainy"]),
                    "wind_speed": random.randint(5, 25),
                    "timestamp": datetime.now().isoformat()
                }
            }
        elif "forecast" in endpoint:
            return {
                "status": "success",
                "data": {
                    "location": "São Paulo, SP",
                    "forecast": [
                        {
                            "date": "2024-01-01",
                            "temp_max": random.randint(25, 35),
                            "temp_min": random.randint(15, 25),
                            "condition": random.choice(["sunny", "cloudy", "rainy"])
                        } for _ in range(7)
                    ]
                }
            }
    
    def _simulate_finance_response(self, endpoint):
        """Simula resposta da API financeira"""
        if "stocks" in endpoint:
            return {
                "status": "success",
                "data": {
                    "symbol": "AAPL",
                    "price": round(random.uniform(150, 200), 2),
                    "change": round(random.uniform(-5, 5), 2),
                    "volume": random.randint(1000000, 10000000),
                    "market_cap": "2.8T",
                    "timestamp": datetime.now().isoformat()
                }
            }
        elif "crypto" in endpoint:
            return {
                "status": "success",
                "data": {
                    "symbol": "BTC",
                    "price": round(random.uniform(40000, 60000), 2),
                    "change_24h": round(random.uniform(-10, 10), 2),
                    "market_cap": "800B",
                    "timestamp": datetime.now().isoformat()
                }
            }
    
    def _simulate_social_response(self, endpoint):
        """Simula resposta da API de redes sociais"""
        if "posts" in endpoint:
            return {
                "status": "success",
                "data": {
                    "posts": [
                        {
                            "id": f"post_{i}",
                            "content": f"Post de exemplo {i}",
                            "likes": random.randint(10, 1000),
                            "shares": random.randint(1, 100),
                            "comments": random.randint(0, 50),
                            "timestamp": datetime.now().isoformat()
                        } for i in range(5)
                    ]
                }
            }
        elif "analytics" in endpoint:
            return {
                "status": "success",
                "data": {
                    "followers": random.randint(1000, 100000),
                    "engagement_rate": round(random.uniform(2, 8), 2),
                    "reach": random.randint(5000, 500000),
                    "impressions": random.randint(10000, 1000000)
                }
            }
    
    def _simulate_ecommerce_response(self, endpoint, data):
        """Simula resposta da API de e-commerce"""
        if "products" in endpoint:
            return {
                "status": "success",
                "data": {
                    "products": [
                        {
                            "id": f"prod_{i}",
                            "name": f"Produto {i}",
                            "price": round(random.uniform(10, 500), 2),
                            "stock": random.randint(0, 100),
                            "category": random.choice(["electronics", "clothing", "books"])
                        } for i in range(10)
                    ]
                }
            }
        elif "orders" in endpoint and data:
            return {
                "status": "success",
                "data": {
                    "order_id": f"ORD{random.randint(10000, 99999)}",
                    "status": "created",
                    "total": data.get("total", 0),
                    "estimated_delivery": "3-5 business days"
                }
            }
    
    def analyze_response(self, response, context=""):
        """Analisa resposta da API usando o agente"""
        analysis_prompt = f"""
        Analise a seguinte resposta da API {self.api_name}:
        
        Contexto: {context}
        Resposta: {json.dumps(response, indent=2)}
        
        Forneça:
        1. Resumo dos dados recebidos
        2. Insights principais
        3. Qualidade dos dados
        4. Ações recomendadas
        5. Possíveis problemas
        """
        
        analysis = self.agent.chat(analysis_prompt, use_context=True)
        return analysis
    
    def get_stats(self):
        """Retorna estatísticas de uso da API"""
        return {
            "api_name": self.api_name,
            "requests_made": self.request_count,
            "cache_size": len(self.cache)
        }

def demo_weather_integration():
    """Demonstra integração com API de clima"""
    print("🌤️ Integração com API de Clima")
    print("=" * 40)
    
    weather_api = APIConnector("weather", "https://api.weather.com")
    
    # Busca clima atual
    print("📡 Buscando clima atual...")
    current_weather = weather_api.make_request("/current/saopaulo")
    
    # Analisa dados do clima
    weather_analysis = weather_api.analyze_response(
        current_weather,
        "Dados de clima atual para São Paulo"
    )
    print(f"🌡️ Análise do Clima: {weather_analysis}")
    
    # Busca previsão
    print("\n📅 Buscando previsão do tempo...")
    forecast = weather_api.make_request("/forecast/saopaulo")
    
    # Analisa previsão
    forecast_analysis = weather_api.analyze_response(
        forecast,
        "Previsão do tempo para os próximos 7 dias"
    )
    print(f"📊 Análise da Previsão: {forecast_analysis}")
    
    return {
        "current_weather": current_weather,
        "forecast": forecast,
        "api_stats": weather_api.get_stats()
    }

def demo_financial_integration():
    """Demonstra integração com APIs financeiras"""
    print("\n💹 Integração com APIs Financeiras")
    print("=" * 40)
    
    finance_api = APIConnector("finance", "https://api.finance.com")
    
    # Busca dados de ações
    print("📈 Buscando dados de ações...")
    stock_data = finance_api.make_request("/stocks/AAPL")
    
    # Analisa dados de ações
    stock_analysis = finance_api.analyze_response(
        stock_data,
        "Dados de ações da Apple (AAPL)"
    )
    print(f"📊 Análise de Ações: {stock_analysis}")
    
    # Busca dados de criptomoedas
    print("\n₿ Buscando dados de criptomoedas...")
    crypto_data = finance_api.make_request("/crypto/BTC")
    
    # Analisa dados de crypto
    crypto_analysis = finance_api.analyze_response(
        crypto_data,
        "Dados de Bitcoin (BTC)"
    )
    print(f"💰 Análise de Crypto: {crypto_analysis}")
    
    # Comparação de investimentos
    comparison_prompt = f"""
    Compare os seguintes investimentos:
    
    Ações (AAPL): {json.dumps(stock_data['data'], indent=2)}
    Crypto (BTC): {json.dumps(crypto_data['data'], indent=2)}
    
    Forneça:
    1. Análise de risco/retorno
    2. Volatilidade comparativa
    3. Recomendações de portfólio
    4. Tendências de mercado
    """
    
    comparison = finance_api.agent.chat(comparison_prompt, use_context=True)
    print(f"\n⚖️ Comparação de Investimentos: {comparison}")
    
    return {
        "stock_data": stock_data,
        "crypto_data": crypto_data,
        "comparison": comparison,
        "api_stats": finance_api.get_stats()
    }

def demo_social_media_integration():
    """Demonstra integração com APIs de redes sociais"""
    print("\n📱 Integração com Redes Sociais")
    print("=" * 40)
    
    social_api = APIConnector("social", "https://api.social.com")
    
    # Busca posts recentes
    print("📝 Buscando posts recentes...")
    posts_data = social_api.make_request("/posts/recent")
    
    # Analisa engajamento dos posts
    posts_analysis = social_api.analyze_response(
        posts_data,
        "Posts recentes da conta"
    )
    print(f"📊 Análise de Posts: {posts_analysis}")
    
    # Busca analytics
    print("\n📈 Buscando analytics...")
    analytics_data = social_api.make_request("/analytics/overview")
    
    # Analisa métricas
    analytics_analysis = social_api.analyze_response(
        analytics_data,
        "Métricas gerais da conta"
    )
    print(f"📊 Análise de Analytics: {analytics_analysis}")
    
    # Estratégia de conteúdo
    strategy_prompt = f"""
    Com base nos dados de posts e analytics:
    
    Posts: {json.dumps(posts_data['data'], indent=2)}
    Analytics: {json.dumps(analytics_data['data'], indent=2)}
    
    Desenvolva uma estratégia de conteúdo:
    1. Tipos de conteúdo mais eficazes
    2. Horários ideais para posting
    3. Estratégias de engajamento
    4. Metas de crescimento
    5. KPIs a acompanhar
    """
    
    strategy = social_api.agent.chat(strategy_prompt, use_context=True)
    print(f"\n🎯 Estratégia de Conteúdo: {strategy}")
    
    return {
        "posts_data": posts_data,
        "analytics_data": analytics_data,
        "strategy": strategy,
        "api_stats": social_api.get_stats()
    }

def demo_ecommerce_integration():
    """Demonstra integração com APIs de e-commerce"""
    print("\n🛒 Integração com E-commerce")
    print("=" * 40)
    
    ecommerce_api = APIConnector("ecommerce", "https://api.ecommerce.com")
    
    # Busca produtos
    print("🛍️ Buscando catálogo de produtos...")
    products_data = ecommerce_api.make_request("/products/catalog")
    
    # Analisa catálogo
    catalog_analysis = ecommerce_api.analyze_response(
        products_data,
        "Catálogo completo de produtos"
    )
    print(f"📦 Análise do Catálogo: {catalog_analysis}")
    
    # Simula criação de pedido
    print("\n🛒 Criando pedido de teste...")
    order_data = {
        "customer_id": "CUST123",
        "items": [
            {"product_id": "prod_1", "quantity": 2},
            {"product_id": "prod_3", "quantity": 1}
        ],
        "total": 150.00
    }
    
    order_response = ecommerce_api.make_request("/orders/create", "POST", order_data)
    
    # Analisa processo de pedido
    order_analysis = ecommerce_api.analyze_response(
        order_response,
        "Criação de novo pedido"
    )
    print(f"📋 Análise do Pedido: {order_analysis}")
    
    # Otimização de vendas
    optimization_prompt = f"""
    Com base nos dados do catálogo e processo de pedidos:
    
    Produtos: {json.dumps(products_data['data'], indent=2)}
    Pedido: {json.dumps(order_response['data'], indent=2)}
    
    Sugira otimizações para:
    1. Gestão de estoque
    2. Precificação dinâmica
    3. Recomendações de produtos
    4. Processo de checkout
    5. Estratégias de upsell/cross-sell
    """
    
    optimization = ecommerce_api.agent.chat(optimization_prompt, use_context=True)
    print(f"\n🚀 Otimizações Sugeridas: {optimization}")
    
    return {
        "products_data": products_data,
        "order_response": order_response,
        "optimization": optimization,
        "api_stats": ecommerce_api.get_stats()
    }

def demo_multi_api_orchestration():
    """Demonstra orquestração de múltiplas APIs"""
    print("\n🔄 Orquestração de Múltiplas APIs")
    print("=" * 40)
    
    # Cria coordenador
    coordinator = MangabaAgent(agent_id="api_orchestrator")
    
    # Cria conectores para diferentes APIs
    weather_api = APIConnector("weather", "https://api.weather.com")
    finance_api = APIConnector("finance", "https://api.finance.com")
    social_api = APIConnector("social", "https://api.social.com")
    
    print("🌐 Coletando dados de múltiplas fontes...")
    
    # Coleta dados de todas as APIs
    weather_data = weather_api.make_request("/current/saopaulo")
    finance_data = finance_api.make_request("/stocks/AAPL")
    social_data = social_api.make_request("/analytics/overview")
    
    # Coordenador analisa dados integrados
    integration_prompt = f"""
    Analise os dados integrados de múltiplas APIs:
    
    Clima: {json.dumps(weather_data['data'], indent=2)}
    Finanças: {json.dumps(finance_data['data'], indent=2)}
    Social: {json.dumps(social_data['data'], indent=2)}
    
    Identifique:
    1. Correlações entre os dados
    2. Insights cross-platform
    3. Oportunidades de negócio
    4. Padrões emergentes
    5. Estratégias integradas
    """
    
    integration_analysis = coordinator.chat(integration_prompt, use_context=True)
    print(f"🔗 Análise Integrada: {integration_analysis}")
    
    # Dashboard executivo
    dashboard_prompt = """
    Crie um dashboard executivo com os dados integrados:
    
    Inclua:
    1. KPIs principais de cada fonte
    2. Alertas e notificações
    3. Tendências identificadas
    4. Recomendações de ação
    5. Próximos passos estratégicos
    
    Formato: Resumo executivo conciso
    """
    
    dashboard = coordinator.chat(dashboard_prompt, use_context=True)
    print(f"\n📊 Dashboard Executivo: {dashboard}")
    
    # Estatísticas de orquestração
    orchestration_stats = {
        "apis_integrated": 3,
        "total_requests": (
            weather_api.get_stats()['requests_made'] +
            finance_api.get_stats()['requests_made'] +
            social_api.get_stats()['requests_made']
        ),
        "data_sources": ["weather", "finance", "social"],
        "integration_points": 5
    }
    
    return {
        "integration_analysis": integration_analysis,
        "dashboard": dashboard,
        "orchestration_stats": orchestration_stats
    }

def demo_api_monitoring_and_alerts():
    """Demonstra monitoramento e alertas de APIs"""
    print("\n🚨 Monitoramento e Alertas de APIs")
    print("=" * 40)
    
    monitor = MangabaAgent(agent_id="api_monitor")
    
    # Simula dados de monitoramento
    api_health_data = {
        "weather_api": {
            "status": "healthy",
            "response_time": 120,  # ms
            "success_rate": 99.5,  # %
            "last_error": None
        },
        "finance_api": {
            "status": "degraded",
            "response_time": 850,  # ms
            "success_rate": 95.2,  # %
            "last_error": "Rate limit exceeded"
        },
        "social_api": {
            "status": "down",
            "response_time": 0,  # ms
            "success_rate": 0,  # %
            "last_error": "Connection timeout"
        }
    }
    
    print("📊 Analisando saúde das APIs...")
    
    # Análise de saúde
    health_analysis_prompt = f"""
    Analise a saúde das seguintes APIs:
    
    {json.dumps(api_health_data, indent=2)}
    
    Para cada API, avalie:
    1. Status atual
    2. Performance
    3. Confiabilidade
    4. Impacto nos negócios
    5. Ações corretivas necessárias
    """
    
    health_analysis = monitor.chat(health_analysis_prompt, use_context=True)
    print(f"🏥 Análise de Saúde: {health_analysis}")
    
    # Geração de alertas
    alerts_prompt = """
    Com base na análise de saúde, gere alertas apropriados:
    
    Crie alertas para:
    1. APIs com problemas críticos
    2. Degradação de performance
    3. Falhas de conectividade
    4. Limites de rate sendo atingidos
    5. Impactos nos usuários finais
    
    Inclua severidade e ações recomendadas.
    """
    
    alerts = monitor.chat(alerts_prompt, use_context=True)
    print(f"\n🚨 Alertas Gerados: {alerts}")
    
    # Plano de recuperação
    recovery_prompt = """
    Desenvolva um plano de recuperação para as APIs com problemas:
    
    Inclua:
    1. Priorização por impacto
    2. Passos de troubleshooting
    3. Alternativas e fallbacks
    4. Comunicação com stakeholders
    5. Prevenção de problemas futuros
    """
    
    recovery_plan = monitor.chat(recovery_prompt, use_context=True)
    print(f"\n🔧 Plano de Recuperação: {recovery_plan}")
    
    return {
        "health_analysis": health_analysis,
        "alerts": alerts,
        "recovery_plan": recovery_plan,
        "apis_monitored": len(api_health_data)
    }

def main():
    """Executa demonstração completa de integração com APIs"""
    print("🌐 Mangaba Agent - Integração com APIs Externas")
    print("=" * 70)
    
    try:
        # Demonstrações individuais de APIs
        weather_result = demo_weather_integration()
        finance_result = demo_financial_integration()
        social_result = demo_social_media_integration()
        ecommerce_result = demo_ecommerce_integration()
        
        # Demonstrações avançadas
        orchestration_result = demo_multi_api_orchestration()
        monitoring_result = demo_api_monitoring_and_alerts()
        
        print("\n🎉 DEMONSTRAÇÃO DE INTEGRAÇÃO COMPLETA!")
        print("=" * 60)
        
        # Calcula estatísticas totais
        total_requests = (
            weather_result['api_stats']['requests_made'] +
            finance_result['api_stats']['requests_made'] +
            social_result['api_stats']['requests_made'] +
            ecommerce_result['api_stats']['requests_made'] +
            orchestration_result['orchestration_stats']['total_requests']
        )
        
        print("\n📊 Resumo dos Resultados:")
        print(f"   🌤️ APIs de Clima: {weather_result['api_stats']['requests_made']} requisições")
        print(f"   💹 APIs Financeiras: {finance_result['api_stats']['requests_made']} requisições")
        print(f"   📱 APIs Sociais: {social_result['api_stats']['requests_made']} requisições")
        print(f"   🛒 APIs E-commerce: {ecommerce_result['api_stats']['requests_made']} requisições")
        print(f"   🔄 Orquestração: {orchestration_result['orchestration_stats']['apis_integrated']} APIs")
        print(f"   🚨 Monitoramento: {monitoring_result['apis_monitored']} APIs")
        
        print(f"\n📈 Estatísticas Gerais:")
        print(f"   Total de requisições: {total_requests}")
        print(f"   APIs diferentes integradas: 4")
        print(f"   Análises geradas: 15+")
        print(f"   Insights cross-platform: Múltiplos")
        
        print("\n🚀 Capacidades Demonstradas:")
        print("   • Integração com APIs REST diversas")
        print("   • Análise inteligente de respostas")
        print("   • Orquestração de múltiplas fontes")
        print("   • Monitoramento de saúde de APIs")
        print("   • Geração de alertas automáticos")
        print("   • Correlação de dados cross-platform")
        print("   • Dashboards executivos integrados")
        print("   • Estratégias baseadas em dados")
        print("   • Planos de recuperação automáticos")
        
    except Exception as e:
        print(f"❌ Erro durante demonstração de APIs: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()