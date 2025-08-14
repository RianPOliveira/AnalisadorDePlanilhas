#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Finanças com Mangaba Agent
Demonstra aplicações de IA em análise financeira, gestão de riscos e planejamento
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangaba_agent import MangabaAgent
from protocols.mcp import ContextType, ContextPriority
import json
import random
from datetime import datetime, timedelta

class FinanceDataGenerator:
    """Gerador de dados financeiros sintéticos"""
    
    @staticmethod
    def generate_financial_statements():
        """Gera demonstrações financeiras"""
        statements = {
            "balance_sheet": {
                "assets": {
                    "current_assets": {
                        "cash": 250000.00,
                        "accounts_receivable": 180000.00,
                        "inventory": 120000.00,
                        "prepaid_expenses": 15000.00,
                        "total": 565000.00
                    },
                    "non_current_assets": {
                        "property_plant_equipment": 800000.00,
                        "intangible_assets": 150000.00,
                        "investments": 100000.00,
                        "total": 1050000.00
                    },
                    "total_assets": 1615000.00
                },
                "liabilities": {
                    "current_liabilities": {
                        "accounts_payable": 95000.00,
                        "short_term_debt": 50000.00,
                        "accrued_expenses": 35000.00,
                        "total": 180000.00
                    },
                    "non_current_liabilities": {
                        "long_term_debt": 400000.00,
                        "deferred_tax": 25000.00,
                        "total": 425000.00
                    },
                    "total_liabilities": 605000.00
                },
                "equity": {
                    "share_capital": 500000.00,
                    "retained_earnings": 510000.00,
                    "total_equity": 1010000.00
                },
                "total_liabilities_equity": 1615000.00
            },
            "income_statement": {
                "revenue": {
                    "sales_revenue": 2500000.00,
                    "service_revenue": 800000.00,
                    "other_revenue": 50000.00,
                    "total_revenue": 3350000.00
                },
                "expenses": {
                    "cost_of_goods_sold": 1500000.00,
                    "salaries_wages": 650000.00,
                    "rent": 120000.00,
                    "utilities": 45000.00,
                    "marketing": 85000.00,
                    "depreciation": 80000.00,
                    "interest_expense": 35000.00,
                    "other_expenses": 95000.00,
                    "total_expenses": 2610000.00
                },
                "ebitda": 820000.00,
                "ebit": 740000.00,
                "net_income": 705000.00,
                "earnings_per_share": 14.10
            },
            "cash_flow": {
                "operating_activities": {
                    "net_income": 705000.00,
                    "depreciation": 80000.00,
                    "changes_working_capital": -45000.00,
                    "operating_cash_flow": 740000.00
                },
                "investing_activities": {
                    "capital_expenditures": -150000.00,
                    "investments": -25000.00,
                    "investing_cash_flow": -175000.00
                },
                "financing_activities": {
                    "debt_proceeds": 100000.00,
                    "debt_payments": -80000.00,
                    "dividends_paid": -200000.00,
                    "financing_cash_flow": -180000.00
                },
                "net_cash_flow": 385000.00,
                "beginning_cash": 115000.00,
                "ending_cash": 500000.00
            }
        }
        return statements
    
    @staticmethod
    def generate_budget_data():
        """Gera dados de orçamento"""
        budget = {
            "annual_budget_2024": {
                "revenue_budget": {
                    "q1": {"planned": 750000.00, "actual": 780000.00, "variance": 30000.00},
                    "q2": {"planned": 800000.00, "actual": 820000.00, "variance": 20000.00},
                    "q3": {"planned": 850000.00, "actual": 835000.00, "variance": -15000.00},
                    "q4": {"planned": 900000.00, "actual": 915000.00, "variance": 15000.00},
                    "total": {"planned": 3300000.00, "actual": 3350000.00, "variance": 50000.00}
                },
                "expense_budget": {
                    "personnel": {"planned": 600000.00, "actual": 650000.00, "variance": -50000.00},
                    "operations": {"planned": 1450000.00, "actual": 1500000.00, "variance": -50000.00},
                    "marketing": {"planned": 100000.00, "actual": 85000.00, "variance": 15000.00},
                    "technology": {"planned": 200000.00, "actual": 180000.00, "variance": 20000.00},
                    "facilities": {"planned": 150000.00, "actual": 165000.00, "variance": -15000.00},
                    "other": {"planned": 100000.00, "actual": 95000.00, "variance": 5000.00},
                    "total": {"planned": 2600000.00, "actual": 2675000.00, "variance": -75000.00}
                },
                "capital_budget": {
                    "equipment": {"planned": 120000.00, "actual": 100000.00, "variance": 20000.00},
                    "technology": {"planned": 80000.00, "actual": 75000.00, "variance": 5000.00},
                    "facilities": {"planned": 50000.00, "actual": 60000.00, "variance": -10000.00},
                    "total": {"planned": 250000.00, "actual": 235000.00, "variance": 15000.00}
                }
            },
            "budget_2025": {
                "revenue_projection": 3800000.00,
                "expense_projection": 2950000.00,
                "capex_projection": 300000.00,
                "net_income_projection": 850000.00,
                "growth_assumptions": {
                    "revenue_growth": 13.4,
                    "expense_growth": 10.3,
                    "margin_improvement": 1.2
                }
            }
        }
        return budget
    
    @staticmethod
    def generate_investment_portfolio():
        """Gera dados de portfólio de investimentos"""
        portfolio = {
            "cash_investments": [
                {
                    "type": "Conta Corrente",
                    "institution": "Banco Principal",
                    "balance": 150000.00,
                    "yield": 0.5,
                    "liquidity": "Imediata",
                    "risk_level": "Baixo"
                },
                {
                    "type": "CDB",
                    "institution": "Banco Investimentos",
                    "balance": 200000.00,
                    "yield": 12.5,
                    "maturity": "2025-06-15",
                    "liquidity": "Baixa",
                    "risk_level": "Baixo"
                },
                {
                    "type": "LCI",
                    "institution": "Banco Regional",
                    "balance": 100000.00,
                    "yield": 11.8,
                    "maturity": "2024-12-20",
                    "liquidity": "Baixa",
                    "risk_level": "Baixo"
                }
            ],
            "equity_investments": [
                {
                    "type": "Ações",
                    "ticker": "PETR4",
                    "quantity": 1000,
                    "purchase_price": 28.50,
                    "current_price": 32.10,
                    "market_value": 32100.00,
                    "gain_loss": 3600.00,
                    "dividend_yield": 8.2
                },
                {
                    "type": "Ações",
                    "ticker": "VALE3",
                    "quantity": 500,
                    "purchase_price": 65.20,
                    "current_price": 71.80,
                    "market_value": 35900.00,
                    "gain_loss": 3300.00,
                    "dividend_yield": 12.5
                },
                {
                    "type": "ETF",
                    "ticker": "BOVA11",
                    "quantity": 200,
                    "purchase_price": 105.30,
                    "current_price": 112.45,
                    "market_value": 22490.00,
                    "gain_loss": 1430.00,
                    "dividend_yield": 5.8
                }
            ],
            "fixed_income": [
                {
                    "type": "Tesouro IPCA+",
                    "amount": 150000.00,
                    "yield": "IPCA + 6.2%",
                    "maturity": "2029-08-15",
                    "risk_level": "Baixo",
                    "current_value": 158500.00
                },
                {
                    "type": "Debênture",
                    "issuer": "Empresa XYZ",
                    "amount": 100000.00,
                    "yield": "CDI + 2.5%",
                    "maturity": "2026-03-10",
                    "risk_level": "Médio",
                    "current_value": 105200.00
                }
            ],
            "portfolio_summary": {
                "total_invested": 950000.00,
                "current_value": 1004190.00,
                "total_return": 54190.00,
                "return_percentage": 5.7,
                "asset_allocation": {
                    "cash": 35.2,
                    "fixed_income": 27.8,
                    "equities": 37.0
                },
                "risk_metrics": {
                    "volatility": 12.5,
                    "sharpe_ratio": 1.8,
                    "max_drawdown": -8.2
                }
            }
        }
        return portfolio
    
    @staticmethod
    def generate_financial_ratios():
        """Gera indicadores financeiros"""
        ratios = {
            "liquidity_ratios": {
                "current_ratio": 3.14,
                "quick_ratio": 2.47,
                "cash_ratio": 1.39,
                "operating_cash_flow_ratio": 4.11
            },
            "profitability_ratios": {
                "gross_margin": 55.2,
                "operating_margin": 22.1,
                "net_margin": 21.0,
                "return_on_assets": 43.7,
                "return_on_equity": 69.8,
                "return_on_invested_capital": 52.3
            },
            "efficiency_ratios": {
                "asset_turnover": 2.07,
                "inventory_turnover": 12.5,
                "receivables_turnover": 18.6,
                "payables_turnover": 15.8,
                "working_capital_turnover": 8.7
            },
            "leverage_ratios": {
                "debt_to_equity": 0.60,
                "debt_to_assets": 0.37,
                "equity_multiplier": 1.60,
                "interest_coverage": 21.1,
                "debt_service_coverage": 5.7
            },
            "market_ratios": {
                "price_to_earnings": 15.2,
                "price_to_book": 2.8,
                "price_to_sales": 1.9,
                "dividend_yield": 4.2,
                "earnings_yield": 6.6
            },
            "growth_ratios": {
                "revenue_growth": 15.3,
                "earnings_growth": 22.1,
                "asset_growth": 8.7,
                "equity_growth": 12.4
            }
        }
        return ratios

