#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Marketing com Mangaba Agent
Demonstra aplicações de IA em marketing digital, análise de campanhas e estratégias
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangaba_agent import MangabaAgent
from protocols.mcp import ContextType, ContextPriority
import json
import random
from datetime import datetime, timedelta

class MarketingDataGenerator:
    """Gerador de dados de marketing sintéticos"""
    
    @staticmethod
    def generate_campaign_data():
        """Gera dados de campanhas de marketing"""
        campaigns = [
            {
                "campaign_id": "CAMP_001",
                "name": "Lançamento Produto X",
                "type": "Product Launch",
                "channel": "Facebook Ads",
                "budget": 15000.00,
                "spent": 12500.00,
                "impressions": 250000,
                "clicks": 3750,
                "conversions": 187,
                "revenue": 28050.00,
                "start_date": "2024-01-15",
                "end_date": "2024-02-15",
                "target_audience": "Mulheres 25-40, interessadas em tecnologia",
                "ctr": 1.5,
                "cpc": 3.33,
                "roas": 2.24
            },
            {
                "campaign_id": "CAMP_002",
                "name": "Black Friday 2024",
                "type": "Seasonal Promotion",
                "channel": "Google Ads",
                "budget": 25000.00,
                "spent": 24800.00,
                "impressions": 500000,
                "clicks": 8500,
                "conversions": 425,
                "revenue": 63750.00,
                "start_date": "2024-11-20",
                "end_date": "2024-11-30",
                "target_audience": "Compradores online, todas as idades",
                "ctr": 1.7,
                "cpc": 2.92,
                "roas": 2.57
            },
            {
                "campaign_id": "CAMP_003",
                "name": "Awareness Brand",
                "type": "Brand Awareness",
                "channel": "Instagram",
                "budget": 8000.00,
                "spent": 7200.00,
                "impressions": 180000,
                "clicks": 2160,
                "conversions": 54,
                "revenue": 8100.00,
                "start_date": "2024-03-01",
                "end_date": "2024-03-31",
                "target_audience": "Jovens 18-30, lifestyle",
                "ctr": 1.2,
                "cpc": 3.33,
                "roas": 1.13
            }
        ]
        return campaigns
    
    @staticmethod
    def generate_social_media_data():
        """Gera dados de redes sociais"""
        social_data = {
            "facebook": {
                "followers": 45000,
                "engagement_rate": 3.2,
                "posts_last_month": 25,
                "avg_likes": 450,
                "avg_comments": 35,
                "avg_shares": 12,
                "reach": 125000,
                "impressions": 180000
            },
            "instagram": {
                "followers": 32000,
                "engagement_rate": 4.8,
                "posts_last_month": 30,
                "avg_likes": 1200,
                "avg_comments": 85,
                "stories_views": 8500,
                "reach": 95000,
                "impressions": 140000
            },
            "linkedin": {
                "followers": 12000,
                "engagement_rate": 2.1,
                "posts_last_month": 15,
                "avg_likes": 180,
                "avg_comments": 25,
                "avg_shares": 8,
                "reach": 35000,
                "impressions": 50000
            },
            "youtube": {
                "subscribers": 8500,
                "videos_last_month": 8,
                "avg_views": 2500,
                "avg_likes": 125,
                "avg_comments": 45,
                "watch_time_hours": 1200,
                "impressions": 75000
            }
        }
        return social_data
    
    @staticmethod
    def generate_customer_journey_data():
        """Gera dados de jornada do cliente"""
        journey_stages = [
            {
                "stage": "Awareness",
                "visitors": 10000,
                "conversion_rate": 15.0,
                "avg_time_spent": "2:30",
                "top_sources": ["Google Organic", "Facebook", "Direct"]
            },
            {
                "stage": "Interest",
                "visitors": 1500,
                "conversion_rate": 25.0,
                "avg_time_spent": "5:45",
                "top_content": ["Blog Posts", "Product Pages", "Videos"]
            },
            {
                "stage": "Consideration",
                "visitors": 375,
                "conversion_rate": 40.0,
                "avg_time_spent": "8:20",
                "top_actions": ["Download Brochure", "Request Demo", "Compare Products"]
            },
            {
                "stage": "Purchase",
                "visitors": 150,
                "conversion_rate": 60.0,
                "avg_order_value": 250.00,
                "payment_methods": ["Credit Card", "PayPal", "Bank Transfer"]
            },
            {
                "stage": "Retention",
                "customers": 90,
                "repeat_purchase_rate": 35.0,
                "avg_lifetime_value": 750.00,
                "satisfaction_score": 4.2
            }
        ]
        return journey_stages

