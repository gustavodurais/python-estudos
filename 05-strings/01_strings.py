"""Strings: métodos, fatiamento e busca."""

texto = "  Curso de Python  "
print(texto.strip())  # remove espaços das pontas
print(texto.upper()) # deixa o texto em maiúsculo
print(texto.lower()) # deixa o texto em minúsculo
print(texto.strip().title()) # deixa a primeira letra de cada palavra em maiúsculo
print(texto.replace("Python", "Pandas")) # substitui uma string por outra

nome = "python"
print(nome[0], nome[-1])  # primeiro e último caractere
print(nome[1:4])  # fatiamento: "yth"
print(nome[::-1])  # invertido
print(len(nome)) # quantidade de caracteres

frase = "maçã,banana,uva"
frutas = frase.split(",")  # texto -> lista
print(frutas)
print(" | ".join(frutas))  # lista -> texto

print("py" in nome) # verifica se uma string está em outra
print(nome.startswith("py"), nome.endswith("on")) # verifica se uma string começa ou termina com outra
print(nome.find("th"), nome.count("o")) # encontra a posição de uma string e conta quantas vezes uma string aparece
print("123".isdigit(), "abc".isalpha()) # verifica se uma string é composta apenas por números ou letras

# Strings são imutáveis: os métodos devolvem um novo texto
maiuscula = nome.upper()
print(nome, maiuscula) # a variável nome não muda