def demo_financial_analysis():
    """Demonstra análise financeira completa"""
    print("💰 Análise Financeira")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="financial_analyst")
    
    # Gera demonstrações financeiras
    statements = FinanceDataGenerator.generate_financial_statements()
    ratios = FinanceDataGenerator.generate_financial_ratios()
    
    print("📊 Analisando demonstrações financeiras...")
    
    # Análise das demonstrações
    financial_analysis_prompt = f"""
    Analise as demonstrações financeiras:
    
    {json.dumps(statements, indent=2)}
    
    Indicadores financeiros:
    {json.dumps(ratios, indent=2)}
    
    Forneça análise completa sobre:
    1. Saúde financeira geral
    2. Liquidez e solvência
    3. Rentabilidade e eficiência
    4. Estrutura de capital
    5. Geração de caixa
    6. Pontos fortes e fracos
    7. Recomendações estratégicas
    """
    
    financial_analysis = agent.chat(financial_analysis_prompt, use_context=True)
    print(f"📈 Análise Financeira: {financial_analysis}")
    
    # Análise de tendências
    trend_analysis_prompt = """
    Analise tendências financeiras:
    
    1. Evolução dos indicadores
    2. Padrões sazonais
    3. Ciclos de negócio
    4. Projeções futuras
    5. Benchmarking setorial
    6. Alertas e oportunidades
    """
    
    trend_analysis = agent.chat(trend_analysis_prompt, use_context=True)
    print(f"📊 Análise de Tendências: {trend_analysis}")
    
    # Valuation
    valuation_prompt = """
    Realize valuation da empresa:
    
    1. Métodos de avaliação (DCF, múltiplos)
    2. Valor intrínseco
    3. Cenários de valuation
    4. Sensibilidade a variáveis
    5. Comparação com mercado
    6. Recomendação de investimento
    """
    
    valuation = agent.chat(valuation_prompt, use_context=True)
    print(f"\n💎 Valuation: {valuation}")
    
    return {
        "statements_analyzed": True,
        "financial_analysis": financial_analysis,
        "trend_analysis": trend_analysis,
        "valuation": valuation
    }

