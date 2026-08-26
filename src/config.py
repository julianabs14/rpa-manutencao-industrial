import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA_APP = os.getenv("EMAIL_SENHA_APP")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")
SMTP_SERVIDOR = os.getenv("SMTP_SERVIDOR", "smtp.gmail.com")
SMTP_PORTA = int(os.getenv("SMTP_PORTA", "587"))

LIMITE_PARADAS_CRITICO = int(os.getenv("LIMITES_PARADAS_CRITICO", "5"))

CAMINHO_CSV_ENTRADA = "data/manutencao_bruta.csv"
PASTA_RELATORIOS = "reports" 
PASTA_LOGS = "logs"

