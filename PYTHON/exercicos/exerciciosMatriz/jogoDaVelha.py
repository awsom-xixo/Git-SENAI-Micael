def verificarVitoria(tabuleiro, jogador):
    for linha in range(len(tabuleiro)):
        if all(tabuleiro[linha][coluna] == jogador for coluna in range(len(tabuleiro))):
            return print('verdadeiro')
        
        if all(tabuleiro[coluna][linha] == jogador for coluna in range(len(tabuleiro))):
            return print('verdadeiro')
        
    return print('falso') # Se nenhuma vitória for reconhecida

def imprimeTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ! ".join(linha))
        print(" - " * 3)
    print()

def verificaEmpate(tabuleiro):
    return all(tabuleiro[i][j] != " " for i in range(len(tabuleiro)) for j in  range(len(tabuleiro)))

def jogoDaVelha():
    tamanho = int(input('Qual o tamanho do tabuleiro? '))
    tabuleiro = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
    jogador = 'x'

    while True:
        imprimeTabuleiro(tabuleiro)
        if not (verificarVitoria(tabuleiro, jogador)):
            break

jogoDaVelha()