def demo_budget_planning():
    """Demonstra planejamento orçamentário"""
    print("\n📋 Planejamento Orçamentário")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="budget_planner")
    
    # Gera dados de orçamento
    budget_data = FinanceDataGenerator.generate_budget_data()
    
    print("📊 Analisando performance orçamentária...")
    
    # Análise orçamentária
    budget_analysis_prompt = f"""
    Analise a performance orçamentária:
    
    {json.dumps(budget_data, indent=2)}
    
    Avalie:
    1. Variações orçamentárias por categoria
    2. Causas dos desvios
    3. Impacto nos resultados
    4. Ações corretivas necessárias
    5. Revisões de projeções
    6. Controles orçamentários
    """
    
    budget_analysis = agent.chat(budget_analysis_prompt, use_context=True)
    print(f"📊 Análise Orçamentária: {budget_analysis}")
    
    # Planejamento 2025
    budget_planning_prompt = """
    Desenvolva orçamento detalhado para 2025:
    
    1. Projeções de receita por segmento
    2. Planejamento de despesas
    3. Investimentos de capital
    4. Fluxo de caixa projetado
    5. Cenários otimista/pessimista
    6. KPIs de acompanhamento
    """
    
    budget_planning = agent.chat(budget_planning_prompt, use_context=True)
    print(f"📈 Planejamento 2025: {budget_planning}")
    
    # Controle orçamentário
    budget_control_prompt = """
    Implemente sistema de controle orçamentário:
    
    1. Relatórios de acompanhamento
    2. Alertas automáticos
    3. Processo de revisões
    4. Responsabilidades por centro de custo
    5. Métricas de performance
    6. Dashboard executivo
    """
    
    budget_control = agent.chat(budget_control_prompt, use_context=True)
    print(f"🎯 Controle Orçamentário: {budget_control}")
    
    # Rolling forecast
    rolling_forecast_prompt = """
    Desenvolva processo de rolling forecast:
    
    1. Metodologia de previsão
    2. Frequência de atualizações
    3. Drivers de negócio
    4. Modelos preditivos
    5. Integração com planejamento
    6. Comunicação de resultados
    """
    
    rolling_forecast = agent.chat(rolling_forecast_prompt, use_context=True)
    print(f"\n🔄 Rolling Forecast: {rolling_forecast}")
    
    return {
        "budget_periods_analyzed": 2,
        "budget_analysis": budget_analysis,
        "budget_planning": budget_planning,
        "budget_control": budget_control,
        "rolling_forecast": rolling_forecast
    }

