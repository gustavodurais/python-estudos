"""Leitura de dados com input() e conversão de tipos, com validação."""


# Funções

def ler_numero(mensagem, tipo=float):
    """Pede um número até que um valor válido seja digitado.

    Aceita vírgula como separador decimal (ex.: 1500,50).
    """
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            return tipo(texto)
        except ValueError:
            print(f"Valor inválido. Digite um número do tipo {tipo.__name__}.")


# Entradas e saídas

fruta = input("Digite o nome de uma fruta: ")
print(fruta)

idade = ler_numero("Digite a sua idade: ", int)
nome = input("Digite o seu nome: ")
salario = ler_numero("Digite o seu salário: ")
ativo = True

print(f"Idade: {idade}")
print(f"Nome: {nome}")
print(f"Salário: {salario:.2f}")
print(f"Ativo: {ativo}")
