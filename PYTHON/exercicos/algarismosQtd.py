def leNumDigitos():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
            return len(str(abs(num)))  #abs() para ignorar o sinal negativo
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


qtd = leNumDigitos()
print(f'O número tem {qtd} digitos.')