def demo_investment_management():
    """Demonstra gestão de investimentos"""
    print("\n📈 Gestão de Investimentos")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="investment_manager")
    
    # Gera dados de portfólio
    portfolio = FinanceDataGenerator.generate_investment_portfolio()
    
    print(f"💼 Analisando portfólio de investimentos...")
    
    # Análise de portfólio
    portfolio_analysis_prompt = f"""
    Analise o portfólio de investimentos:
    
    {json.dumps(portfolio, indent=2)}
    
    Avalie:
    1. Diversificação do portfólio
    2. Relação risco-retorno
    3. Adequação aos objetivos
    4. Performance vs. benchmarks
    5. Concentração de riscos
    6. Oportunidades de otimização
    """
    
    portfolio_analysis = agent.chat(portfolio_analysis_prompt, use_context=True)
    print(f"📊 Análise de Portfólio: {portfolio_analysis}")
    
    # Estratégia de investimento
    investment_strategy_prompt = """
    Desenvolva estratégia de investimento:
    
    1. Objetivos de investimento
    2. Perfil de risco
    3. Horizonte temporal
    4. Asset allocation estratégica
    5. Critérios de seleção
    6. Política de rebalanceamento
    """
    
    investment_strategy = agent.chat(investment_strategy_prompt, use_context=True)
    print(f"🎯 Estratégia de Investimento: {investment_strategy}")
    
    # Gestão de riscos
    risk_management_prompt = """
    Implemente gestão de riscos de investimento:
    
    1. Identificação de riscos
    2. Métricas de risco (VaR, CVaR)
    3. Limites de exposição
    4. Hedging strategies
    5. Stress testing
    6. Monitoramento contínuo
    """
    
    risk_management = agent.chat(risk_management_prompt, use_context=True)
    print(f"⚠️ Gestão de Riscos: {risk_management}")
    
    # Performance attribution
    performance_attribution_prompt = """
    Realize análise de performance attribution:
    
    1. Decomposição de retornos
    2. Contribuição por ativo
    3. Efeito de seleção vs. alocação
    4. Análise de timing
    5. Benchmarking
    6. Relatórios de performance
    """
    
    performance_attribution = agent.chat(performance_attribution_prompt, use_context=True)
    print(f"\n📈 Performance Attribution: {performance_attribution}")
    
    return {
        "assets_analyzed": len(portfolio['cash_investments']) + len(portfolio['equity_investments']) + len(portfolio['fixed_income']),
        "portfolio_analysis": portfolio_analysis,
        "investment_strategy": investment_strategy,
        "risk_management": risk_management,
        "performance_attribution": performance_attribution
    }

