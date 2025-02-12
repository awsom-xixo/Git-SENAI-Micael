import random

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.dia = 0

    def dormir(self):
        if self.idade > 100:
            print(f"{self.nome} veio a falecer de causas naturais aos {self.idade} anos... Press F to pay respect.")
        else:
            self.dia += 1
            if self.dia % 365 == 0:
                self.envelhecer()
                self.crescer()

        mensagens = [
            'Mais um dia sem fazer absolutamente nada...',
            'Você dorme encarando o teto.',
            'Você teve um ótimo descanso!',
            'Você teve um pesadelo :('
        ]
        print(random.choice(mensagens))
        print(f"Um dia passou.")

    def verificar_morte(self):
        if self.idade >= 100:
            print(f"{self.nome} faleceu de causas naturais aos {self.idade} anos... Press F to pay respect.")
            exit()
        elif self.peso <= 30:
            print(f"{self.nome} morreu de anorexia aos {self.idade} anos...")
            exit()
        elif self.peso >= 300:
            print(f"{self.nome} morreu por não suportar o próprio peso aos {self.idade} anos...")
            exit()

    def envelhecer(self):
        self.idade += 1
        mensagens = [
            'PARABÉNS PRA VOCÊ, MUITOS ANOS DE VIDA!! ;)',
            'Você passou mais um ano da sua vida sem dar ideia pra *aquela* romana...',
            'Você está cada vez mais próximo da morte.',
            'Você conseguiu, mais um ano sobrevivido no Brasil!'
        ]
        print(random.choice(mensagens))
        print(f"Você está um ano mais velho, agora tem {self.idade} anos.")

    def crescer(self):
        if self.idade <= 21:
            self.altura += 0.05
            print(f"Você cresceu mais 5cm, agora tem {self.altura:.2f}m.")

            mensagens = [
                'Você se mediu durante uma consulta no hospital e notou que cresceu mais 5cm!',
                'Sabia que no EUA as garotas adoram caras altos?...',
                'Cada vez mais alto, mas e quanto ao seu peso, han?!',
                'Wow, cada vez mais alto.'
            ]
            print(random.choice(mensagens))

    def engordar(self):
        self.peso += 0.5
        mensagens = [
            'Você ATACOU um Rodízio de Pizza, foi terrível!',
            'Você comeu tudo que encontrou dentro do armário de besteiras.',
            'Só sabe comer? Pfff...',
            'Cada vez mais redondo.'
        ]
        print(random.choice(mensagens))
        print(f"Você engordou 0.5kg, agora tem {self.peso:.1f}kg.")

    def treinar(self):
        self.peso += 0.2
        mensagens = [
            'Wow, finalmente fez algo útil!',
            '"BIG MUSCLES, BIG *BIG* MUSCLES" na sua cabeça enquanto faz exercícios que até uma idosa seria capaz.',
            'Você se exercita ouvindo rock pensando que é descolado.',
            'Esse é o caminho pra *romana*!'
        ]
        print(random.choice(mensagens))
        print(f"Sua massa muscular aumentou, agora você tem {self.peso:.1f}kg.")

    def emagrecer(self):
        self.peso -= 1
        mensagens = [
            'FIT!',
            'Você inventa uma dieta, segue ela e passa fome.',
            'Perdendo alguns quilinhos, um de cada vez...',
            '"As meninas gostam de homens magros?" Você se questiona enquanto passa um dia comendo grama...'
        ]
        print(random.choice(mensagens))
        print(f"Você emagreceu 1kg, agora tem {self.peso:.1f}kg.")


if __name__ == "__main__":
    individuo = Pessoa(nome="João", idade=15, peso=70, altura=1.70)

    from os import name, system
    while True:
        res = input(f"Você quer encerrar o programa? [S/N] ").strip().upper()[0]
        system('clear' if name == 'posix' else 'cls')

        if res != "N":
            exit()

        individuo.dia = 0
        individuo.idade = 15
        individuo.altura = 1.70
        individuo.peso = 70

        while True:
            print(f"\nDia {individuo.dia}")
            print(f"Nome: {individuo.nome}")
            print(f"Idade: {individuo.idade} anos")
            print(f"Peso: {individuo.peso:.1f}kg")
            print(f"Altura: {individuo.altura:.2f}m\n")

            print("[P] para *Pular Um Ano*")
            print("[D] para *Dormir*")
            print("[C] para *Comer*")
            print("[T] para *Treinar*")
            print("[E] para *Emagrecer*")
            print("[S] para *Encerrar*")
            print("")

            res = input("Digite qualquer opção acima pra realizar uma ação: ").strip().upper()[0]
            system('clear' if name == 'posix' else 'cls')

            match res:

                case "D":
                    individuo.dormir()
                case "P":
                    individuo.dia += 365
                    individuo.envelhecer()
                    individuo.crescer()
                    individuo.verificar_morte()
                case "C":
                    individuo.engordar()
                    individuo.verificar_morte()
                case "T":
                    individuo.treinar()
                    individuo.verificar_morte()
                case "E":
                    individuo.emagrecer()
                    individuo.verificar_morte()
                case "S":
                    break
