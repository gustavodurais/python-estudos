"""Dicionários: pares chave -> valor."""
import json

# Dicionário é uma coleção de pares chave -> valor.
# Chaves são únicas e podem ser de qualquer tipo imutável (strings, inteiros, tuplas).
# Valores podem ser de qualquer tipo.

aluno = {"nome": "Ana", "idade": 20, "curso": "Python"}

print(aluno["nome"])
print(aluno.get("email", "não informado"))  # get não dá erro se faltar

aluno["idade"] = 21  # altera
aluno["email"] = "ana@exemplo.com"  # adiciona
del aluno["curso"]  # remove

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
print(list(aluno.keys()))
print(list(aluno.values()))

# Dicionário com listas
notas = {"Ana": [8, 9], "Bruno": [6, 7.5]}
for nome, lista in notas.items():
    print(f"{nome}: média {sum(lista) / len(lista):.1f}")

# Contagem de palavras
texto = "python é bom python é útil"
contagem = {}
for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)

# Dicionários e JSON são muito parecidos: base para trabalhar com APIs
print(json.dumps(aluno, ensure_ascii=False, indent=2))