def demo_risk_assessment():
    """Demonstra avaliação de riscos financeiros"""
    print("\n⚠️ Avaliação de Riscos")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="risk_analyst")
    
    # Simula dados de risco
    risk_data = {
        "market_risks": {
            "interest_rate_risk": {
                "exposure": 500000.00,
                "duration": 3.2,
                "sensitivity": -16000.00,
                "hedge_ratio": 0.75
            },
            "currency_risk": {
                "usd_exposure": 200000.00,
                "eur_exposure": 150000.00,
                "hedge_ratio": 0.60,
                "var_1day": 8500.00
            },
            "equity_risk": {
                "portfolio_value": 300000.00,
                "beta": 1.15,
                "var_1day": 12000.00,
                "max_drawdown": -18.5
            }
        },
        "credit_risks": {
            "counterparty_exposure": [
                {"name": "Cliente A", "exposure": 150000.00, "rating": "BBB", "pd": 0.8},
                {"name": "Cliente B", "exposure": 200000.00, "rating": "A", "pd": 0.3},
                {"name": "Cliente C", "exposure": 100000.00, "rating": "BB", "pd": 2.1},
                {"name": "Banco X", "exposure": 300000.00, "rating": "AA", "pd": 0.1}
            ],
            "total_exposure": 750000.00,
            "expected_loss": 6750.00,
            "concentration_risk": "Médio"
        },
        "operational_risks": {
            "process_failures": {"frequency": 2, "avg_loss": 15000.00, "max_loss": 50000.00},
            "system_failures": {"frequency": 1, "avg_loss": 25000.00, "max_loss": 100000.00},
            "fraud_risk": {"frequency": 0.5, "avg_loss": 40000.00, "max_loss": 200000.00},
            "regulatory_risk": {"probability": 0.1, "impact": 150000.00}
        },
        "liquidity_risks": {
            "cash_position": 250000.00,
            "credit_lines": 500000.00,
            "liquid_assets": 400000.00,
            "funding_gap": -50000.00,
            "stress_scenario": -180000.00
        }
    }
    
    print("⚠️ Avaliando riscos financeiros...")
    
    # Análise de riscos
    risk_analysis_prompt = f"""
    Analise os riscos financeiros:
    
    {json.dumps(risk_data, indent=2)}
    
    Avalie:
    1. Exposição por tipo de risco
    2. Concentrações de risco
    3. Correlações entre riscos
    4. Adequação de capital
    5. Efetividade dos hedges
    6. Cenários de stress
    """
    
    risk_analysis = agent.chat(risk_analysis_prompt, use_context=True)
    print(f"📊 Análise de Riscos: {risk_analysis}")
    
    # Modelo de risco
    risk_modeling_prompt = """
    Desenvolva modelo integrado de risco:
    
    1. Metodologia VaR/CVaR
    2. Simulação Monte Carlo
    3. Stress testing
    4. Backtesting
    5. Limites de risco
    6. Reporting automático
    """
    
    risk_modeling = agent.chat(risk_modeling_prompt, use_context=True)
    print(f"🔬 Modelagem de Risco: {risk_modeling}")
    
    # Estratégias de mitigação
    risk_mitigation_prompt = """
    Desenvolva estratégias de mitigação:
    
    1. Hedging strategies
    2. Diversificação
    3. Seguros e garantias
    4. Controles internos
    5. Planos de contingência
    6. Monitoramento contínuo
    """
    
    risk_mitigation = agent.chat(risk_mitigation_prompt, use_context=True)
    print(f"🛡️ Mitigação de Riscos: {risk_mitigation}")
    
    # Governança de riscos
    risk_governance_prompt = """
    Implemente governança de riscos:
    
    1. Estrutura organizacional
    2. Políticas e procedimentos
    3. Comitês de risco
    4. Reporting para alta administração
    5. Cultura de risco
    6. Compliance regulatório
    """
    
    risk_governance = agent.chat(risk_governance_prompt, use_context=True)
    print(f"\n🏛️ Governança de Riscos: {risk_governance}")
    
    return {
        "risk_categories": 4,
        "risk_analysis": risk_analysis,
        "risk_modeling": risk_modeling,
        "risk_mitigation": risk_mitigation,
        "risk_governance": risk_governance
    }

