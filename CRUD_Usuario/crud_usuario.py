import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database

def atualizar_tabela():
    for row in tabela.get_children():
        tabela.delete(row)
    usuarios = database.listar_usuarios()
    for usuario in usuarios:
        tabela.insert("", "end", values=usuario)

def novo_usuario():
    nome = input_nome.get()
    email = input_email.get()
    endereco = input_endereco.get()

    if nome == "" or email == "" or endereco == "":
        messagebox.showwarning("AVISO", "Nome, Email e Endereço são Obrigatórios")
        return

    database.inserir_usuario(nome, email, endereco)
    limpar_campos()
    atualizar_tabela()

def editar_usuario():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecionar um Usuário")
        return
    
    id = input_id.get()
    nome = input_nome.get()
    email = input_email.get()
    endereco = input_endereco.get()

    database.atualizar_usuario(id, nome, email, endereco)
    limpar_campos()
    atualizar_tabela()

def deletar_usuario():
    selecionado = tabela.selection()
    if not selecionado: 
        messagebox.showwarning("Aviso", "Selecionar um Usuário")
        return
    
    valores = tabela.item(selecionado, "values")
    id = valores[0]
    
    reposta = messagebox.askyesno("Aviso","Deseja Deletar o Usuário")
    if reposta:
        database.excluir_usuario(id)
        limpar_campos()
        atualizar_tabela()

def selecionar_usuario(event):
    selecinado = tabela.selection()
    if selecinado:
        limpar_campos()
        valores = tabela.item(selecinado, "values")
        input_id.insert(0, valores[0])
        input_nome.insert(0, valores[1])
        input_email.insert(0, valores[2])
        input_endereco.insert(0, valores[3])

def limpar_campos():
    input_id.delete(0, tk.END)
    input_nome.delete(0, tk.END)
    input_email.delete(0, tk.END)
    input_endereco.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Usuario (MySQL)")
janela.geometry("750x450")

frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

tk.Label(frame_form, text="ID: ").grid(row=0, column=0, padx=5, sticky="e")
input_id = tk.Entry(frame_form, width=20)
input_id.grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Nome:").grid(row=0, column=2, padx=5, sticky="e")
input_nome = tk.Entry(frame_form, width=40)
input_nome.grid(row=0, column=3, padx=5)

tk.Label(frame_form, text="Email:").grid(row=1, column=0, padx=5, sticky="e")
input_email = tk.Entry(frame_form, width=20)
input_email.grid(row=1, column=1, padx=5)

tk.Label(frame_form, text="Endereço:").grid(row=1, column=2, padx=5, sticky="e")
input_endereco = tk.Entry(frame_form, width=40)
input_endereco.grid(row=1, column=3, padx=5)

frame_botao = tk.Frame(janela)
frame_botao.pack(pady=10)

tk.Button(frame_botao, text="Novo", width=10, command=novo_usuario).grid(row=0, column=0, padx=5)
tk.Button(frame_botao, text="Editar", width=10, command=editar_usuario).grid(row=0, column=1, padx=5)
tk.Button(frame_botao, text="Excluir", width=10, command=deletar_usuario).grid(row=0, column=2, padx=5)
tk.Button(frame_botao, text="Limpar", width=10, command=limpar_campos).grid(row=0, column=3, padx=5)

colunas = ("ID", "NOME", "EMAIL", "ENDERECO")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=170)

tabela.pack(fill="both", expand=True, padx=20, pady=20)
tabela.bind("<<TreeviewSelect>>", selecionar_usuario)

atualizar_tabela()

janela.mainloop()