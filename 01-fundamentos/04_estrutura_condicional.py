"""Estrutura condicional: if, elif e else."""

# Testa os valores de fronteira (16, 17, 18) para conferir a lógica.
for idade in (15, 17, 18, 19):
    if idade >= 18:
        print(f"{idade} anos: você é maior de idade.")
    elif idade > 16:
        print(f"{idade} anos: você é infanto juvenil!")
    else:
        print(f"{idade} anos: você é menor de idade.")
