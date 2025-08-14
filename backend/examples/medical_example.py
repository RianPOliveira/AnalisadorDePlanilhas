#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Medicina com Mangaba Agent
Demonstra aplicações de IA em diagnóstico, análise médica e gestão hospitalar
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangaba_agent import MangabaAgent
from protocols.mcp import ContextType, ContextPriority
import json
import random
from datetime import datetime, timedelta

class MedicalDataGenerator:
    """Gerador de dados médicos sintéticos"""
    
    @staticmethod
    def generate_patient_data():
        """Gera dados de pacientes para análise"""
        patients = [
            {
                "patient_id": "PAC_001",
                "name": "João Silva",
                "age": 45,
                "gender": "Masculino",
                "weight": 78.5,
                "height": 175,
                "bmi": 25.6,
                "blood_type": "O+",
                "allergies": ["Penicilina", "Frutos do mar"],
                "chronic_conditions": ["Hipertensão", "Diabetes tipo 2"],
                "current_medications": [
                    {"name": "Losartana", "dosage": "50mg", "frequency": "1x/dia"},
                    {"name": "Metformina", "dosage": "850mg", "frequency": "2x/dia"}
                ],
                "vital_signs": {
                    "blood_pressure": "140/90",
                    "heart_rate": 78,
                    "temperature": 36.5,
                    "oxygen_saturation": 98,
                    "respiratory_rate": 16
                },
                "last_visit": "2024-11-10",
                "risk_factors": ["Sedentarismo", "Histórico familiar de DCV"]
            },
            {
                "patient_id": "PAC_002",
                "name": "Maria Santos",
                "age": 32,
                "gender": "Feminino",
                "weight": 65.0,
                "height": 162,
                "bmi": 24.8,
                "blood_type": "A+",
                "allergies": ["Látex"],
                "chronic_conditions": ["Asma"],
                "current_medications": [
                    {"name": "Salbutamol", "dosage": "100mcg", "frequency": "SOS"}
                ],
                "vital_signs": {
                    "blood_pressure": "110/70",
                    "heart_rate": 72,
                    "temperature": 36.8,
                    "oxygen_saturation": 97,
                    "respiratory_rate": 18
                },
                "last_visit": "2024-11-15",
                "risk_factors": ["Exposição a alérgenos"]
            },
            {
                "patient_id": "PAC_003",
                "name": "Carlos Oliveira",
                "age": 67,
                "gender": "Masculino",
                "weight": 85.2,
                "height": 170,
                "bmi": 29.5,
                "blood_type": "B-",
                "allergies": [],
                "chronic_conditions": ["Artrite reumatoide", "Osteoporose"],
                "current_medications": [
                    {"name": "Metotrexato", "dosage": "15mg", "frequency": "1x/semana"},
                    {"name": "Ácido fólico", "dosage": "5mg", "frequency": "1x/semana"},
                    {"name": "Cálcio + Vitamina D", "dosage": "600mg", "frequency": "1x/dia"}
                ],
                "vital_signs": {
                    "blood_pressure": "130/85",
                    "heart_rate": 68,
                    "temperature": 36.2,
                    "oxygen_saturation": 96,
                    "respiratory_rate": 14
                },
                "last_visit": "2024-11-08",
                "risk_factors": ["Idade avançada", "Imobilidade"]
            }
        ]
        return patients
    
    @staticmethod
    def generate_lab_results():
        """Gera resultados de exames laboratoriais"""
        lab_results = [
            {
                "patient_id": "PAC_001",
                "test_date": "2024-11-10",
                "tests": {
                    "hemograma": {
                        "hemoglobina": {"value": 13.5, "unit": "g/dL", "reference": "12.0-15.5", "status": "Normal"},
                        "hematocrito": {"value": 40.2, "unit": "%", "reference": "36-46", "status": "Normal"},
                        "leucocitos": {"value": 7200, "unit": "/mm³", "reference": "4000-11000", "status": "Normal"},
                        "plaquetas": {"value": 280000, "unit": "/mm³", "reference": "150000-450000", "status": "Normal"}
                    },
                    "bioquimica": {
                        "glicemia_jejum": {"value": 145, "unit": "mg/dL", "reference": "70-99", "status": "Elevado"},
                        "hba1c": {"value": 8.2, "unit": "%", "reference": "<7.0", "status": "Elevado"},
                        "colesterol_total": {"value": 220, "unit": "mg/dL", "reference": "<200", "status": "Elevado"},
                        "hdl": {"value": 35, "unit": "mg/dL", "reference": ">40", "status": "Baixo"},
                        "ldl": {"value": 150, "unit": "mg/dL", "reference": "<100", "status": "Elevado"},
                        "triglicerides": {"value": 180, "unit": "mg/dL", "reference": "<150", "status": "Elevado"},
                        "creatinina": {"value": 1.1, "unit": "mg/dL", "reference": "0.7-1.3", "status": "Normal"},
                        "ureia": {"value": 35, "unit": "mg/dL", "reference": "15-45", "status": "Normal"}
                    }
                }
            },
            {
                "patient_id": "PAC_002",
                "test_date": "2024-11-15",
                "tests": {
                    "hemograma": {
                        "hemoglobina": {"value": 12.8, "unit": "g/dL", "reference": "12.0-15.5", "status": "Normal"},
                        "hematocrito": {"value": 38.5, "unit": "%", "reference": "36-46", "status": "Normal"},
                        "leucocitos": {"value": 9500, "unit": "/mm³", "reference": "4000-11000", "status": "Normal"},
                        "eosinofilos": {"value": 8, "unit": "%", "reference": "1-4", "status": "Elevado"}
                    },
                    "imunologia": {
                        "ige_total": {"value": 450, "unit": "UI/mL", "reference": "<100", "status": "Elevado"},
                        "ige_especifica_acaro": {"value": 25.5, "unit": "kUA/L", "reference": "<0.35", "status": "Positivo"},
                        "ige_especifica_polen": {"value": 12.8, "unit": "kUA/L", "reference": "<0.35", "status": "Positivo"}
                    }
                }
            },
            {
                "patient_id": "PAC_003",
                "test_date": "2024-11-08",
                "tests": {
                    "reumatologia": {
                        "pcr": {"value": 15.2, "unit": "mg/L", "reference": "<3.0", "status": "Elevado"},
                        "vhs": {"value": 45, "unit": "mm/h", "reference": "<20", "status": "Elevado"},
                        "fator_reumatoide": {"value": 180, "unit": "UI/mL", "reference": "<20", "status": "Positivo"},
                        "anti_ccp": {"value": 85, "unit": "U/mL", "reference": "<20", "status": "Positivo"}
                    },
                    "metabolismo_osseo": {
                        "vitamina_d": {"value": 18, "unit": "ng/mL", "reference": "30-100", "status": "Baixo"},
                        "pth": {"value": 65, "unit": "pg/mL", "reference": "15-65", "status": "Normal"},
                        "calcio": {"value": 9.2, "unit": "mg/dL", "reference": "8.5-10.5", "status": "Normal"}
                    }
                }
            }
        ]
        return lab_results
    
    @staticmethod
    def generate_imaging_data():
        """Gera dados de exames de imagem"""
        imaging_studies = [
            {
                "patient_id": "PAC_001",
                "study_date": "2024-11-12",
                "study_type": "Ecocardiograma",
                "findings": {
                    "left_ventricle": "Hipertrofia concêntrica leve",
                    "ejection_fraction": "60%",
                    "valves": "Insuficiência mitral leve",
                    "conclusion": "Alterações compatíveis com hipertensão arterial"
                },
                "radiologist": "Dr. Pedro Cardoso",
                "urgency": "Rotina"
            },
            {
                "patient_id": "PAC_002",
                "study_date": "2024-11-16",
                "study_type": "Tomografia de Tórax",
                "findings": {
                    "lungs": "Espessamento brônquico bilateral",
                    "pleura": "Sem alterações",
                    "mediastinum": "Linfonodos hilares aumentados",
                    "conclusion": "Achados compatíveis com asma brônquica"
                },
                "radiologist": "Dra. Ana Pulmonar",
                "urgency": "Rotina"
            },
            {
                "patient_id": "PAC_003",
                "study_date": "2024-11-09",
                "study_type": "Densitometria Óssea",
                "findings": {
                    "lumbar_spine": "T-score: -2.8 (Osteoporose)",
                    "femoral_neck": "T-score: -2.5 (Osteoporose)",
                    "total_hip": "T-score: -2.2 (Osteopenia)",
                    "conclusion": "Osteoporose em coluna lombar e colo femoral"
                },
                "radiologist": "Dr. Marcos Ósseo",
                "urgency": "Rotina"
            }
        ]
        return imaging_studies

