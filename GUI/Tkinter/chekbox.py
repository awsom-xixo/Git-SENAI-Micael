import tkinter as tk

janela = tk.Tk()
emails_promocionais = tk.IntVar() # Assumirá valor 0 quando desmarcado e 1 quando marcado. 
termos_deUso = tk.IntVar()

def enviar():
    if emails_promocionais.get():
        print('Usuário deseja receber emails promocionais')

    else:
        print('Usuário NÃO deseja receber emails promocionais')

    if termos_deUso.get():
        print('Usuário aceita os termos de uso e política de privacidade')

    else:
        print('Usuário NÃO aceita os termos de uso e política de privacidade')

checkbox_promocoes = tk.Checkbutton(text='Deseja receber emails promocionais?', variable=emails_promocionais)
checkbox_promocoes.grid(row=0, column=0)

checkbox_termos = tk.Checkbutton(text='Li, concordo e aceito seguir os Termos de Uso da Aplicação\n assim como concordo com a política de privacidade', variable=termos_deUso)
checkbox_termos.grid(row=1, column=0)

botao_enviar = tk.Button(text='ENVIAR', command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()