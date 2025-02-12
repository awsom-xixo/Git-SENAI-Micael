class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario  # Salário encapsulado (privado)

    def entregarSalario(self):
        return self.__salario  # Método para acessar o salário

    def mostrarSalario(self):
        return self.__salario  # Método base (será sobrescrito nas classes filhas)

class Gerente(Funcionario):
    def mostrarSalario(self):
        bonus = 0.20
        salario_com_bonus = self.entregarSalario() * (1 + bonus)  # Adicionando 20% ao salário
        return salario_com_bonus

class Programador(Funcionario):
    def mostrarSalario(self):
        bonus = 0.10
        salario_com_bonus = self.entregarSalario() * (1 + bonus)  # Adicionando 10% ao salário
        return salario_com_bonus

programadores = [Programador('Paulo', 600), Programador('Augusto', 650)]
gerentes = [Gerente('Neri', 700)]

print('Programadores\n', '-'*15)
for programador in programadores:
    print(f"{programador.nome}: R${programador.mostrarSalario():.2f}")

print('\nGerentes\n', '-'*15)
for gerente in gerentes:
    print(f"{gerente.nome}: R${gerente.mostrarSalario():.2f}")