def demo_diagnostic_assistance():
    """Demonstra assistência diagnóstica"""
    print("🩺 Assistência Diagnóstica")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="diagnostic_assistant")
    
    # Gera dados de pacientes
    patients = MedicalDataGenerator.generate_patient_data()
    lab_results = MedicalDataGenerator.generate_lab_results()
    
    print(f"👥 Analisando {len(patients)} pacientes...")
    
    # Análise diagnóstica
    diagnostic_prompt = f"""
    Analise os dados clínicos dos pacientes:
    
    PACIENTES:
    {json.dumps(patients, indent=2)}
    
    EXAMES LABORATORIAIS:
    {json.dumps(lab_results, indent=2)}
    
    Para cada paciente, forneça:
    1. Análise dos sinais vitais
    2. Interpretação dos exames laboratoriais
    3. Correlação clínico-laboratorial
    4. Hipóteses diagnósticas
    5. Exames complementares sugeridos
    6. Monitoramento recomendado
    """
    
    diagnostic_analysis = agent.chat(diagnostic_prompt, use_context=True)
    print(f"🔍 Análise Diagnóstica: {diagnostic_analysis}")
    
    # Avaliação de risco
    risk_assessment_prompt = """
    Avalie os fatores de risco de cada paciente:
    
    1. Risco cardiovascular
    2. Risco de complicações diabéticas
    3. Risco de exacerbação de asma
    4. Risco de fraturas
    5. Interações medicamentosas
    6. Estratificação de risco global
    """
    
    risk_assessment = agent.chat(risk_assessment_prompt, use_context=True)
    print(f"⚠️ Avaliação de Risco: {risk_assessment}")
    
    # Recomendações terapêuticas
    treatment_recommendations_prompt = """
    Sugira recomendações terapêuticas:
    
    1. Ajustes medicamentosos
    2. Mudanças no estilo de vida
    3. Frequência de consultas
    4. Metas terapêuticas
    5. Educação do paciente
    6. Prevenção de complicações
    """
    
    treatment_recommendations = agent.chat(treatment_recommendations_prompt, use_context=True)
    print(f"\n💊 Recomendações Terapêuticas: {treatment_recommendations}")
    
    return {
        "patients_analyzed": len(patients),
        "diagnostic_analysis": diagnostic_analysis,
        "risk_assessment": risk_assessment,
        "treatment_recommendations": treatment_recommendations
    }

