"""Montagem e envio de e-mail com anexo via SMTP."""
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path


def montar_mensagem(remetente, destinatario, assunto, corpo, anexo):
    """Cria o e-mail com o arquivo CSV anexado."""
    caminho = Path(anexo)
    mensagem = EmailMessage()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    mensagem.set_content(corpo)
    mensagem.add_attachment(
        caminho.read_bytes(),
        maintype="text",
        subtype="csv",
        filename=caminho.name,
    )
    return mensagem


def enviar_email(mensagem, host, porta, usuario, senha):
    """Envia a mensagem. Porta 465 usa SSL; outras portas usam STARTTLS."""
    contexto = ssl.create_default_context()
    if porta == 465:
        with smtplib.SMTP_SSL(host, porta, context=contexto) as servidor:
            servidor.login(usuario, senha)
            servidor.send_message(mensagem)
    else:
        with smtplib.SMTP(host, porta) as servidor:
            servidor.starttls(context=contexto)
            servidor.login(usuario, senha)
            servidor.send_message(mensagem)
