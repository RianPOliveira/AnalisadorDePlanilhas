#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Automação de Tarefas com Mangaba Agent
Demonstra automação de workflows, tarefas recorrentes e processos empresariais
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangaba_agent import MangabaAgent
from protocols.mcp import ContextType, ContextPriority
import json
import time
from datetime import datetime, timedelta
import random

class TaskScheduler:
    """Agendador de tarefas automatizadas"""
    
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []
        self.agent = MangabaAgent(agent_id="task_scheduler")
    
    def add_task(self, task_id, description, priority="medium", due_date=None):
        """Adiciona nova tarefa"""
        task = {
            "id": task_id,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "created_at": datetime.now().isoformat(),
            "status": "pending"
        }
        self.tasks.append(task)
        
        # Adiciona ao contexto do agente
        self.agent.chat(
            f"Nova tarefa adicionada: {json.dumps(task)}",
            use_context=True
        )
        
        return task
    
    def execute_task(self, task_id):
        """Executa uma tarefa específica"""
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if not task:
            return {"error": "Tarefa não encontrada"}
        
        # Simula execução da tarefa
        execution_prompt = f"""
        Execute a seguinte tarefa:
        
        ID: {task['id']}
        Descrição: {task['description']}
        Prioridade: {task['priority']}
        
        Forneça:
        1. Passos executados
        2. Resultado obtido
        3. Tempo estimado
        4. Status final
        """
        
        result = self.agent.chat(execution_prompt, use_context=True)
        
        # Atualiza status da tarefa
        task['status'] = 'completed'
        task['completed_at'] = datetime.now().isoformat()
        task['result'] = result
        
        # Move para lista de concluídas
        self.tasks.remove(task)
        self.completed_tasks.append(task)
        
        return task
    
    def get_pending_tasks(self):
        """Retorna tarefas pendentes"""
        return [t for t in self.tasks if t['status'] == 'pending']
    
    def get_task_summary(self):
        """Retorna resumo das tarefas"""
        return {
            "pending": len(self.tasks),
            "completed": len(self.completed_tasks),
            "total": len(self.tasks) + len(self.completed_tasks)
        }

def demo_email_automation():
    """Demonstra automação de emails"""
    print("📧 Automação de Emails")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="email_automator")
    
    # Cenários de email
    email_scenarios = [
        {
            "type": "welcome",
            "recipient": "novo.cliente@email.com",
            "context": "Cliente se cadastrou hoje"
        },
        {
            "type": "follow_up",
            "recipient": "cliente.ativo@email.com",
            "context": "Última compra há 30 dias"
        },
        {
            "type": "reminder",
            "recipient": "cliente.carrinho@email.com",
            "context": "Carrinho abandonado há 2 dias"
        }
    ]
    
    automated_emails = []
    
    for scenario in email_scenarios:
        print(f"\n📨 Processando email {scenario['type']}...")
        
        email_prompt = f"""
        Crie um email automatizado para o cenário:
        
        Tipo: {scenario['type']}
        Destinatário: {scenario['recipient']}
        Contexto: {scenario['context']}
        
        Gere:
        1. Assunto atrativo
        2. Corpo do email personalizado
        3. Call-to-action apropriado
        4. Tom adequado ao contexto
        """
        
        email_content = agent.chat(email_prompt, use_context=True)
        
        automated_email = {
            "scenario": scenario,
            "content": email_content,
            "generated_at": datetime.now().isoformat(),
            "status": "ready_to_send"
        }
        
        automated_emails.append(automated_email)
        print(f"✅ Email {scenario['type']} gerado")
    
    # Análise de efetividade
    effectiveness_prompt = f"""
    Analise a efetividade dos {len(automated_emails)} emails gerados:
    
    Tipos: {[e['scenario']['type'] for e in automated_emails]}
    
    Avalie:
    1. Personalização adequada
    2. Timing apropriado
    3. Potencial de conversão
    4. Melhorias sugeridas
    """
    
    effectiveness = agent.chat(effectiveness_prompt, use_context=True)
    print(f"\n📊 Análise de Efetividade: {effectiveness}")
    
    return {
        "emails_generated": len(automated_emails),
        "emails": automated_emails,
        "effectiveness_analysis": effectiveness
    }

