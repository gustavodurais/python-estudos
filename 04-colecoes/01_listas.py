"""Listas: coleção ordenada e mutável."""

frutas = ["maçã", "banana", "laranja"]

print(frutas)
print(frutas[0], frutas[-1])  # primeiro e último item
print(len(frutas))

frutas.append("uva")  # adiciona no fim
frutas.insert(1, "morango")  # adiciona na posição 1
frutas.remove("banana")  # remove pelo valor
ultima = frutas.pop()  # remove e devolve o último item
print(frutas, "| removida:", ultima)

frutas.sort()  # ordena a própria lista
print(sorted(frutas, reverse=True))  # devolve uma nova lista ordenada
print("laranja" in frutas)  # verifica se o item existe

for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")

numeros = [1, 2, 3, 4, 5, 6]
print(numeros[1:4])  # fatiamento [início:fim): posições 1, 2 e 3
print(sum(numeros), min(numeros), max(numeros))

# Compreensão de lista: cria uma lista a partir de outra
quadrados = [n ** 2 for n in numeros]
pares = [n for n in numeros if n % 2 == 0]
print(quadrados)
print(pares)
