class ZeNinguem:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def ficarPobre(self):
        self.__salario = 0
        return "Fodidooooookkkkkkkkkkkkkkkk agr ta pobre"
    def retornarSalario(self):
        return self.__salario

class Vitor(ZeNinguem):
    def ficarPobre(self):
        return super().ficarPobre()

fodido = Vitor('Vitor Araújo Cassambolas', 1400)

print(f"Nome: {fodido.nome}\n Salário: {fodido.retornarSalario()}")
print(fodido.ficarPobre())
print(f"Nome: {fodido.nome}\n Salário: {fodido.retornarSalario()}")