def demo_report_generation():
    """Demonstra geração automática de relatórios"""
    print("\n📊 Geração Automática de Relatórios")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="report_generator")
    
    # Dados simulados para relatório
    business_data = {
        "sales": {
            "current_month": 150000,
            "previous_month": 135000,
            "target": 160000
        },
        "customers": {
            "new_customers": 45,
            "returning_customers": 120,
            "churn_rate": 0.05
        },
        "products": {
            "top_selling": ["Produto A", "Produto B", "Produto C"],
            "inventory_low": ["Produto X", "Produto Y"]
        },
        "marketing": {
            "campaign_roi": 3.2,
            "conversion_rate": 0.08,
            "cost_per_acquisition": 25.50
        }
    }
    
    print("📈 Gerando relatório executivo...")
    
    # Geração de relatório executivo
    executive_report_prompt = f"""
    Gere um relatório executivo com base nos seguintes dados:
    
    {json.dumps(business_data, indent=2)}
    
    O relatório deve incluir:
    1. Resumo executivo
    2. Principais métricas
    3. Análise de performance
    4. Tendências identificadas
    5. Recomendações estratégicas
    6. Próximos passos
    
    Formato: Profissional e objetivo
    """
    
    executive_report = agent.chat(executive_report_prompt, use_context=True)
    print(f"📋 Relatório Executivo: {executive_report}")
    
    # Geração de relatório operacional
    print("\n🔧 Gerando relatório operacional...")
    
    operational_report_prompt = """
    Com base nos mesmos dados, gere um relatório operacional detalhado:
    
    1. Análise detalhada de vendas
    2. Performance por produto
    3. Análise de clientes
    4. Eficiência de marketing
    5. Alertas operacionais
    6. Ações corretivas necessárias
    
    Formato: Técnico e detalhado
    """
    
    operational_report = agent.chat(operational_report_prompt, use_context=True)
    print(f"🔧 Relatório Operacional: {operational_report}")
    
    return {
        "executive_report": executive_report,
        "operational_report": operational_report,
        "data_processed": business_data
    }

def demo_customer_service_automation():
    """Demonstra automação de atendimento ao cliente"""
    print("\n🎧 Automação de Atendimento ao Cliente")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="customer_service_bot")
    
    # Simulação de tickets de suporte
    support_tickets = [
        {
            "id": "TICKET001",
            "customer": "João Silva",
            "issue": "Não consigo fazer login na minha conta",
            "priority": "medium",
            "category": "technical"
        },
        {
            "id": "TICKET002",
            "customer": "Maria Santos",
            "issue": "Cobrança indevida no meu cartão",
            "priority": "high",
            "category": "billing"
        },
        {
            "id": "TICKET003",
            "customer": "Pedro Costa",
            "issue": "Como cancelar minha assinatura?",
            "priority": "low",
            "category": "account"
        }
    ]
    
    resolved_tickets = []
    
    for ticket in support_tickets:
        print(f"\n🎫 Processando {ticket['id']}...")
        
        # Análise e resolução automática
        resolution_prompt = f"""
        Analise e resolva o seguinte ticket de suporte:
        
        ID: {ticket['id']}
        Cliente: {ticket['customer']}
        Problema: {ticket['issue']}
        Prioridade: {ticket['priority']}
        Categoria: {ticket['category']}
        
        Forneça:
        1. Análise do problema
        2. Solução proposta
        3. Passos para o cliente
        4. Tempo estimado de resolução
        5. Necessidade de escalação
        """
        
        resolution = agent.chat(resolution_prompt, use_context=True)
        
        resolved_ticket = {
            **ticket,
            "resolution": resolution,
            "resolved_at": datetime.now().isoformat(),
            "status": "resolved"
        }
        
        resolved_tickets.append(resolved_ticket)
        print(f"✅ {ticket['id']} resolvido")
    
    # Análise de qualidade do atendimento
    quality_analysis_prompt = f"""
    Analise a qualidade do atendimento automatizado:
    
    Tickets processados: {len(resolved_tickets)}
    Categorias: {list(set(t['category'] for t in support_tickets))}
    
    Avalie:
    1. Eficácia das resoluções
    2. Tempo de resposta
    3. Satisfação esperada do cliente
    4. Casos que precisam de escalação
    5. Melhorias no processo
    """
    
    quality_analysis = agent.chat(quality_analysis_prompt, use_context=True)
    print(f"\n📊 Análise de Qualidade: {quality_analysis}")
    
    return {
        "tickets_resolved": len(resolved_tickets),
        "resolutions": resolved_tickets,
        "quality_analysis": quality_analysis
    }

