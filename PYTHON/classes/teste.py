class Conta:
    numero = "00000-0"
    saldo = 0.00

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if (self.saldo > 0):
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")


if __name__ == '__main__':
    conta = Conta()
    conta.saldo = 20
    conta.numero = "13131-2"


    val = float(input('Digite um valor para depositar na sua conta: '))
    res = str(input(f"Você tem certeza que quer adicionar R${val} a sua conta? [S/N] ")).strip().upper()[0]

    if res == "S":
        conta.deposito(val)
    else:
        conta.saldo = conta.saldo

    print(f"Saldo atual da conta: R${conta.saldo}")

    res =""

    res = input(f"Quer finalizar o programa? [S/N] ")
        
    if res.strip().upper()[0]=="S":


        pass