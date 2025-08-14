#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Análise de Documentos com Mangaba Agent
Demonstra processamento de diferentes tipos de documentos e extração de informações
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangaba_agent import MangabaAgent
from protocols.mcp import ContextType, ContextPriority
import json
from datetime import datetime

def demo_contract_analysis():
    """Demonstra análise de contratos"""
    print("📄 Análise de Contratos")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="contract_analyzer")
    
    # Exemplo de contrato
    contract_text = """
    CONTRATO DE PRESTAÇÃO DE SERVIÇOS
    
    CONTRATANTE: Empresa ABC Ltda., CNPJ 12.345.678/0001-90
    CONTRATADO: João Silva, CPF 123.456.789-00
    
    OBJETO: Desenvolvimento de sistema web
    PRAZO: 90 dias corridos a partir da assinatura
    VALOR: R$ 50.000,00 (cinquenta mil reais)
    
    PAGAMENTO: 30% na assinatura, 40% na entrega do protótipo, 30% na entrega final
    
    CLÁUSULA DE CONFIDENCIALIDADE: O contratado se compromete a manter sigilo
    sobre todas as informações confidenciais da contratante.
    
    MULTA POR ATRASO: 2% do valor total por dia de atraso na entrega.
    """
    
    print("📋 Analisando contrato...")
    
    # Análise estrutural
    analysis_prompt = f"""
    Analise o seguinte contrato e extraia as informações principais:
    
    {contract_text}
    
    Forneça:
    1. Partes envolvidas
    2. Objeto do contrato
    3. Valores e prazos
    4. Cláusulas importantes
    5. Riscos identificados
    """
    
    analysis = agent.chat(analysis_prompt, use_context=True)
    print(f"📊 Análise: {analysis}")
    
    # Verificação de compliance
    compliance_prompt = """
    Com base no contrato analisado, verifique:
    1. Se todas as cláusulas obrigatórias estão presentes
    2. Se os valores e prazos estão claramente definidos
    3. Se há cláusulas que podem gerar conflitos
    4. Sugestões de melhorias
    """
    
    compliance = agent.chat(compliance_prompt, use_context=True)
    print(f"✅ Compliance: {compliance}")
    
    return {"analysis": analysis, "compliance": compliance}

def demo_financial_report_analysis():
    """Demonstra análise de relatórios financeiros"""
    print("\n💰 Análise de Relatórios Financeiros")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="financial_analyzer")
    
    # Dados financeiros simulados
    financial_data = {
        "receitas": {
            "2023": 1500000,
            "2022": 1200000,
            "2021": 1000000
        },
        "despesas": {
            "2023": 1100000,
            "2022": 950000,
            "2021": 850000
        },
        "ativos": {
            "circulante": 800000,
            "nao_circulante": 2200000
        },
        "passivos": {
            "circulante": 400000,
            "nao_circulante": 1200000
        }
    }
    
    print("📈 Analisando dados financeiros...")
    
    # Análise de tendências
    trends_prompt = f"""
    Analise os seguintes dados financeiros e identifique tendências:
    
    {json.dumps(financial_data, indent=2)}
    
    Forneça:
    1. Análise de crescimento de receitas
    2. Evolução das despesas
    3. Margem de lucro por ano
    4. Situação patrimonial
    5. Indicadores de liquidez
    """
    
    trends = agent.chat(trends_prompt, use_context=True)
    print(f"📊 Tendências: {trends}")
    
    # Projeções
    projection_prompt = """
    Com base nos dados históricos analisados, faça projeções para 2024:
    1. Receita esperada
    2. Despesas projetadas
    3. Lucro estimado
    4. Recomendações estratégicas
    """
    
    projections = agent.chat(projection_prompt, use_context=True)
    print(f"🔮 Projeções: {projections}")
    
    return {"trends": trends, "projections": projections}