def demo_clinical_decision_support():
    """Demonstra suporte à decisão clínica"""
    print("\n🧠 Suporte à Decisão Clínica")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="clinical_decision_support")
    
    # Simula casos clínicos complexos
    clinical_cases = [
        {
            "case_id": "CASO_001",
            "chief_complaint": "Dor torácica há 2 horas",
            "patient_age": 55,
            "gender": "Masculino",
            "symptoms": ["Dor precordial", "Sudorese", "Náusea", "Dispneia"],
            "vital_signs": {"BP": "160/100", "HR": 95, "RR": 20, "O2Sat": 96},
            "ecg_findings": "Supradesnivelamento de ST em V2-V6",
            "troponin": "Elevada (0.8 ng/mL)",
            "risk_factors": ["Tabagismo", "Hipertensão", "Dislipidemia"]
        },
        {
            "case_id": "CASO_002",
            "chief_complaint": "Febre e tosse há 5 dias",
            "patient_age": 28,
            "gender": "Feminino",
            "symptoms": ["Febre 38.5°C", "Tosse produtiva", "Dor pleurítica", "Fadiga"],
            "vital_signs": {"BP": "110/70", "HR": 88, "RR": 22, "O2Sat": 94},
            "chest_xray": "Consolidação em lobo inferior direito",
            "lab_results": {"WBC": "15000", "CRP": "120 mg/L", "PCT": "2.5 ng/mL"},
            "risk_factors": ["Nenhum"]
        }
    ]
    
    print(f"📋 Analisando {len(clinical_cases)} casos clínicos...")
    
    # Análise de casos
    case_analysis_prompt = f"""
    Analise os seguintes casos clínicos:
    
    {json.dumps(clinical_cases, indent=2)}
    
    Para cada caso, forneça:
    1. Diagnóstico diferencial
    2. Diagnóstico mais provável
    3. Urgência do caso
    4. Próximos passos diagnósticos
    5. Tratamento inicial
    6. Critérios de internação
    """
    
    case_analysis = agent.chat(case_analysis_prompt, use_context=True)
    print(f"📊 Análise de Casos: {case_analysis}")
    
    # Protocolos clínicos
    protocol_guidance_prompt = """
    Aplique protocolos clínicos relevantes:
    
    1. Protocolo de síndrome coronariana aguda
    2. Protocolo de pneumonia adquirida na comunidade
    3. Escores de risco (GRACE, CURB-65)
    4. Guidelines de tratamento
    5. Critérios de alta hospitalar
    6. Follow-up recomendado
    """
    
    protocol_guidance = agent.chat(protocol_guidance_prompt, use_context=True)
    print(f"📋 Orientação por Protocolos: {protocol_guidance}")
    
    # Alertas de segurança
    safety_alerts_prompt = """
    Identifique alertas de segurança:
    
    1. Sinais de alarme
    2. Contraindicações medicamentosas
    3. Alergias e interações
    4. Monitoramento necessário
    5. Complicações potenciais
    6. Quando reavaliar
    """
    
    safety_alerts = agent.chat(safety_alerts_prompt, use_context=True)
    print(f"\n🚨 Alertas de Segurança: {safety_alerts}")
    
    return {
        "cases_analyzed": len(clinical_cases),
        "case_analysis": case_analysis,
        "protocol_guidance": protocol_guidance,
        "safety_alerts": safety_alerts
    }

