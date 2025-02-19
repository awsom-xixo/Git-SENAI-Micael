class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

def leNome():
    nome = str(input('Digite o nome do funcionário: '))
    return nome

def leSalario():
    salario = float(input('Digite o salário do vendedor: '))
    return salario

vendedor = Funcionario(leNome(),leSalario())

print(vendedor.nome, vendedor.salario)