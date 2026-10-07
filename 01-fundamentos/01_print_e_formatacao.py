"""Variáveis, tipos e formas de formatar texto com print."""

# Variáveis

PI = 3.14
raio = 5
area = PI * raio ** 2  # área do círculo = pi * r²

# Prints

print(area)
print(type(area))

# 1) vírgula: o print converte e separa com espaço
print("O valor da área é:", area)

# 2) concatenação: exige converter o número para texto com str()
print("O valor da área é: " + str(area))

# 3) formatação com % (estilo antigo, ainda aparece em códigos legados)
print("O valor da área é: %.2f" % area)

# 4) f-string (forma recomendada) - quantas casas a partir da vírgula
print(f"O valor da área é: {area:.2f}")
