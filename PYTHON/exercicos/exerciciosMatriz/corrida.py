import random

def imprimeTabela(tabela, cabecalho):
    print(" | ".join(cabecalho))
    print("-" * (len(" | ".join(cabecalho))))  # Linha de separação
    
    # Imprime a matriz de forma organizada
    for linha in tabela:
        # Map para garantir que todos os valores sejam impressos como strings
        print("    |    ".join(map(str, linha)))  

def mediaTabela(tabela):
    tabelaMedia = [sum(linha) / len(linha) for linha in tabela]

    for linha in tabelaMedia:
        print(linha, end='\n')


tabela = [[random.randint(120, 300) for _ in range(4)] for _ in range(4)]

cabecalho = ["Volta 1", "Volta 2", "Volta 3", "Volta 4"]
imprimeTabela(tabela, cabecalho)
print(f'\nMédia de cada piloto (s):')
mediaTabela(tabela)