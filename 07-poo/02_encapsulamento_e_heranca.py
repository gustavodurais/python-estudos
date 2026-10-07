"""POO: encapsulamento, herança e polimorfismo."""


class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # "_" indica uso interno da classe

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor

    def __str__(self):
        return f"{self.titular}: R$ {self._saldo:.2f}"


class ContaPoupanca(ContaBancaria):
    """Herda tudo de ContaBancaria e acrescenta rendimento."""

    def __init__(self, titular, saldo_inicial=0, taxa_juros=0.005):
        super().__init__(titular, saldo_inicial)
        self.taxa_juros = taxa_juros

    def render_juros(self):
        self._saldo += self._saldo * self.taxa_juros

    def __str__(self):  # sobrescreve o método da classe pai
        return f"[Poupança] {super().__str__()}"


def main():
    corrente = ContaBancaria("Ana", 100)
    poupanca = ContaPoupanca("Bruno", 1000)

    corrente.depositar(50)
    poupanca.render_juros()

    try:
        corrente.sacar(500)
    except ValueError as erro:
        print(f"Erro: {erro}")

    # Polimorfismo: o mesmo print funciona para os dois tipos de conta
    for conta in (corrente, poupanca):
        print(conta)


if __name__ == "__main__":
    main()
