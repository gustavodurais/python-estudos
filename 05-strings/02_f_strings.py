"""f-strings: formatação de texto moderna."""

# f-strings são uma forma de formatar strings em python
# Elas são mais legíveis e fáceis de usar do que as outras formas de formatação
# Elas são mais rápidas do que as outras formas de formatação

nome = "Ana"
idade = 20
salario = 3456.789
percentual = 0.256

print(f"{nome} tem {idade} anos")
print(f"Próximo ano: {idade + 1}")  # aceita expressões
print(f"Salário: R$ {salario:.2f}")  # duas casas decimais
print(f"Com milhar: {salario:,.2f}")  # padrão americano: 3,456.79

# Formato brasileiro (3.456,79): troca os separadores
br = f"{salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f"Formato brasileiro: R$ {br}")

print(f"Percentual: {percentual:.1%}") # formata como porcentagem
print(f"Zeros à esquerda: {idade:05d}") # adiciona zeros à esquerda
print(f"[{nome:>10}] [{nome:<10}] [{nome:^10}]")  # alinhamento
print(f"{nome=}")  # mostra nome e valor (útil para depurar)
