"""Funções: definição, parâmetros, retorno e validação de entrada."""

APROVACAO_MINIMA = 7


def mensagem1():
    """Função sem retorno: apenas imprime."""
    print("Olá mundo!")


def mensagem2():
    """Função com retorno: devolve um texto."""
    return "Olá mundo! Mensagem 2."

# A função ler_nota faz o input e a validação, deixando o código mais limpo e organizado.

def ler_nota(mensagem):
    """Lê uma nota entre 0 e 10, repetindo a pergunta se for inválida."""
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número válido.")
            continue
        if 0 <= nota <= 10:
            return nota
        print("A nota deve estar entre 0 e 10.")


def calcular_media(nota1, nota2):
    """Só calcula: não imprime nada, por isso é fácil de reaproveitar."""
    return (nota1 + nota2) / 2


def situacao(media):
    """Devolve 'Aprovado' ou 'Reprovado' conforme a média."""
    return "Aprovado" if media >= APROVACAO_MINIMA else "Reprovado"

# Main é a função principal que manda no código, ou seja, é onde o código começa a ser executado.

def main():
    mensagem1()
    print(mensagem2())

    nota1 = ler_nota("Digite a nota 1 do aluno(a): ")
    nota2 = ler_nota("Digite a nota 2 do aluno(a): ")
    media = calcular_media(nota1, nota2)

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Média: {media:.2f} | Resultado: {situacao(media)}")

# O if __name__ == "__main__": serve para que o código só rode quando o arquivo for executado diretamente.

if __name__ == "__main__":
    main()
