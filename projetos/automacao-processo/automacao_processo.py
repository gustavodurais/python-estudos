"""Automação de processo: abre o sistema, faz login, baixa um CSV e envia
por e-mail.

A SENHA DO SISTEMA NUNCA PASSA PELO CÓDIGO: o script digita só o usuário e
espera você digitar a senha e concluir o login.

Uso:
    python automacao_processo.py --simular   # só mostra o que faria
    python automacao_processo.py             # execução real
"""
import argparse
import getpass
import logging
import smtplib
import time
from pathlib import Path

import config
from enviador_email import enviar_email, montar_mensagem

logger = logging.getLogger(__name__)

TOLERANCIA_RELOGIO = 2  # segundos de folga ao comparar datas de arquivos
CHECAGENS_ESTAVEIS = 3  # tamanho igual em N checagens = download concluído


def obter_pyautogui():
    """Importa o pyautogui só quando necessário (não funciona sem tela)."""
    import pyautogui

    pyautogui.FAILSAFE = True  # mouse no canto superior esquerdo aborta
    pyautogui.PAUSE = 0.5  # pausa entre as ações
    return pyautogui


def validar_configuracao(simular):
    """Garante que as configurações obrigatórias foram preenchidas."""
    obrigatorias = {
        "NOME_SISTEMA": config.NOME_SISTEMA,
        "USUARIO_SISTEMA": config.USUARIO_SISTEMA,
        "EMAIL_REMETENTE": config.EMAIL_REMETENTE,
        "EMAIL_DESTINATARIO": config.EMAIL_DESTINATARIO,
    }
    faltando = [nome for nome, valor in obrigatorias.items() if not valor]
    if not faltando:
        return
    texto = ", ".join(faltando)
    if simular:
        logger.warning("Configurações ainda vazias no .env: %s", texto)
    else:
        raise ValueError(f"Preencha no arquivo .env: {texto}")


def abrir_sistema(simular):
    """Abre o sistema pelo menu Iniciar do Windows."""
    logger.info("Abrindo o sistema '%s'...", config.NOME_SISTEMA)
    if simular:
        return
    gui = obter_pyautogui()
    gui.press("win")
    time.sleep(1)
    gui.write(config.NOME_SISTEMA, interval=0.05)
    time.sleep(1)
    gui.press("enter")
    time.sleep(config.ESPERA_ABERTURA)


def fazer_login(simular):
    """Digita o usuário e espera você informar a senha manualmente."""
    logger.info("Digitando o usuário '%s'...", config.USUARIO_SISTEMA)
    if simular:
        logger.info("Simulação: pediria a senha ao usuário.")
        return
    gui = obter_pyautogui()
    gui.write(config.USUARIO_SISTEMA, interval=0.05)
    gui.press("tab")  # leva o cursor ao campo de senha
    input(
        "\nDigite a SENHA no sistema e conclua o login.\n"
        "Depois volte a esta janela e pressione ENTER: "
    )


def encontrar_csv_recente(pasta, desde):
    """Devolve o CSV mais novo da pasta modificado a partir de 'desde'."""
    candidatos = [
        arquivo
        for arquivo in Path(pasta).glob("*.csv")
        if arquivo.stat().st_mtime >= desde - TOLERANCIA_RELOGIO
    ]
    return max(candidatos, key=lambda a: a.stat().st_mtime, default=None)


def aguardar_download(pasta, desde, timeout, intervalo=1.0):
    """Espera um CSV novo aparecer e parar de crescer (download concluído).

    Navegadores gravam o download com extensão temporária (.crdownload,
    .part) e só depois renomeiam para .csv. Mesmo assim, conferimos que o
    tamanho ficou igual por algumas checagens seguidas.
    """
    limite = time.monotonic() + timeout
    tamanho_anterior = -1
    estaveis = 0
    while time.monotonic() < limite:
        arquivo = encontrar_csv_recente(pasta, desde)
        if arquivo is not None:
            tamanho = arquivo.stat().st_size
            if tamanho > 0 and tamanho == tamanho_anterior:
                estaveis += 1
                if estaveis >= CHECAGENS_ESTAVEIS:
                    return arquivo
            else:
                estaveis = 0
            tamanho_anterior = tamanho
        time.sleep(intervalo)
    raise TimeoutError(
        f"Nenhum CSV novo apareceu em {pasta} após {timeout} segundos."
    )


def baixar_csv(simular):
    """Aciona a exportação do CSV e espera o arquivo chegar à pasta."""
    logger.info("Baixando o CSV para %s...", config.PASTA_DOWNLOADS)
    if simular:
        return None
    inicio = time.time()
    if config.BOTAO_EXPORTAR:
        obter_pyautogui().click(*config.BOTAO_EXPORTAR)
    else:
        print("\nBOTAO_EXPORTAR não configurado: clique em exportar o CSV.")
    arquivo = aguardar_download(
        config.PASTA_DOWNLOADS, inicio, config.TEMPO_MAX_DOWNLOAD
    )
    logger.info("Download concluído: %s", arquivo.name)
    return arquivo


def enviar_resultado(arquivo, simular):
    """Envia o CSV por e-mail para o destinatário configurado."""
    logger.info("Enviando e-mail para %s...", config.EMAIL_DESTINATARIO)
    if simular:
        return
    senha = config.EMAIL_SENHA or getpass.getpass("Senha do e-mail: ")
    mensagem = montar_mensagem(
        remetente=config.EMAIL_REMETENTE,
        destinatario=config.EMAIL_DESTINATARIO,
        assunto=f"Relatório CSV - {time.strftime('%d/%m/%Y')}",
        corpo="Olá,\n\nSegue em anexo o arquivo CSV.\n\n(Envio automático)",
        anexo=arquivo,
    )
    enviar_email(
        mensagem,
        config.SMTP_HOST,
        config.SMTP_PORTA,
        config.EMAIL_REMETENTE,
        senha,
    )
    logger.info("E-mail enviado com sucesso.")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--simular",
        action="store_true",
        help="mostra os passos sem mexer no mouse/teclado nem enviar e-mail",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )

    try:
        validar_configuracao(args.simular)
        if not args.simular:
            logger.info(
                "Começando em %ds. Mouse no canto superior esquerdo aborta.",
                config.ESPERA_INICIAL,
            )
            time.sleep(config.ESPERA_INICIAL)
        abrir_sistema(args.simular)
        fazer_login(args.simular)
        arquivo = baixar_csv(args.simular)
        enviar_resultado(arquivo, args.simular)
    except (ValueError, TimeoutError, OSError, smtplib.SMTPException) as erro:
        logger.error("Falha na automação: %s", erro)
        return 1
    except KeyboardInterrupt:
        logger.warning("Interrompido pelo usuário.")
        return 1
    except Exception:
        logger.exception("Erro inesperado.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