def demo_inventory_management():
    """Demonstra automação de gestão de estoque"""
    print("\n📦 Automação de Gestão de Estoque")
    print("=" * 40)
    
    agent = MangabaAgent(agent_id="inventory_manager")
    
    # Dados de estoque simulados
    inventory_data = {
        "products": [
            {"id": "PROD001", "name": "Notebook Dell", "current_stock": 5, "min_stock": 10, "max_stock": 50},
            {"id": "PROD002", "name": "Mouse Logitech", "current_stock": 25, "min_stock": 20, "max_stock": 100},
            {"id": "PROD003", "name": "Teclado Mecânico", "current_stock": 2, "min_stock": 15, "max_stock": 60},
            {"id": "PROD004", "name": "Monitor 24\"", "current_stock": 45, "min_stock": 10, "max_stock": 40}
        ],
        "sales_velocity": {
            "PROD001": 2.5,  # unidades por dia
            "PROD002": 5.0,
            "PROD003": 3.2,
            "PROD004": 1.8
        }
    }
    
    print("📊 Analisando níveis de estoque...")
    
    # Análise de estoque
    inventory_analysis_prompt = f"""
    Analise os seguintes dados de estoque:
    
    {json.dumps(inventory_data, indent=2)}
    
    Identifique:
    1. Produtos com estoque baixo
    2. Produtos com excesso de estoque
    3. Necessidades de reposição
    4. Previsão de ruptura
    5. Otimizações recomendadas
    """
    
    inventory_analysis = agent.chat(inventory_analysis_prompt, use_context=True)
    print(f"📈 Análise: {inventory_analysis}")
    
    # Geração automática de pedidos
    print("\n🛒 Gerando pedidos de reposição...")
    
    reorder_prompt = """
    Com base na análise de estoque, gere pedidos de reposição automáticos:
    
    Para cada produto que precisa de reposição:
    1. Quantidade a pedir
    2. Justificativa
    3. Prioridade do pedido
    4. Fornecedor sugerido
    5. Prazo de entrega esperado
    """
    
    reorder_suggestions = agent.chat(reorder_prompt, use_context=True)
    print(f"🛒 Sugestões de Pedidos: {reorder_suggestions}")
    
    return {
        "products_analyzed": len(inventory_data['products']),
        "inventory_analysis": inventory_analysis,
        "reorder_suggestions": reorder_suggestions
    }

