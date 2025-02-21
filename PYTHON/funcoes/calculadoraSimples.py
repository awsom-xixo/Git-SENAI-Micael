def main():
    while True:
        num1, num2 = leValores()
        if num1 is None or num2 is None:
            print("Encerrando calculadora...")
            break

        operacao = input('Escolha uma operação (+, -, *, /, ^) ou "sair" para sair: ')
        if operacao.lower() == "sair":
            print("Encerrando calculadora...")
            break

        match operacao:
            case '+':
                print(adicionar(num1, num2))
            case '-':
                print(subtrair(num1, num2))
            case '*':
                print(multiplicar(num1, num2))
            case '/':
                print(dividir(num1, num2))
            case '^':
                print(elevar(num1, num2))
            case _:
                print("Operação inválida! Tente novamente.")

def leValores():
    """Lê dois valores do usuário e converte para float."""
    try:
        valor1 = input('Digite um número (ou "sair" para encerrar): ')
        if valor1.lower() == 'sair':
            return None, None

        valor2 = input('Digite outro número: ')
        if valor2.lower() == 'sair':
            return None, None

        return float(valor1), float(valor2)
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return leValores()  # Tenta novamente

def adicionar(num1, num2):
    return f'Resultado: {num1 + num2}'

def subtrair(num1, num2):
    return f'Resultado: {num1 - num2}'

def multiplicar(num1, num2):
    return f'Resultado: {num1 * num2}'

def dividir(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero!"
    return f'Resultado: {num1 / num2}'

def elevar(num1, num2):
    return f'Resultado: {num1 ** num2}'

# Executa a calculadora
main()