def demo_financial_planning():
    """Demonstra planejamento financeiro estratégico"""
    print("\n🎯 Planejamento Financeiro")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="financial_planner")
    
    # Simula dados de planejamento
    planning_data = {
        "strategic_objectives": [
            {"objective": "Crescimento de receita 25%", "timeline": "3 anos", "investment": 500000.00},
            {"objective": "Expansão internacional", "timeline": "2 anos", "investment": 800000.00},
            {"objective": "Digitalização completa", "timeline": "18 meses", "investment": 300000.00},
            {"objective": "Aquisição estratégica", "timeline": "1 ano", "investment": 2000000.00}
        ],
        "financial_constraints": {
            "available_cash": 1200000.00,
            "credit_capacity": 1500000.00,
            "debt_limit": 0.6,
            "minimum_liquidity": 300000.00,
            "dividend_policy": 0.3
        },
        "scenarios": {
            "base_case": {"revenue_growth": 15, "margin_improvement": 2, "capex_ratio": 8},
            "optimistic": {"revenue_growth": 25, "margin_improvement": 4, "capex_ratio": 12},
            "pessimistic": {"revenue_growth": 5, "margin_improvement": -1, "capex_ratio": 5}
        }
    }
    
    print("🎯 Desenvolvendo planejamento financeiro...")
    
    # Planejamento estratégico
    strategic_planning_prompt = f"""
    Desenvolva planejamento financeiro estratégico:
    
    {json.dumps(planning_data, indent=2)}
    
    Analise:
    1. Viabilidade dos objetivos
    2. Necessidades de financiamento
    3. Estrutura de capital ótima
    4. Cronograma de investimentos
    5. Impacto nos indicadores
    6. Alternativas de financiamento
    """
    
    strategic_planning = agent.chat(strategic_planning_prompt, use_context=True)
    print(f"📊 Planejamento Estratégico: {strategic_planning}")
    
    # Projeções financeiras
    financial_projections_prompt = """
    Crie projeções financeiras detalhadas:
    
    1. Demonstrações projetadas (5 anos)
    2. Fluxo de caixa livre
    3. Necessidades de capital de giro
    4. Análise de sensibilidade
    5. Pontos de equilíbrio
    6. Métricas de retorno
    """
    
    financial_projections = agent.chat(financial_projections_prompt, use_context=True)
    print(f"📈 Projeções Financeiras: {financial_projections}")
    
    # Otimização de capital
    capital_optimization_prompt = """
    Otimize estrutura de capital:
    
    1. Custo médio ponderado de capital
    2. Alavancagem ótima
    3. Mix debt/equity
    4. Timing de financiamentos
    5. Política de dividendos
    6. Gestão de liquidez
    """
    
    capital_optimization = agent.chat(capital_optimization_prompt, use_context=True)
    print(f"⚖️ Otimização de Capital: {capital_optimization}")
    
    # Monitoramento e controle
    monitoring_control_prompt = """
    Implemente sistema de monitoramento:
    
    1. KPIs financeiros
    2. Dashboards executivos
    3. Alertas automáticos
    4. Revisões periódicas
    5. Ações corretivas
    6. Comunicação com stakeholders
    """
    
    monitoring_control = agent.chat(monitoring_control_prompt, use_context=True)
    print(f"\n📊 Monitoramento e Controle: {monitoring_control}")
    
    return {
        "strategic_objectives": len(planning_data['strategic_objectives']),
        "strategic_planning": strategic_planning,
        "financial_projections": financial_projections,
        "capital_optimization": capital_optimization,
        "monitoring_control": monitoring_control
    }