def demo_legal_document_review():
    """Demonstra revisão de documentos legais"""
    print("\n⚖️ Revisão de Documentos Legais")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="legal_reviewer")
    
    # Exemplo de termo de uso
    terms_text = """
    TERMOS DE USO - PLATAFORMA DIGITAL
    
    1. ACEITAÇÃO DOS TERMOS
    Ao utilizar nossa plataforma, você concorda com estes termos.
    
    2. USO PERMITIDO
    A plataforma destina-se apenas para uso pessoal e não comercial.
    
    3. PROPRIEDADE INTELECTUAL
    Todo conteúdo é protegido por direitos autorais.
    
    4. LIMITAÇÃO DE RESPONSABILIDADE
    Não nos responsabilizamos por danos diretos ou indiretos.
    
    5. MODIFICAÇÕES
    Podemos alterar estes termos a qualquer momento.
    
    6. LEI APLICÁVEL
    Estes termos são regidos pela lei brasileira.
    """
    
    print("📜 Revisando termos de uso...")
    
    # Análise legal
    legal_analysis_prompt = f"""
    Revise os seguintes termos de uso sob a perspectiva legal brasileira:
    
    {terms_text}
    
    Analise:
    1. Conformidade com a LGPD
    2. Conformidade com o CDC
    3. Cláusulas abusivas potenciais
    4. Lacunas importantes
    5. Sugestões de melhorias
    """
    
    legal_review = agent.chat(legal_analysis_prompt, use_context=True)
    print(f"⚖️ Revisão Legal: {legal_review}")
    
    # Sugestões de adequação
    compliance_prompt = """
    Com base na revisão legal, sugira adequações específicas para:
    1. Melhor proteção de dados pessoais
    2. Maior transparência para o usuário
    3. Redução de riscos legais
    4. Conformidade regulatória
    """
    
    compliance_suggestions = agent.chat(compliance_prompt, use_context=True)
    print(f"📋 Sugestões: {compliance_suggestions}")
    
    return {"legal_review": legal_review, "suggestions": compliance_suggestions}

def demo_research_paper_analysis():
    """Demonstra análise de artigos científicos"""
    print("\n🔬 Análise de Artigos Científicos")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="research_analyzer")
    
    # Resumo de artigo científico
    paper_abstract = """
    TÍTULO: Aplicação de Inteligência Artificial na Análise de Sentimentos em Redes Sociais
    
    RESUMO: Este estudo investiga a eficácia de algoritmos de aprendizado de máquina
    na análise de sentimentos de posts em redes sociais. Utilizamos um dataset de
    100.000 tweets coletados durante 6 meses, aplicando técnicas de processamento
    de linguagem natural (NLP) e redes neurais convolucionais (CNN). Os resultados
    mostram uma acurácia de 87% na classificação de sentimentos positivos, negativos
    e neutros. O modelo proposto supera métodos tradicionais em 12% na precisão.
    
    PALAVRAS-CHAVE: inteligência artificial, análise de sentimentos, redes sociais,
    processamento de linguagem natural, aprendizado de máquina
    
    METODOLOGIA: Coleta de dados via API do Twitter, pré-processamento com remoção
    de stopwords e normalização, treinamento de modelo CNN com validação cruzada.
    """
    
    print("📚 Analisando artigo científico...")
    
    # Análise metodológica
    methodology_prompt = f"""
    Analise a metodologia do seguinte artigo científico:
    
    {paper_abstract}
    
    Avalie:
    1. Rigor metodológico
    2. Tamanho e qualidade da amostra
    3. Técnicas utilizadas
    4. Validade dos resultados
    5. Limitações do estudo
    """
    
    methodology_analysis = agent.chat(methodology_prompt, use_context=True)
    print(f"🔍 Análise Metodológica: {methodology_analysis}")
    
    # Relevância e impacto
    impact_prompt = """
    Com base no artigo analisado, avalie:
    1. Relevância científica do tema
    2. Contribuição para o campo de estudo
    3. Aplicabilidade prática dos resultados
    4. Sugestões para pesquisas futuras
    5. Potencial de citação
    """
    
    impact_analysis = agent.chat(impact_prompt, use_context=True)
    print(f"📈 Análise de Impacto: {impact_analysis}")
    
    return {"methodology": methodology_analysis, "impact": impact_analysis}

def demo_technical_documentation_review():
    """Demonstra revisão de documentação técnica"""
    print("\n🛠️ Revisão de Documentação Técnica")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="tech_doc_reviewer")
    
    # Exemplo de documentação de API
    api_doc = """
    API DE PAGAMENTOS - DOCUMENTAÇÃO
    
    ENDPOINT: POST /api/v1/payments
    
    DESCRIÇÃO: Processa pagamentos via cartão de crédito
    
    PARÂMETROS:
    - amount (number, required): Valor do pagamento em centavos
    - currency (string, required): Código da moeda (BRL, USD)
    - card_token (string, required): Token do cartão
    - description (string, optional): Descrição do pagamento
    
    RESPOSTA DE SUCESSO (200):
    {
      "id": "pay_123456",
      "status": "approved",
      "amount": 10000,
      "currency": "BRL"
    }
    
    CÓDIGOS DE ERRO:
    - 400: Parâmetros inválidos
    - 401: Token de autenticação inválido
    - 402: Pagamento recusado
    - 500: Erro interno do servidor
    
    EXEMPLO DE USO:
    curl -X POST https://api.exemplo.com/v1/payments \
      -H "Authorization: Bearer TOKEN" \
      -d '{"amount": 10000, "currency": "BRL", "card_token": "card_123"}'
    """
    
    print("📖 Revisando documentação de API...")
    
    # Análise de completude
    completeness_prompt = f"""
    Revise a seguinte documentação de API:
    
    {api_doc}
    
    Analise:
    1. Completude das informações
    2. Clareza das instruções
    3. Exemplos práticos
    4. Tratamento de erros
    5. Informações de segurança
    """
    
    completeness_review = agent.chat(completeness_prompt, use_context=True)
    print(f"📋 Revisão de Completude: {completeness_review}")
    
    # Sugestões de melhoria
    improvement_prompt = """
    Com base na documentação analisada, sugira melhorias para:
    1. Facilitar a integração por desenvolvedores
    2. Reduzir dúvidas comuns
    3. Melhorar exemplos de código
    4. Adicionar informações de segurança
    5. Incluir casos de uso avançados
    """
    
    improvements = agent.chat(improvement_prompt, use_context=True)
    print(f"💡 Sugestões: {improvements}")
    
    return {"completeness": completeness_review, "improvements": improvements}

