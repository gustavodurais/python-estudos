"""Arquivos com 'with open' e tratamento dos erros mais comuns."""

# Arquivos com 'with open' e tratamento dos erros mais comuns
# With open é usado para abrir arquivos em python
# O 'with open' é mais seguro do que o 'open' porque ele fecha o arquivo automaticamente

from pathlib import Path

PASTA = Path(__file__).parent # caminho da pasta
EXISTENTE = PASTA.parent / "03-arquivos" / "dados" / "arquivo1.txt" # caminho do arquivo
INEXISTENTE = PASTA / "nao_existe.txt" # caminho do arquivo que não existe


def ler_arquivo(caminho): # lê o arquivo
    """Devolve o texto do arquivo, ou None se não for possível ler."""
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo: # abre o arquivo
            return arquivo.read()
    except FileNotFoundError: # captura a exceção FileNotFoundError
        print(f"Arquivo não encontrado: {caminho.name}")
    except PermissionError: # captura a exceção PermissionError
        print(f"Sem permissão para ler: {caminho.name}")
    except UnicodeDecodeError: # captura a exceção UnicodeDecodeError
        print(f"O arquivo não está em UTF-8: {caminho.name}")
    return None


def main(): # função principal
    conteudo = ler_arquivo(EXISTENTE) # lê o arquivo existente
    if conteudo is not None: # se o arquivo foi lido com sucesso
        print("Conteúdo:", conteudo.strip()) # imprime o conteúdo

    ler_arquivo(INEXISTENTE) # lê o arquivo inexistente


if __name__ == "__main__": # inicia o programa
    main()
