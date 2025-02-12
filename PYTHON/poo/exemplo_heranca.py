# Classe Pai (Superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return "Algum som..."  # Método genérico

# Classe Filha (Herda de Animal)
class Cachorro(Animal):
    def fazer_som(self):  # Sobrescrevendo o método da classe pai
        return "Au Au!"

# Classe Filha (Herda de Animal)
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Usando as classes
dog = Cachorro("Rex")
cat = Gato("Whiskers")

print(dog.nome, ":", dog.fazer_som())  # Rex : Au Au!
print(cat.nome, ":", cat.fazer_som())  # Whiskers : Miau!
