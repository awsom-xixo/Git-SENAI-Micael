class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado (__)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

# Criando a conta
conta = ContaBancaria("Xixo", 500)

# Testando os métodos
conta.depositar(200)
conta.sacar(100)
conta.mostrar_saldo()

# Não podemos acessar __saldo diretamente (isso gera erro!)
# print(conta.__saldo)  ❌ Atributo privado!