def demo_batch_document_processing():
    """Demonstra processamento em lote de documentos"""
    print("\n📦 Processamento em Lote de Documentos")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="batch_processor")
    
    # Simulação de múltiplos documentos
    documents = [
        {
            "id": "DOC001",
            "type": "invoice",
            "content": "Nota Fiscal 123 - Valor: R$ 1.500,00 - Vencimento: 30/12/2024"
        },
        {
            "id": "DOC002",
            "type": "contract",
            "content": "Contrato de Locação - Prazo: 12 meses - Valor: R$ 2.000,00/mês"
        },
        {
            "id": "DOC003",
            "type": "report",
            "content": "Relatório Mensal - Vendas: R$ 50.000,00 - Crescimento: 15%"
        },
        {
            "id": "DOC004",
            "type": "email",
            "content": "Proposta comercial - Desconto de 10% para pagamento à vista"
        }
    ]
    
    print(f"📄 Processando {len(documents)} documentos...")
    
    results = []
    
    for doc in documents:
        print(f"\n🔄 Processando {doc['id']} ({doc['type']})...")
        
        # Análise específica por tipo
        analysis_prompt = f"""
        Analise o seguinte documento do tipo '{doc['type']}':
        
        {doc['content']}
        
        Extraia:
        1. Informações principais
        2. Valores monetários
        3. Datas importantes
        4. Ações necessárias
        5. Prioridade de tratamento
        """
        
        analysis = agent.chat(analysis_prompt, use_context=True)
        
        result = {
            "document_id": doc['id'],
            "type": doc['type'],
            "analysis": analysis,
            "processed_at": datetime.now().isoformat()
        }
        
        results.append(result)
        print(f"✅ {doc['id']} processado")
    
    # Relatório consolidado
    consolidation_prompt = f"""
    Com base no processamento de {len(documents)} documentos, gere um relatório consolidado:
    
    Documentos processados: {[r['document_id'] for r in results]}
    
    Inclua:
    1. Resumo executivo
    2. Documentos por prioridade
    3. Ações recomendadas
    4. Próximos passos
    """
    
    consolidated_report = agent.chat(consolidation_prompt, use_context=True)
    print(f"\n📊 Relatório Consolidado: {consolidated_report}")
    
    return {
        "processed_documents": len(results),
        "results": results,
        "consolidated_report": consolidated_report
    }

def main():
    """Executa demonstração completa de análise de documentos"""
    print("📄 Mangaba Agent - Análise de Documentos")
    print("=" * 60)
    
    try:
        # Diferentes tipos de análise
        contract_result = demo_contract_analysis()
        financial_result = demo_financial_report_analysis()
        legal_result = demo_legal_document_review()
        research_result = demo_research_paper_analysis()
        tech_doc_result = demo_technical_documentation_review()
        batch_result = demo_batch_document_processing()
        
        print("\n🎉 DEMONSTRAÇÃO DE ANÁLISE COMPLETA!")
        print("=" * 50)
        
        print("\n📊 Resumo dos Resultados:")
        print(f"   📋 Contratos analisados: 1")
        print(f"   💰 Relatórios financeiros: 1")
        print(f"   ⚖️ Documentos legais: 1")
        print(f"   🔬 Artigos científicos: 1")
        print(f"   🛠️ Documentação técnica: 1")
        print(f"   📦 Processamento em lote: {batch_result['processed_documents']} documentos")
        
        print("\n🚀 Capacidades Demonstradas:")
        print("   • Análise contextual de contratos")
        print("   • Interpretação de dados financeiros")
        print("   • Revisão legal e compliance")
        print("   • Avaliação de pesquisa científica")
        print("   • Revisão de documentação técnica")
        print("   • Processamento em lote eficiente")
        print("   • Extração de informações estruturadas")
        print("   • Geração de relatórios consolidados")
        
    except Exception as e:
        print(f"❌ Erro durante demonstração: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()