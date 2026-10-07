"""Tuplas: coleção ordenada e imutável."""

# Tupla é uma lista ordenada e imutável. 

coordenada = (10.5, 20.3)
x, y = coordenada  # desempacotamento
print(f"x = {x}, y = {y}")

dias_uteis = ("seg", "ter", "qua", "qui", "sex")
print(dias_uteis[0], len(dias_uteis))
print(dias_uteis.index("qua"), dias_uteis.count("sex"))

# Tuplas não podem ser alteradas (exceções: veja a pasta 06-excecoes)
try:
    coordenada[0] = 99
except TypeError as erro:
    print(f"Erro esperado: {erro}")


def menor_e_maior(valores):
    """Uma função pode devolver vários valores: na verdade, uma tupla."""
    return min(valores), max(valores)


menor, maior = menor_e_maior([3, 1, 9, 4])
print(f"menor = {menor}, maior = {maior}")
