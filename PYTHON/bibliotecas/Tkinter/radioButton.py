import tkinter as tk

janela = tk.Tk()
var_escolha = tk.StringVar()


def enviar():
    print(var_escolha.get())

botao_classeEconomica = tk.Radiobutton(text='Classe Econômica', variable=var_escolha, value='Classe Econômica')
botao_classeExecutiva = tk.Radiobutton(text='Classe Executiva', variable=var_escolha, value='Classe Executiva')
botao_primeiraClasse = tk.Radiobutton(text='Primeira Classe', variable=var_escolha, value='Primeira Classe')

botao_classeEconomica.grid(row=0, column=0)
botao_classeExecutiva.grid(row=0, column=1)
botao_primeiraClasse.grid(row=0, column=2)

botao_enviar = tk.Button(text='ENVIAR', command=enviar)
botao_enviar.grid(row=1, column=0)



janela.mainloop()