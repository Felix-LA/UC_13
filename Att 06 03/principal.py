import tkinter as tk

janela = tk.Tk()

def abrir_janela_novo_usuario():
    janela_usuario = tk.Toplevel()
    janela_usuario.title("Novo Usuario")
    janela_usuario.geometry("350x300")

    tk.Label(janela_usuario, text="Nome: ").grid(row=0,column=0, padx=5, pady=5)
    input_nome = tk.Entry(janela_usuario, width=35)
    input_nome.grid(row=0,column=1,padx=10,pady=5)

    tk.Label(janela_usuario, text="Telefone: ").grid(row=1,column=0, padx=5, pady=5)
    input_telefone = tk.Entry(janela_usuario, width=35)
    input_telefone.grid(row=1,column=1,padx=10,pady=5)

    tk.Label(janela_usuario, text="E-mail: ").grid(row=2,column=0, padx=5, pady=5)
    input_email = tk.Entry(janela_usuario, width=35)
    input_email.grid(row=2,column=1,padx=10,pady=5)

    tk.Label(janela_usuario, text="Endereço: ").grid(row=3,column=0, padx=5, pady=5)
    input_endereço = tk.Entry(janela_usuario, width=35)
    input_endereço.grid(row=3,column=1,padx=10,pady=5)

    tk.Label(janela_usuario, text="RG: ").grid(row=4,column=0, padx=5, pady=5)
    input_rg = tk.Entry(janela_usuario, width=35)
    input_rg.grid(row=4,column=1,padx=10,pady=5)

    tk.Label(janela_usuario, text="RG: ").grid(row=5,column=0, padx=5, pady=5)
    input_cpf = tk.Entry(janela_usuario, width=35)
    input_cpf.grid(row=5,column=1,padx=10,pady=5)

    tk.Label(janela_usuario, text="Idade: ").grid(row=6,column=0, padx=5, pady=5)
    input_idade = tk.Entry(janela_usuario, width=35)
    input_idade.grid(row=6,column=1,padx=10,pady=5)

    def salvar_usuario():
        nome = input_nome.get()
        email = input_email.get()

        lista_usuario.insert(tk.END, f"{nome} - {email}")
        janela_usuario.destroy

    botao_salvar = tk.Button(janela_usuario, text="Salvar", command=salvar_usuario)
    botao_salvar.grid(row=7, column=1,padx=10, pady=5, sticky="e")


janela.title("Cadastro de Usuário")
janela.geometry("400x300")

menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Sair", command=janela.quit)

menu_usuario = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Usuario", menu=menu_usuario)
menu_usuario.add_command(label="Sair", command=janela.quit)

botao_cadastro = tk.Button(janela, text="Novo Cadastro", command=abrir_janela_novo_usuario)
botao_cadastro.grid(row=0, column=0, padx=10, pady=10, sticky="e")

lista_usuario = tk.Listbox(janela, width=60)
lista_usuario.grid(row=1, column=0, padx=10, pady=10)


janela.mainloop()

