import tkinter as tk
from tkinter import ttk

# +----------------------------------------+
# + ESSE CÓDIGO AINDA PRECISA DE MELHORIAS +
# +----------------------------------------+

dict_deCotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

def buscar_cotacao():
    global dict_deCotacoes
    moeda_preenchida = moeda.get()
    cotacaoMoeda = dict_deCotacoes.get(moeda_preenchida)
    # Aqui você garante que só tenha uma label
    if hasattr(buscar_cotacao, 'mensagem_cotacao'): 
        buscar_cotacao.mensagem_cotacao.destroy()
    
    buscar_cotacao.mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    buscar_cotacao.mensagem_cotacao.grid(row=3, column=0)

    if cotacaoMoeda:
        buscar_cotacao.mensagem_cotacao['text'] = f'Cotação do {moeda_preenchida} é de R${cotacaoMoeda}'

def buscar_cotacoes():
    texto = caixa_texto.get('1.0', tk.END)
    lista_deMoedas = texto.split('\n')  # Corrigido para dividir corretamente por nova linha
    mensagem_cotacoes = []
    for item in lista_deMoedas:
        cotacao = dict_deCotacoes.get(item) 
        if cotacao:
            mensagem_cotacoes.append(f'{item}:{cotacao}')
    mensagem3 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem3.grid(row=6, column=1)

botao_multiplascotacoes = tk.Button(text='Buscar Cotações', command=buscar_cotacoes)
botao_multiplascotacoes.grid(row=5, column=1)

janela = tk.Tk()
janela.title('Cotação de Moedas')
# Faz a configuração se manter a mesma não importa o tamanho da janela
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

mensagem = tk.Label(text='Sistema de Busca de Cotação de Moedas', fg='white', bg='black', width=30, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky='nsew')

mensagem1 = tk.Label(text='Selecione a moeda desejada:', height=3)
mensagem1.grid(row=1, column=0)

mensagem2 = tk.Label(text='Caso você queira pegar mais de uma cotação ao mesmo tempo, basta digitar uma moeda em cada linha')
mensagem2.grid(row=3, column=0, columnspan=2)

botao_deBusca = tk.Button(text='Buscar Cotação', command=buscar_cotacao)  # Botão que interage com a função 'buscar_cotacao'
botao_deBusca.grid(row=2, column=1)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky='nsew')

# Cria uma lista suspensa com as chaves do dicionário
moedas = list(dict_deCotacoes.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

janela.mainloop()
