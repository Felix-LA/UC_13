import tkinter as tk
from tkinter import messagebox
from random import randrange

janela = tk.Tk()
janela.title("Jogo da Velha")
janela.geometry("300x400")

tabuleiro = []
botoes = []
modoJogo = None
jogadorAtual = "O"


def CriarTabuleiro():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]


def draw_board():
    for i in range(3):
        for j in range(3):
            valor = tabuleiro[i][j]
            if valor in ["X", "O"]:
                botoes[i][j]["text"] = valor
                botoes[i][j]["state"] = "disabled"
    


def ChecarVencedor():
    linhas = []

    linhas.extend(tabuleiro)

    for c in range(3):
        linhas.append([
            tabuleiro[0][c],
            tabuleiro[1][c],
            tabuleiro[2][c]
        ])

    linhas.append([
        tabuleiro[0][0],
        tabuleiro[1][1],
        tabuleiro[2][2]
    ])

    linhas.append([
        tabuleiro[0][2],
        tabuleiro[1][1],
        tabuleiro[2][0]
    ])

    for linha in linhas:
        if linha == ["X", "X", "X"]:
            return "X"
        if linha == ["O", "O", "O"]:
            return "O"

    cheio = True

    for linha in tabuleiro:
        for item in linha:
            if item not in ["X", "O"]:
                cheio = False

    if cheio:
        return "Empate"

    return None


def MovimentoJogador(linha, coluna):
    global jogadorAtual

    if tabuleiro[linha][coluna] in ["X", "O"]:
        return

    tabuleiro[linha][coluna] = jogadorAtual
    draw_board()

    vencedor = ChecarVencedor()

    if vencedor:
        mostrar_resultado(vencedor)
        return

    if modoJogo == "computador":
        MovimentoComputador()
    else:
        jogadorAtual = "X" if jogadorAtual == "O" else "O"


def MovimentoComputador():
    livres = []

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] not in ["X", "O"]:
                livres.append((i, j))

    if not livres:
        return

    i, j = livres[randrange(len(livres))]
    tabuleiro[i][j] = "X"

    draw_board()

    vencedor = ChecarVencedor()

    if vencedor:
        mostrar_resultado(vencedor)


def voltar_menu():
    frame_jogo.pack_forget()
    frame_menu.pack(pady=20)


def mostrar_resultado(vencedor):

    if vencedor == "Empate":
        mensagem = "Deu empate!"

    elif modoJogo == "computador":
        if vencedor =="X":
            mensagem = "O Computador Venceu!"
        else:
            mensagem = "O Jogador Venceu!"
            
    else:
        if vencedor == "X":
            mensagem = "Jogador 2 Venceu"
        else:
            mensagem = "Jogador 1 Venceu"
                

    messagebox.showinfo("Fim do jogo", mensagem)
    reiniciar()

    jogar_novamente = messagebox.askyesno(
        "Fim do jogo",
        mensagem + "\n\nDeseja jogar novamente?"
    )

    if jogar_novamente:
        voltar_menu()
    else:
        janela.destroy()


def reiniciar():
    global tabuleiro, jogadorAtual

    tabuleiro = CriarTabuleiro()
    jogadorAtual = "O"

    for i in range(3):
        for j in range(3):
            botoes[i][j]["text"] = ""
            botoes[i][j]["state"] = "normal"

    if modoJogo == "computador":
        tabuleiro[1][1] = "X"
        
    draw_board()


def escolher_computador():
    global modoJogo
    modoJogo = "computador"
    iniciar_jogo()


def escolher_jogador():
    global modoJogo
    modoJogo = "2jogadores"
    iniciar_jogo()


def iniciar_jogo():
    global tabuleiro, jogadorAtual

    frame_menu.pack_forget()
    frame_jogo.pack()

    tabuleiro = CriarTabuleiro()
    jogadorAtual = "O"

    if modoJogo == "computador":
        tabuleiro[1][1] = "X"

    draw_board()
    

frame_menu = tk.Frame(janela)
frame_menu.pack(pady=20)

tk.Label(frame_menu, text="Escolha o modo de jogo").pack(pady=10)

tk.Button(
    frame_menu,
    text="Contra Computador",command=escolher_computador,width=20).pack(pady=5)

tk.Button(
    frame_menu,text="2 Jogadores",command=escolher_jogador,width=20).pack(pady=5)



frame_jogo = tk.Frame(janela)

for i in range(3):
    frame_jogo.rowconfigure(i, weight=1)
    frame_jogo.columnconfigure(i, weight=1)

for i in range(3):
    linha = []
    for j in range(3):
        botao = tk.Button(
            frame_jogo,
            text="",width=3,height=1,font=("Arial", 28, "bold"),borderwidth=3, relief="solid",command=lambda i=i, j=j: MovimentoJogador(i, j))

        botao.grid(row=i, column=j, sticky="nsew")
        linha.append(botao)

    botoes.append(linha)


janela.mainloop()