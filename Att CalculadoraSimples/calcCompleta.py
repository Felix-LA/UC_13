import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("200x280")

def calculo():
    try:
        resultado = eval(inputVisor.get())
        limpar()
        inputVisor.insert(0, str(resultado))

    except:
        limpar()
        inputVisor.insert(0, "ERRO")



def adicionar(valor):
    inputVisor.insert(tk.END, valor)


def limpar():
    inputVisor.delete(0, tk.END)

inputVisor = tk.Entry(janela, font=("arial",20),bd=5, width=12,justify="right")
inputVisor.grid(row=0,column=0,columnspan=4, padx=3, pady=3)

botoes = {
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
}

for(texto, linha , coluna) in botoes:
    if texto == "=":
        tk.Button(janela, text=texto, width=5,height=2, command=calculo
                  ).grid(row=linha,column=coluna,padx=2,pady=2)
    else:
        tk.Button(janela, text=texto, width=5,height=2, command=lambda t=texto : adicionar(t)
                  ).grid(row=linha,column=coluna,padx=2,pady=2)
        
botaoLimpar = tk.Button(janela, text="C", width=22,height=2,bg="red",fg="white", command=limpar)
botaoLimpar.grid(row=5,column=0,columnspan=4,padx=2,pady=2)




janela.mainloop()