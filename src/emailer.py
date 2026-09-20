import smtplib
from email.message import EmailMessage
from src.config import (
    EMAIL_REMETENTE, EMAIL_SENHA_APP, EMAIL_DESTINATARIO, SMTP_SERVIDOR, SMTP_PORTA
)

def enviar_relatorio_por_email(caminho_relatorio, resumo_texto):
    mensagem = EmailMessage()
    mensagem["Subjetct"] = "Relatório Diário de Manutenção"
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = EMAIL_DESTINATARIO
    mensagem.set_content(
        "Ola, \n\nSegue em anexo o relatorio automatico de manutencao. \n\n"
        f"Resumo rapido: \n{resumo_texto}\n\n"
        "Este e-mail foi enviado automaticamente por um RPA"
    
    )

    with open(caminho_relatorio, "rb") as arquivo:
        conteudo = arquivo.read()

    mensagem.add_attachment(
        conteudo,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=caminho_relatorio.split("/")[-1]
    )

    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as servidor:
        servidor.starttls()
        servidor.login( EMAIL_REMETENTE, EMAIL_SENHA_APP)
        servidor.send_message(mensagem)

        
