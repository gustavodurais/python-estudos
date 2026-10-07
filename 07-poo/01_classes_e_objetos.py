"""POO básica: classes, objetos, atributos e métodos."""

# POO (Programação Orientada a Objetos) é uma forma de organizar o código em classes e objetos
# Classes são como moldes para criar objetos
# Objetos são instâncias de uma classe
# Atributos são características de um objeto
# Métodos são ações que um objeto pode realizar

class Aluno:
    """Representa um aluno e as suas notas."""

    NOTA_MINIMA = 7  # atributo de classe: igual para todos os alunos

    def __init__(self, nome): # método construtor
        self.nome = nome  # atributo de instância
        self.notas = []

    def adicionar_nota(self, nota): # método que adiciona nota
        if not 0 <= nota <= 10: # verifica se a nota é válida
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.notas.append(nota)

    @property
    def media(self): # método que calcula a média
        """Usada como atributo: aluno.media (sem parênteses)."""
        if not self.notas: # verifica se tem notas
            return 0.0
        return sum(self.notas) / len(self.notas)

    def situacao(self): # método que retorna a situação do aluno
        if self.media >= self.NOTA_MINIMA: # verifica se a média é maior ou igual a nota mínima
            return "Aprovado"
        return "Reprovado"

    def __str__(self): # método que retorna a representação do objeto
        return f"{self.nome}: média {self.media:.1f} ({self.situacao()})"


def main():
    ana = Aluno("Ana")
    ana.adicionar_nota(8)
    ana.adicionar_nota(9.5)

    bruno = Aluno("Bruno")
    bruno.adicionar_nota(5)
    bruno.adicionar_nota(6)

    print(ana)
    print(bruno)

    try:
        bruno.adicionar_nota(11)
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
