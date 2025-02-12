class Veiculo:
    def mover(self):
        pass  # Método genérico

class Carro(Veiculo):
    def mover(self):
        return "O carro está dirigindo na estrada."

class Barco(Veiculo):
    def mover(self):
        return "O barco está navegando no mar."

class Aviao(Veiculo):
    def mover(self):
        return "O avião está voando no céu."

# Criando uma lista de veículos
veiculos = [Carro(), Barco(), Aviao()]

# Testando o polimorfismo
for veiculo in veiculos:
    print(veiculo.mover())  