def demo_campaign_analysis():
    """Demonstra análise de campanhas de marketing"""
    print("📊 Análise de Campanhas de Marketing")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="marketing_analyst")
    
    # Gera dados de campanhas
    campaigns = MarketingDataGenerator.generate_campaign_data()
    
    print(f"📈 Analisando {len(campaigns)} campanhas...")
    
    # Análise de performance
    performance_prompt = f"""
    Analise a performance das seguintes campanhas de marketing:
    
    {json.dumps(campaigns, indent=2)}
    
    Forneça insights sobre:
    1. ROI e ROAS de cada campanha
    2. Eficiência de canais (Facebook, Google, Instagram)
    3. CTR e CPC comparativos
    4. Campanhas com melhor custo-benefício
    5. Recomendações de otimização
    """
    
    performance_analysis = agent.chat(performance_prompt, use_context=True)
    print(f"📊 Análise de Performance: {performance_analysis}")
    
    # Otimização de budget
    budget_optimization_prompt = """
    Com base na análise de performance, sugira uma redistribuição de orçamento:
    
    1. Quais campanhas merecem mais investimento?
    2. Quais campanhas devem ter orçamento reduzido?
    3. Novos canais a explorar
    4. Estratégias de bidding
    5. Cronograma de investimentos
    """
    
    budget_optimization = agent.chat(budget_optimization_prompt, use_context=True)
    print(f"💰 Otimização de Budget: {budget_optimization}")
    
    return {
        "campaigns_analyzed": len(campaigns),
        "performance_analysis": performance_analysis,
        "budget_optimization": budget_optimization
    }

def demo_social_media_strategy():
    """Demonstra estratégia de redes sociais"""
    print("\n📱 Estratégia de Redes Sociais")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="social_media_strategist")
    
    # Gera dados de redes sociais
    social_data = MarketingDataGenerator.generate_social_media_data()
    
    print(f"🌐 Analisando presença em {len(social_data)} plataformas...")
    
    # Análise de engajamento
    engagement_prompt = f"""
    Analise o desempenho nas redes sociais:
    
    {json.dumps(social_data, indent=2)}
    
    Avalie:
    1. Taxa de engajamento por plataforma
    2. Crescimento de seguidores
    3. Alcance e impressões
    4. Performance de conteúdo
    5. Oportunidades de melhoria
    """
    
    engagement_analysis = agent.chat(engagement_prompt, use_context=True)
    print(f"📈 Análise de Engajamento: {engagement_analysis}")
    
    # Estratégia de conteúdo
    content_strategy_prompt = """
    Desenvolva uma estratégia de conteúdo otimizada:
    
    1. Tipos de conteúdo para cada plataforma
    2. Frequência de postagem ideal
    3. Horários de maior engajamento
    4. Hashtags e palavras-chave
    5. Colaborações e parcerias
    6. Calendário editorial
    """
    
    content_strategy = agent.chat(content_strategy_prompt, use_context=True)
    print(f"📝 Estratégia de Conteúdo: {content_strategy}")
    
    # Influencer marketing
    influencer_strategy_prompt = """
    Sugira uma estratégia de marketing de influenciadores:
    
    1. Perfil ideal de influenciadores
    2. Micro vs macro influenciadores
    3. Tipos de colaboração
    4. Métricas de avaliação
    5. Budget e ROI esperado
    """
    
    influencer_strategy = agent.chat(influencer_strategy_prompt, use_context=True)
    print(f"\n🌟 Marketing de Influenciadores: {influencer_strategy}")
    
    return {
        "platforms_analyzed": len(social_data),
        "engagement_analysis": engagement_analysis,
        "content_strategy": content_strategy,
        "influencer_strategy": influencer_strategy
    }