def demo_treasury_management():
    """Demonstra gestão de tesouraria"""
    print("\n💎 Gestão de Tesouraria")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="treasury_manager")
    
    # Simula dados de tesouraria
    treasury_data = {
        "cash_positions": {
            "brl_accounts": [
                {"bank": "Banco A", "balance": 150000.00, "rate": 0.5},
                {"bank": "Banco B", "balance": 200000.00, "rate": 0.8},
                {"bank": "Banco C", "balance": 100000.00, "rate": 0.3}
            ],
            "usd_accounts": [
                {"bank": "Bank X", "balance": 50000.00, "rate": 2.1},
                {"bank": "Bank Y", "balance": 30000.00, "rate": 1.8}
            ],
            "total_brl": 450000.00,
            "total_usd": 80000.00
        },
        "cash_flow_forecast": {
            "week_1": {"inflows": 200000.00, "outflows": 180000.00, "net": 20000.00},
            "week_2": {"inflows": 150000.00, "outflows": 220000.00, "net": -70000.00},
            "week_3": {"inflows": 300000.00, "outflows": 160000.00, "net": 140000.00},
            "week_4": {"inflows": 180000.00, "outflows": 200000.00, "net": -20000.00}
        },
        "funding_facilities": [
            {"type": "Linha de Crédito", "limit": 500000.00, "used": 100000.00, "rate": "CDI + 3.5%"},
            {"type": "Conta Garantida", "limit": 200000.00, "used": 0.00, "rate": "CDI + 5.0%"},
            {"type": "FIDC", "limit": 300000.00, "used": 150000.00, "rate": "CDI + 2.8%"}
        ],
        "fx_exposures": {
            "usd_receivables": 120000.00,
            "usd_payables": 80000.00,
            "net_exposure": 40000.00,
            "hedge_ratio": 0.75
        }
    }
    
    print("💰 Otimizando gestão de tesouraria...")
    
    # Gestão de liquidez
    liquidity_management_prompt = f"""
    Otimize gestão de liquidez:
    
    {json.dumps(treasury_data, indent=2)}
    
    Analise:
    1. Posições de caixa por moeda
    2. Previsão de fluxo de caixa
    3. Necessidades de funding
    4. Otimização de rendimentos
    5. Gestão de concentração bancária
    6. Políticas de cash pooling
    """
    
    liquidity_management = agent.chat(liquidity_management_prompt, use_context=True)
    print(f"💧 Gestão de Liquidez: {liquidity_management}")
    
    # Gestão cambial
    fx_management_prompt = """
    Desenvolva estratégia cambial:
    
    1. Identificação de exposições
    2. Políticas de hedge
    3. Instrumentos derivativos
    4. Timing de operações
    5. Limites de risco
    6. Monitoramento de posições
    """
    
    fx_management = agent.chat(fx_management_prompt, use_context=True)
    print(f"💱 Gestão Cambial: {fx_management}")
    
    # Otimização de funding
    funding_optimization_prompt = """
    Otimize estrutura de funding:
    
    1. Diversificação de fontes
    2. Custo de funding
    3. Prazos e vencimentos
    4. Covenants e garantias
    5. Relacionamento bancário
    6. Contingency funding
    """
    
    funding_optimization = agent.chat(funding_optimization_prompt, use_context=True)
    print(f"🏦 Otimização de Funding: {funding_optimization}")
    
    # Cash management
    cash_management_prompt = """
    Implemente cash management avançado:
    
    1. Automação de processos
    2. Sistemas de pagamento
    3. Conciliação bancária
    4. Controles de segurança
    5. Reporting em tempo real
    6. Integração com ERP
    """
    
    cash_management = agent.chat(cash_management_prompt, use_context=True)
    print(f"\n💳 Cash Management: {cash_management}")
    
    return {
        "accounts_managed": len(treasury_data['cash_positions']['brl_accounts']) + len(treasury_data['cash_positions']['usd_accounts']),
        "liquidity_management": liquidity_management,
        "fx_management": fx_management,
        "funding_optimization": funding_optimization,
        "cash_management": cash_management
    }

