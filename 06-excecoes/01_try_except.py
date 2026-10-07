"""Tratamento de exceções: try, except, else, finally e raise."""

# Try, except, else, finally e raise são usados para tratamento de exceções em python
# Try é usado para tentar executar um código
# Except é usado para capturar uma exceção
# Else é usado para executar um código se não houver exceção
# Finally é usado para executar um código sempre
# Raise é usado para levantar uma exceção


def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError: # captura a exceção ZeroDivisionError
        print("Erro: divisão por zero.")
        return None
    else:  # só roda se NÃO houve exceção
        return resultado
    finally:  # roda sempre, com ou sem erro
        print("Divisão finalizada.")


def validar_idade(idade):
    """Levanta uma exceção própria quando o valor não faz sentido."""
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.") # lança uma exceção
    return idade


def converter(texto):
    try:
        return int(texto) # converte para inteiro
    except ValueError: # captura a exceção ValueError
        print(f"'{texto}' não é um número inteiro.")
    except TypeError: # captura a exceção TypeError
        print("Tipo inválido para conversão.")
    return None


def main():
    print(dividir(10, 2)) # roda normalmente
    print(dividir(10, 0)) # roda normalmente também, mas com erro

    print(converter("42"))
    print(converter("abc"))
    print(converter(None))

    try:
        validar_idade(-5) # lança uma exceção
    except ValueError as erro: # captura a exceção ValueError
        print(f"Erro capturado: {erro}")


if __name__ == "__main__": # inicia o programa
    main()