def demo_customer_journey_optimization():
    """Demonstra otimização da jornada do cliente"""
    print("\n🛤️ Otimização da Jornada do Cliente")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="journey_optimizer")
    
    # Gera dados de jornada
    journey_data = MarketingDataGenerator.generate_customer_journey_data()
    
    print(f"🎯 Analisando {len(journey_data)} estágios da jornada...")
    
    # Análise de funil
    funnel_analysis_prompt = f"""
    Analise o funil de conversão da jornada do cliente:
    
    {json.dumps(journey_data, indent=2)}
    
    Identifique:
    1. Gargalos no funil de conversão
    2. Estágios com maior drop-off
    3. Oportunidades de otimização
    4. Pontos de fricção
    5. Estratégias de nurturing
    """
    
    funnel_analysis = agent.chat(funnel_analysis_prompt, use_context=True)
    print(f"🔍 Análise de Funil: {funnel_analysis}")
    
    # Personalização
    personalization_prompt = """
    Desenvolva estratégias de personalização para cada estágio:
    
    1. Conteúdo personalizado por estágio
    2. Triggers de automação
    3. Segmentação de audiência
    4. Mensagens direcionadas
    5. Ofertas personalizadas
    """
    
    personalization = agent.chat(personalization_prompt, use_context=True)
    print(f"🎨 Personalização: {personalization}")
    
    # Retenção e fidelização
    retention_prompt = """
    Crie estratégias de retenção e fidelização:
    
    1. Programas de fidelidade
    2. Email marketing pós-compra
    3. Upsell e cross-sell
    4. Atendimento proativo
    5. Comunidade de clientes
    """
    
    retention_strategy = agent.chat(retention_prompt, use_context=True)
    print(f"\n🔄 Estratégia de Retenção: {retention_strategy}")
    
    return {
        "journey_stages": len(journey_data),
        "funnel_analysis": funnel_analysis,
        "personalization": personalization,
        "retention_strategy": retention_strategy
    }

def demo_market_research():
    """Demonstra pesquisa de mercado"""
    print("\n🔬 Pesquisa de Mercado")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="market_researcher")
    
    # Simula dados de pesquisa
    market_data = {
        "target_market": {
            "size": "R$ 2.5 bilhões",
            "growth_rate": "8.5% ao ano",
            "segments": ["Premium", "Mid-market", "Budget"],
            "demographics": {
                "age_groups": {"18-25": 25, "26-35": 35, "36-45": 25, "46+": 15},
                "income_levels": {"High": 20, "Medium": 60, "Low": 20},
                "locations": {"Urban": 70, "Suburban": 25, "Rural": 5}
            }
        },
        "competitors": [
            {"name": "Competitor A", "market_share": 25, "strengths": ["Brand", "Distribution"], "weaknesses": ["Price", "Innovation"]},
            {"name": "Competitor B", "market_share": 20, "strengths": ["Technology", "Customer Service"], "weaknesses": ["Marketing", "Scale"]},
            {"name": "Competitor C", "market_share": 15, "strengths": ["Price", "Efficiency"], "weaknesses": ["Quality", "Brand"]}
        ],
        "trends": [
            "Digitalização acelerada",
            "Sustentabilidade",
            "Personalização",
            "Mobile-first",
            "IA e automação"
        ]
    }
    
    print("📊 Analisando dados de mercado...")
    
    # Análise competitiva
    competitive_analysis_prompt = f"""
    Realize uma análise competitiva detalhada:
    
    {json.dumps(market_data, indent=2)}
    
    Analise:
    1. Posicionamento competitivo
    2. Gaps no mercado
    3. Oportunidades de diferenciação
    4. Ameaças competitivas
    5. Estratégias de entrada/expansão
    """
    
    competitive_analysis = agent.chat(competitive_analysis_prompt, use_context=True)
    print(f"⚔️ Análise Competitiva: {competitive_analysis}")
    
    # Segmentação de mercado
    segmentation_prompt = """
    Desenvolva uma estratégia de segmentação:
    
    1. Segmentos prioritários
    2. Personas detalhadas
    3. Proposta de valor por segmento
    4. Canais de distribuição
    5. Estratégias de pricing
    """
    
    segmentation = agent.chat(segmentation_prompt, use_context=True)
    print(f"🎯 Segmentação: {segmentation}")
    
    # Previsão de tendências
    trends_forecast_prompt = """
    Analise as tendências e faça previsões:
    
    1. Impacto das tendências no negócio
    2. Oportunidades emergentes
    3. Riscos e desafios
    4. Adaptações necessárias
    5. Cronograma de implementação
    """
    
    trends_forecast = agent.chat(trends_forecast_prompt, use_context=True)
    print(f"\n🔮 Previsão de Tendências: {trends_forecast}")
    
    return {
        "market_segments": len(market_data["target_market"]["segments"]),
        "competitors_analyzed": len(market_data["competitors"]),
        "competitive_analysis": competitive_analysis,
        "segmentation": segmentation,
        "trends_forecast": trends_forecast
    }