def demo_patient_monitoring():
    """Demonstra monitoramento de pacientes"""
    print("\n📊 Monitoramento de Pacientes")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="patient_monitor")
    
    # Simula dados de monitoramento
    monitoring_data = [
        {
            "patient_id": "PAC_001",
            "monitoring_type": "Diabetes",
            "parameters": {
                "glucose_readings": [145, 180, 165, 155, 170, 160, 175],
                "hba1c_trend": [8.5, 8.2, 8.0],
                "medication_adherence": 85,
                "lifestyle_score": 60,
                "complications_risk": "Alto"
            },
            "alerts": ["Glicemia persistentemente elevada", "HbA1c acima da meta"]
        },
        {
            "patient_id": "PAC_002",
            "monitoring_type": "Asma",
            "parameters": {
                "peak_flow_readings": [380, 360, 340, 320, 300, 280, 260],
                "symptom_score": [2, 3, 4, 5, 6, 7, 8],
                "medication_usage": {"rescue_inhaler": 8, "controller": 90},
                "trigger_exposure": ["Ácaros", "Polen", "Exercício"],
                "exacerbation_risk": "Moderado"
            },
            "alerts": ["Declínio do peak flow", "Aumento do uso de broncodilatador"]
        },
        {
            "patient_id": "PAC_003",
            "monitoring_type": "Artrite Reumatoide",
            "parameters": {
                "das28_score": [5.2, 4.8, 4.5, 4.2],
                "morning_stiffness": [120, 90, 75, 60],
                "joint_count": {"swollen": 8, "tender": 12},
                "inflammatory_markers": {"CRP": 15.2, "ESR": 45},
                "functional_status": "Moderadamente limitado"
            },
            "alerts": ["Atividade da doença moderada", "Resposta parcial ao tratamento"]
        }
    ]
    
    print(f"📈 Monitorando {len(monitoring_data)} pacientes...")
    
    # Análise de tendências
    trend_analysis_prompt = f"""
    Analise as tendências de monitoramento:
    
    {json.dumps(monitoring_data, indent=2)}
    
    Para cada paciente, avalie:
    1. Tendências dos parâmetros clínicos
    2. Controle da doença
    3. Aderência ao tratamento
    4. Fatores de risco emergentes
    5. Necessidade de ajustes terapêuticos
    6. Prognóstico a curto prazo
    """
    
    trend_analysis = agent.chat(trend_analysis_prompt, use_context=True)
    print(f"📈 Análise de Tendências: {trend_analysis}")
    
    # Sistema de alertas
    alert_system_prompt = """
    Configure sistema de alertas personalizados:
    
    1. Alertas críticos (ação imediata)
    2. Alertas de atenção (revisão em 24h)
    3. Alertas informativos (próxima consulta)
    4. Thresholds personalizados
    5. Escalação automática
    6. Notificações para pacientes
    """
    
    alert_system = agent.chat(alert_system_prompt, use_context=True)
    print(f"🚨 Sistema de Alertas: {alert_system}")
    
    # Planos de cuidado
    care_plans_prompt = """
    Desenvolva planos de cuidado personalizados:
    
    1. Metas terapêuticas específicas
    2. Cronograma de monitoramento
    3. Educação do paciente
    4. Autocuidado e automonitoramento
    5. Suporte familiar
    6. Recursos comunitários
    """
    
    care_plans = agent.chat(care_plans_prompt, use_context=True)
    print(f"\n📋 Planos de Cuidado: {care_plans}")
    
    return {
        "patients_monitored": len(monitoring_data),
        "trend_analysis": trend_analysis,
        "alert_system": alert_system,
        "care_plans": care_plans
    }

