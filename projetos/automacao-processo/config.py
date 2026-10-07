"""Configurações da automação, lidas do arquivo .env (nunca versionado)."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")


def _env(nome, padrao=""):
    """Lê uma variável de ambiente; valor vazio equivale a 'não definido'."""
    return os.getenv(nome) or padrao


def _coordenada(texto):
    """Converte '120,340' em (120, 340). Devolve None se estiver vazio."""
    if not texto:
        return None
    x, y = texto.split(",")
    return int(x), int(y)


# --- Sistema ---------------------------------------------------------------
NOME_SISTEMA = _env("NOME_SISTEMA")
USUARIO_SISTEMA = _env("USUARIO_SISTEMA")
BOTAO_EXPORTAR = _coordenada(_env("BOTAO_EXPORTAR"))  # None = clique manual
ESPERA_ABERTURA = 8  # segundos para o sistema abrir
ESPERA_INICIAL = 5  # segundos para você deixar a tela pronta

# --- Download --------------------------------------------------------------
PASTA_DOWNLOADS = Path(_env("PASTA_DOWNLOADS", str(Path.home() / "Downloads")))
TEMPO_MAX_DOWNLOAD = int(_env("TEMPO_MAX_DOWNLOAD", "120"))

# --- E-mail ----------------------------------------------------------------
SMTP_HOST = _env("SMTP_HOST", "smtp.gmail.com")
SMTP_PORTA = int(_env("SMTP_PORTA", "465"))
EMAIL_REMETENTE = _env("EMAIL_REMETENTE")
EMAIL_SENHA = _env("EMAIL_SENHA")  # vazio = a senha é pedida no terminal
EMAIL_DESTINATARIO = _env("EMAIL_DESTINATARIO")