def demo_workflow_orchestration():
    """Demonstra orquestração de workflows complexos"""
    print("\n🔄 Orquestração de Workflows")
    print("=" * 40)
    
    # Cria agentes especializados
    orchestrator = MangabaAgent(agent_id="workflow_orchestrator")
    data_processor = MangabaAgent(agent_id="data_processor")
    quality_checker = MangabaAgent(agent_id="quality_checker")
    notifier = MangabaAgent(agent_id="notifier")
    
    # Workflow: Processamento de pedido
    order_data = {
        "order_id": "ORD12345",
        "customer": "Empresa XYZ",
        "items": [
            {"product": "Notebook", "quantity": 10, "price": 2500.00},
            {"product": "Mouse", "quantity": 15, "price": 50.00}
        ],
        "total": 25750.00,
        "payment_method": "credit_card"
    }
    
    print(f"🚀 Iniciando workflow para pedido {order_data['order_id']}...")
    
    # Etapa 1: Orquestrador inicia processo
    orchestration_prompt = f"""
    Inicie o workflow de processamento do pedido:
    
    {json.dumps(order_data, indent=2)}
    
    Defina:
    1. Sequência de etapas
    2. Responsáveis por cada etapa
    3. Critérios de validação
    4. Pontos de controle
    5. Ações em caso de erro
    """
    
    workflow_plan = orchestrator.chat(orchestration_prompt, use_context=True)
    print(f"📋 Plano do Workflow: {workflow_plan}")
    
    # Etapa 2: Processamento de dados
    print("\n🔄 Etapa 2: Processamento de dados...")
    
    data_processing_prompt = f"""
    Processe os dados do pedido:
    
    {json.dumps(order_data, indent=2)}
    
    Execute:
    1. Validação de dados
    2. Cálculo de impostos
    3. Verificação de disponibilidade
    4. Reserva de estoque
    5. Preparação para faturamento
    """
    
    processing_result = data_processor.chat(data_processing_prompt, use_context=True)
    print(f"⚙️ Resultado do Processamento: {processing_result}")
    
    # Etapa 3: Controle de qualidade
    print("\n✅ Etapa 3: Controle de qualidade...")
    
    quality_check_prompt = """
    Execute controle de qualidade no processamento:
    
    Verifique:
    1. Integridade dos dados
    2. Conformidade com regras de negócio
    3. Cálculos corretos
    4. Disponibilidade confirmada
    5. Aprovação para prosseguir
    """
    
    quality_result = quality_checker.chat(quality_check_prompt, use_context=True)
    print(f"🔍 Resultado da Qualidade: {quality_result}")
    
    # Etapa 4: Notificações
    print("\n📢 Etapa 4: Notificações...")
    
    notification_prompt = f"""
    Gere notificações apropriadas para o pedido {order_data['order_id']}:
    
    Crie notificações para:
    1. Cliente (confirmação do pedido)
    2. Estoque (reserva de produtos)
    3. Financeiro (cobrança)
    4. Logística (preparação para envio)
    5. Gerência (relatório de status)
    """
    
    notifications = notifier.chat(notification_prompt, use_context=True)
    print(f"📧 Notificações: {notifications}")
    
    # Finalização do workflow
    completion_prompt = f"""
    Finalize o workflow do pedido {order_data['order_id']}:
    
    Resumo das etapas executadas:
    1. Planejamento: Concluído
    2. Processamento: Concluído
    3. Qualidade: Aprovado
    4. Notificações: Enviadas
    
    Gere:
    1. Status final do workflow
    2. Próximas ações
    3. Métricas de performance
    4. Lições aprendidas
    """
    
    workflow_completion = orchestrator.chat(completion_prompt, use_context=True)
    print(f"\n🎯 Finalização: {workflow_completion}")
    
    return {
        "order_id": order_data['order_id'],
        "workflow_steps": 4,
        "agents_involved": 4,
        "status": "completed",
        "completion_summary": workflow_completion
    }

def main():
    """Executa demonstração completa de automação"""
    print("🤖 Mangaba Agent - Automação de Tarefas")
    print("=" * 60)
    
    try:
        # Demonstração de agendador de tarefas
        print("\n⏰ Demonstração do Agendador de Tarefas")
        print("-" * 40)
        
        scheduler = TaskScheduler()
        
        # Adiciona tarefas
        scheduler.add_task("TASK001", "Gerar relatório mensal", "high")
        scheduler.add_task("TASK002", "Backup do banco de dados", "medium")
        scheduler.add_task("TASK003", "Atualizar documentação", "low")
        
        print(f"📋 Tarefas adicionadas: {scheduler.get_task_summary()['total']}")
        
        # Executa tarefas
        for task in scheduler.get_pending_tasks():
            result = scheduler.execute_task(task['id'])
            print(f"✅ {task['id']}: {result['status']}")
        
        # Outras demonstrações
        email_result = demo_email_automation()
        report_result = demo_report_generation()
        service_result = demo_customer_service_automation()
        inventory_result = demo_inventory_management()
        workflow_result = demo_workflow_orchestration()
        
        print("\n🎉 DEMONSTRAÇÃO DE AUTOMAÇÃO COMPLETA!")
        print("=" * 50)
        
        print("\n📊 Resumo dos Resultados:")
        print(f"   ⏰ Tarefas executadas: {scheduler.get_task_summary()['completed']}")
        print(f"   📧 Emails automatizados: {email_result['emails_generated']}")
        print(f"   📊 Relatórios gerados: 2")
        print(f"   🎧 Tickets resolvidos: {service_result['tickets_resolved']}")
        print(f"   📦 Produtos analisados: {inventory_result['products_analyzed']}")
        print(f"   🔄 Workflows orquestrados: 1")
        
        print("\n🚀 Capacidades Demonstradas:")
        print("   • Agendamento inteligente de tarefas")
        print("   • Automação de comunicações")
        print("   • Geração automática de relatórios")
        print("   • Atendimento ao cliente automatizado")
        print("   • Gestão inteligente de estoque")
        print("   • Orquestração de workflows complexos")
        print("   • Coordenação entre múltiplos agentes")
        print("   • Tomada de decisão automatizada")
        
    except Exception as e:
        print(f"❌ Erro durante demonstração de automação: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()