def demo_medical_imaging_analysis():
    """Demonstra análise de imagens médicas"""
    print("\n🖼️ Análise de Imagens Médicas")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="imaging_analyst")
    
    # Gera dados de imagens
    imaging_data = MedicalDataGenerator.generate_imaging_data()
    
    print(f"📸 Analisando {len(imaging_data)} estudos de imagem...")
    
    # Análise de achados
    imaging_analysis_prompt = f"""
    Analise os achados de imagem:
    
    {json.dumps(imaging_data, indent=2)}
    
    Para cada estudo, forneça:
    1. Interpretação dos achados
    2. Significado clínico
    3. Correlação com sintomas
    4. Diagnósticos diferenciais
    5. Necessidade de estudos adicionais
    6. Seguimento recomendado
    """
    
    imaging_analysis = agent.chat(imaging_analysis_prompt, use_context=True)
    print(f"🔍 Análise de Imagens: {imaging_analysis}")
    
    # Detecção de achados críticos
    critical_findings_prompt = """
    Identifique achados críticos que requerem ação imediata:
    
    1. Achados que ameaçam a vida
    2. Necessidade de intervenção urgente
    3. Comunicação imediata com clínico
    4. Protocolos de emergência
    5. Tempo para ação
    6. Documentação necessária
    """
    
    critical_findings = agent.chat(critical_findings_prompt, use_context=True)
    print(f"🚨 Achados Críticos: {critical_findings}")
    
    # Controle de qualidade
    quality_control_prompt = """
    Avalie a qualidade dos estudos de imagem:
    
    1. Qualidade técnica das imagens
    2. Adequação do protocolo
    3. Artefatos presentes
    4. Limitações do estudo
    5. Necessidade de repetição
    6. Recomendações técnicas
    """
    
    quality_control = agent.chat(quality_control_prompt, use_context=True)
    print(f"\n✅ Controle de Qualidade: {quality_control}")
    
    return {
        "studies_analyzed": len(imaging_data),
        "imaging_analysis": imaging_analysis,
        "critical_findings": critical_findings,
        "quality_control": quality_control
    }

