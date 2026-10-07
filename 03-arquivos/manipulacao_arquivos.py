"""Leitura e escrita de arquivos com pathlib e with open."""
from pathlib import Path

# Caminhos relativos a este script: funcionam de qualquer pasta.
PASTA_DADOS = Path(__file__).parent / "dados"
ENTRADA = PASTA_DADOS / "arquivo1.txt"
SAIDA = PASTA_DADOS / "saida.txt"

# Leitura. O 'with' fecha o arquivo sozinho, mesmo se ocorrer um erro.
with open(ENTRADA, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())

# Escrita: o modo "w" apaga o conteúdo anterior do arquivo.
with open(SAIDA, "w", encoding="utf-8") as arquivo:
    arquivo.write("Curso Python\n")

# Acréscimo: o modo "a" adiciona ao final sem apagar.
with open(SAIDA, "a", encoding="utf-8") as arquivo:
    arquivo.write("Acentuação funciona: ção, é, ü\n")

# Leitura linha a linha, com numeração.
with open(SAIDA, "r", encoding="utf-8") as arquivo:
    for numero, linha in enumerate(arquivo, start=1):
        print(f"{numero}: {linha.rstrip()}")
