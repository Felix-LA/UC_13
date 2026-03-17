import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x200")



def calculo():
    try:
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        operacao = EntradaOperacao.get()

        if operacao == "+":
            calcular = valor1 + valor2
        elif operacao == "-":
            calcular = valor1 - valor2
        elif operacao == "*":
           calcular = valor1 * valor2
        elif operacao == "/":
            calcular = valor1 / valor2

        result.config(text=f"Resultado: {calcular}")
    except:
        result.config(text=f"Informe Numeros Validos")
    


num1 = tk.Label(janela, text="Inserir Variável: ")
num1.grid(row=0, column=0,padx=10,pady=10,sticky="w")
entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1,padx=10,pady=10,sticky="w")


Labeloperacao = tk.Label(janela,text="Informe a operação: ")
Labeloperacao.grid(row=1, column=0,padx=10,pady=10,sticky="w")
EntradaOperacao = tk.Entry(janela)
EntradaOperacao.grid(row=1, column=1,padx=10,pady=10,sticky="w")

num2 = tk.Label(janela, text="Inserir Variável: ")
num2.grid(row=2, column=0,padx=10,pady=10,sticky="w")
entrada2 = tk.Entry(janela)
entrada2.grid(row=2, column=1,padx=10,pady=10,sticky="w")


result = tk.Label(janela, text="Resultado: ")
result.grid(row=4, column=0,padx=10,pady=10,sticky="w")

botao = tk.Button(janela,text="Calcular", command=calculo)
botao.grid(row=3, column=0,padx=10,pady=10,sticky="w")


janela.mainloop()