def demo_marketing_automation():
    """Demonstra automação de marketing"""
    print("\n🤖 Automação de Marketing")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="automation_specialist")
    
    # Simula dados de automação
    automation_data = {
        "email_campaigns": {
            "welcome_series": {"emails": 5, "open_rate": 45, "click_rate": 12, "conversion_rate": 8},
            "abandoned_cart": {"emails": 3, "open_rate": 35, "click_rate": 18, "conversion_rate": 15},
            "re_engagement": {"emails": 4, "open_rate": 25, "click_rate": 8, "conversion_rate": 5},
            "post_purchase": {"emails": 3, "open_rate": 55, "click_rate": 22, "conversion_rate": 12}
        },
        "lead_scoring": {
            "criteria": ["Email opens", "Website visits", "Content downloads", "Demo requests"],
            "thresholds": {"Cold": "0-25", "Warm": "26-50", "Hot": "51-75", "Qualified": "76-100"}
        },
        "workflows": [
            {"name": "Lead Nurturing", "triggers": 5, "actions": 12, "conversion_rate": 18},
            {"name": "Customer Onboarding", "triggers": 3, "actions": 8, "completion_rate": 85},
            {"name": "Upsell Campaign", "triggers": 4, "actions": 6, "success_rate": 22}
        ]
    }
    
    print("⚙️ Analisando automações de marketing...")
    
    # Análise de performance
    automation_analysis_prompt = f"""
    Analise a performance das automações de marketing:
    
    {json.dumps(automation_data, indent=2)}
    
    Avalie:
    1. Eficácia das campanhas de email
    2. Sistema de lead scoring
    3. Performance dos workflows
    4. Oportunidades de otimização
    5. Novas automações a implementar
    """
    
    automation_analysis = agent.chat(automation_analysis_prompt, use_context=True)
    print(f"📊 Análise de Automação: {automation_analysis}")
    
    # Otimização de workflows
    workflow_optimization_prompt = """
    Sugira otimizações para os workflows:
    
    1. Melhorias nos triggers
    2. Sequências de ações mais eficazes
    3. Personalização avançada
    4. Testes A/B recomendados
    5. Integração entre canais
    """
    
    workflow_optimization = agent.chat(workflow_optimization_prompt, use_context=True)
    print(f"🔧 Otimização de Workflows: {workflow_optimization}")
    
    # IA e machine learning
    ai_integration_prompt = """
    Proponha integração de IA nas automações:
    
    1. Predição de comportamento do cliente
    2. Otimização automática de campanhas
    3. Personalização em tempo real
    4. Chatbots inteligentes
    5. Análise preditiva de churn
    """
    
    ai_integration = agent.chat(ai_integration_prompt, use_context=True)
    print(f"\n🧠 Integração de IA: {ai_integration}")
    
    return {
        "email_campaigns": len(automation_data["email_campaigns"]),
        "workflows": len(automation_data["workflows"]),
        "automation_analysis": automation_analysis,
        "workflow_optimization": workflow_optimization,
        "ai_integration": ai_integration
    }

def main():
    """Executa demonstração completa de marketing"""
    print("🚀 Mangaba Agent - Soluções de Marketing")
    print("=" * 80)
    
    try:
        # Demonstrações de diferentes áreas de marketing
        campaign_result = demo_campaign_analysis()
        social_result = demo_social_media_strategy()
        journey_result = demo_customer_journey_optimization()
        research_result = demo_market_research()
        automation_result = demo_marketing_automation()
        
        print("\n🎉 DEMONSTRAÇÃO DE MARKETING COMPLETA!")
        print("=" * 70)
        
        print("\n📊 Resumo dos Resultados:")
        print(f"   📈 Campanhas analisadas: {campaign_result['campaigns_analyzed']}")
        print(f"   📱 Plataformas sociais: {social_result['platforms_analyzed']}")
        print(f"   🛤️ Estágios da jornada: {journey_result['journey_stages']}")
        print(f"   🏢 Concorrentes analisados: {research_result['competitors_analyzed']}")
        print(f"   🤖 Workflows de automação: {automation_result['workflows']}")
        
        print(f"\n🚀 Capacidades Demonstradas:")
        print("   • Análise de performance de campanhas")
        print("   • Otimização de orçamento publicitário")
        print("   • Estratégia de redes sociais")
        print("   • Marketing de influenciadores")
        print("   • Otimização da jornada do cliente")
        print("   • Personalização de experiências")
        print("   • Pesquisa e análise competitiva")
        print("   • Segmentação de mercado")
        print("   • Automação de marketing")
        print("   • Integração de IA em campanhas")
        print("   • Análise preditiva de tendências")
        print("   • ROI e ROAS optimization")
        
    except Exception as e:
        print(f"❌ Erro durante demonstração de marketing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()