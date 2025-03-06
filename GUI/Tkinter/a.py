import tkinter as tk
from tkinter import messagebox

# Lista global para armazenar os usuários cadastrados
usuarios = []

class Registro:
    def __init__(self, janela):
        # Configurações básicas da janela
        self.janela = janela
        self.janela.title("Registro de Usuário")
        self.janela.geometry("300x200")
        self.janela.config(background = "Light Blue")
        
        # Faz a configuração se manter a mesma não importa o tamanho da janela
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=1)

        # Campo para o nome de usuário
        tk.Label(janela, text="Nome de Usuário:").grid(row=0, column=0, columnspan=2, pady=5)
        self.usuario_entry = tk.Entry(janela)
        self.usuario_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)

        # Campo para a senha
        tk.Label(janela, text="Senha:").grid(row=2, column=0, columnspan=2, pady=5)
        self.senha_entry = tk.Entry(janela, show="*")  # Oculta a senha
        self.senha_entry.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10)

        # Botões para registrar e acessar a tela de login
        tk.Button(janela, text="Registrar", command=self.cadastrar_usuario).grid(row=4, column=0, sticky="ew", padx=5, pady=10)
        tk.Button(janela, text="Login", command=self.tela_login).grid(row=4, column=1, sticky="ew", padx=5, pady=10)

    def cadastrar_usuario(self):

        """Registra um novo usuário na lista global"""

        usuario = self.usuario_entry.get().strip()
        senha = self.senha_entry.get().strip()
        
        # Verifica se o nome de usuário foi preenchido
        if not usuario:
            messagebox.showerror("Erro", "Nome de usuário não pode ser vazio!")
            return
        
        # Verifica se o usuário já existe
        if any(p["usuario"] == usuario for p in usuarios):
            messagebox.showerror("Erro", "Usuário já existe! Escolha outro nome.")
            return
        
        # Verifica se a senha tem no mínimo 6 caracteres
        if len(senha) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres!")
            return
        
        # Adiciona o novo usuário à lista global
        usuarios.append({"usuario": usuario, "senha": senha})
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        
    def tela_login(self):
        """Fecha a tela de registro e abre a tela de login"""
        self.janela.destroy()
        janela = tk.Tk()
        Login(janela)
        janela.mainloop()



class Login:
    def __init__(self, janela):
        # Configurações básicas da janela de login
        self.janela = janela
        self.janela.title("Login de Usuário")
        self.janela.geometry("300x180")
        self.janela.config(background = "Light Green")

        # Configuração da grade para melhor alinhamento
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=1)

        # Campo para nome de usuário
        tk.Label(janela, text="Nome de Usuário:").grid(row=0, column=0, columnspan=2, pady=5)
        self.usuario_entry = tk.Entry(janela)
        self.usuario_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)

        # Campo para senha
        tk.Label(janela, text="Senha:").grid(row=2, column=0, columnspan=2, pady=5)
        self.senha_entry = tk.Entry(janela, show="*")
        self.senha_entry.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10)

        # Botão para validar o login
        tk.Button(janela, text="Entrar", command=self.verificar_conta).grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    
    def verificar_conta(self):
        """Verifica se o usuário e senha inseridos estão na lista global"""
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        
        # Procura o usuário na lista global
        for user in usuarios:
            if user["usuario"] == usuario and user["senha"] == senha:
                messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
                return

        # Se não encontrar, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")


# Executa o programa, iniciando pela tela de registro
if __name__ == "__main__":
    janela = tk.Tk()
    Registro(janela)
    janela.mainloop()
