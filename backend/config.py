import os
from dotenv import load_dotenv

# Carrega automaticamente o .env
load_dotenv()

class Config:
    """Configuração super simples - agnóstica para qualquer provedor de IA."""
    
    def __init__(self):
        # Obrigatórios
        self.api_key = os.getenv('GOOGLE_API_KEY') or os.getenv('API_KEY')
        self.model = os.getenv('MODEL_NAME', 'gemini-pro') or os.getenv('MODEL', 'gemini-pro')
        
        # Opcionais
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        
        # Validação simples
        if not self.api_key:
            raise ValueError("[ERROR] GOOGLE_API_KEY não encontrada! Configure no arquivo .env")
    
    def __str__(self):
        return f"Config(model={self.model}, log_level={self.log_level})"

# Instância global para facilitar
config = Config()