# Função para exibir uma mensagem de boas-vindas personalizada
def exibir_boas_vindas(nome):
    mensagem = f"Hello, {nome}! Welcome to the world of Python."
    print(mensagem)
    print("-" * len(mensagem))  # Adiciona uma linha abaixo da mensagem com o mesmo comprimento

# Função principal do programa
def main():
    # Solicita o nome do usuário
    nome_usuario = input("Por favor, insira seu nome: ")
    
    # Exibe a mensagem de boas-vindas
    exibir_boas_vindas(nome_usuario)
    
    # Exibe uma mensagem adicional
    print("\nAqui estão algumas informações legais sobre Python:")
    print("1. Python é uma linguagem de programação poderosa e fácil de aprender.")
    print("2. Python suporta vários paradigmas de programação.")
    print("3. A comunidade Python é uma das maiores e mais acolhedoras.")
    print("\nDivirta-se explorando o mundo de Python!")

# Executa o programa principal
if __name__ == "__main__":
    main()