def demo_drug_interaction_checker():
    """Demonstra verificação de interações medicamentosas"""
    print("\n💊 Verificação de Interações Medicamentosas")
    print("=" * 50)
    
    agent = MangabaAgent(agent_id="drug_interaction_checker")
    
    # Simula prescrições complexas
    prescriptions = [
        {
            "patient_id": "PAC_001",
            "medications": [
                {"name": "Losartana", "dose": "50mg", "frequency": "1x/dia"},
                {"name": "Metformina", "dose": "850mg", "frequency": "2x/dia"},
                {"name": "Atorvastatina", "dose": "20mg", "frequency": "1x/dia"},
                {"name": "AAS", "dose": "100mg", "frequency": "1x/dia"},
                {"name": "Omeprazol", "dose": "20mg", "frequency": "1x/dia"}
            ],
            "allergies": ["Penicilina"],
            "comorbidities": ["Diabetes", "Hipertensão", "Dislipidemia"],
            "kidney_function": "Normal",
            "liver_function": "Normal"
        },
        {
            "patient_id": "PAC_002",
            "medications": [
                {"name": "Salbutamol", "dose": "100mcg", "frequency": "SOS"},
                {"name": "Budesonida", "dose": "200mcg", "frequency": "2x/dia"},
                {"name": "Montelucaste", "dose": "10mg", "frequency": "1x/dia"},
                {"name": "Loratadina", "dose": "10mg", "frequency": "1x/dia"}
            ],
            "allergies": ["Látex"],
            "comorbidities": ["Asma"],
            "kidney_function": "Normal",
            "liver_function": "Normal"
        }
    ]
    
    print(f"💊 Verificando {len(prescriptions)} prescrições...")
    
    # Análise de interações
    interaction_analysis_prompt = f"""
    Analise as interações medicamentosas:
    
    {json.dumps(prescriptions, indent=2)}
    
    Para cada prescrição, identifique:
    1. Interações medicamento-medicamento
    2. Interações medicamento-doença
    3. Contraindicações por alergia
    4. Ajustes por função renal/hepática
    5. Severidade das interações
    6. Alternativas terapêuticas
    """
    
    interaction_analysis = agent.chat(interaction_analysis_prompt, use_context=True)
    print(f"⚠️ Análise de Interações: {interaction_analysis}")
    
    # Otimização de prescrições
    prescription_optimization_prompt = """
    Otimize as prescrições:
    
    1. Simplificação de esquemas
    2. Redução de interações
    3. Melhoria da aderência
    4. Custo-efetividade
    5. Monitoramento necessário
    6. Educação do paciente
    """
    
    prescription_optimization = agent.chat(prescription_optimization_prompt, use_context=True)
    print(f"🔧 Otimização de Prescrições: {prescription_optimization}")
    
    # Alertas farmacológicos
    pharmacological_alerts_prompt = """
    Configure alertas farmacológicos:
    
    1. Alertas de dosagem
    2. Alertas de duração
    3. Alertas de monitoramento
    4. Alertas de descontinuação
    5. Alertas de gravidez/lactação
    6. Alertas de idade
    """
    
    pharmacological_alerts = agent.chat(pharmacological_alerts_prompt, use_context=True)
    print(f"\n🚨 Alertas Farmacológicos: {pharmacological_alerts}")
    
    return {
        "prescriptions_checked": len(prescriptions),
        "interaction_analysis": interaction_analysis,
        "prescription_optimization": prescription_optimization,
        "pharmacological_alerts": pharmacological_alerts
    }

def main():
    """Executa demonstração completa de soluções médicas"""
    print("🏥 Mangaba Agent - Soluções Médicas")
    print("=" * 80)
    
    try:
        # Demonstrações de diferentes áreas médicas
        diagnostic_result = demo_diagnostic_assistance()
        decision_result = demo_clinical_decision_support()
        monitoring_result = demo_patient_monitoring()
        imaging_result = demo_medical_imaging_analysis()
        drug_result = demo_drug_interaction_checker()
        
        print("\n🎉 DEMONSTRAÇÃO MÉDICA COMPLETA!")
        print("=" * 70)
        
        print("\n📊 Resumo dos Resultados:")
        print(f"   👥 Pacientes analisados: {diagnostic_result['patients_analyzed']}")
        print(f"   📋 Casos clínicos: {decision_result['cases_analyzed']}")
        print(f"   📈 Pacientes monitorados: {monitoring_result['patients_monitored']}")
        print(f"   🖼️ Estudos de imagem: {imaging_result['studies_analyzed']}")
        print(f"   💊 Prescrições verificadas: {drug_result['prescriptions_checked']}")
        
        print(f"\n🏥 Capacidades Demonstradas:")
        print("   • Assistência diagnóstica inteligente")
        print("   • Interpretação de exames laboratoriais")
        print("   • Suporte à decisão clínica")
        print("   • Aplicação de protocolos clínicos")
        print("   • Monitoramento contínuo de pacientes")
        print("   • Sistema de alertas personalizados")
        print("   • Análise de imagens médicas")
        print("   • Detecção de achados críticos")
        print("   • Verificação de interações medicamentosas")
        print("   • Otimização de prescrições")
        print("   • Avaliação de riscos clínicos")
        print("   • Planos de cuidado personalizados")
        print("   • Controle de qualidade em imagens")
        print("   • Alertas de segurança farmacológica")
        
    except Exception as e:
        print(f"❌ Erro durante demonstração médica: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()