def main():
    """Executa demonstração completa de soluções financeiras"""
    print("💰 Mangaba Agent - Soluções Financeiras")
    print("=" * 80)
    
    try:
        # Demonstrações de diferentes áreas financeiras
        analysis_result = demo_financial_analysis()
        budget_result = demo_budget_planning()
        investment_result = demo_investment_management()
        risk_result = demo_risk_assessment()
        planning_result = demo_financial_planning()
        treasury_result = demo_treasury_management()
        
        print("\n🎉 DEMONSTRAÇÃO FINANCEIRA COMPLETA!")
        print("=" * 70)
        
        print("\n📊 Resumo dos Resultados:")
        print(f"   📈 Demonstrações analisadas: {analysis_result['statements_analyzed']}")
        print(f"   📋 Períodos orçamentários: {budget_result['budget_periods_analyzed']}")
        print(f"   💼 Ativos analisados: {investment_result['assets_analyzed']}")
        print(f"   ⚠️ Categorias de risco: {risk_result['risk_categories']}")
        print(f"   🎯 Objetivos estratégicos: {planning_result['strategic_objectives']}")
        print(f"   💰 Contas gerenciadas: {treasury_result['accounts_managed']}")
        
        print(f"\n💰 Capacidades Demonstradas:")
        print("   • Análise de demonstrações financeiras")
        print("   • Cálculo e interpretação de indicadores")
        print("   • Análise de tendências e valuation")
        print("   • Planejamento orçamentário")
        print("   • Controle e rolling forecast")
        print("   • Gestão de portfólio de investimentos")
        print("   • Estratégias de investimento")
        print("   • Análise de risco-retorno")
        print("   • Avaliação de riscos financeiros")
        print("   • Modelagem de risco (VaR, stress test)")
        print("   • Estratégias de mitigação")
        print("   • Planejamento financeiro estratégico")
        print("   • Projeções e cenários")
        print("   • Otimização de estrutura de capital")
        print("   • Gestão de tesouraria")
        print("   • Gestão de liquidez e câmbio")
        print("   • Otimização de funding")
        
    except Exception as e:
        print(f"❌ Erro durante demonstração financeira: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()