import tkinter as tk
from tkinter import ttk


def init_window():
    window = tk.Tk()
    window.title('Calculadora')
    window.geometry('400x300')

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)
    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(window, text = 'ingrese primer numero')
    label_entrada1.grid(column=0,row=1)
    label_entrada2 = tk.Label(window, text = 'ingrese segundo numero')
    label_entrada2.grid(column=0,row=2)

    label_operador = tk.Label(window, text = 'Escoja un operador', font =('Arial bold',10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold',15))
    label_resultado.grid (column = 0, row = 5)

    boton = tk.Button(window,
                      command = lambda: click_calcular(
                          label_resultado,
                          entrada1.get (),
                          entrada2.get (),
                          combo_operadores.get()),
                      text= 'Calcular',
                      bg='purple',
                      fg='white')
    boton.grid(column = 1, row = 4)

##----------------------------------Los 3 widgets--

##1
    label_nombre = tk.Label(window, text = 'ingrese su nombre')
    label_nombre.grid(column=0,row=6)
    entrada_nombre = tk.Entry(window, width=20)
    entrada_nombre.grid(column=1, row=6)


##2
    label_apelldio = tk.Label(window, text = 'ingrese su apellido')
    label_apelldio.grid(column=0,row=7)
    entrada_apellido = tk.Entry(window, width=20)
    entrada_apellido.grid(column=1, row=7)
##3
    boton_salud = tk.Button(window,
                      command=lambda: click_saludo(
                          label_resultado,
                          entrada_nombre.get(),
                          entrada_apellido.get(),
                      ),
                      text='Saludo',
                      bg='black',
                      fg='red')
    boton_salud.grid(column=1, row=8)

    window.mainloop()

def calculadora(num1,num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        resultado = num1 ** num2

    return resultado

def click_calcular(label, num1, num2, operador):

    valor1 = float(num1)
    valor2 = float(num2)

    res = calculadora(valor1, valor2, operador)

    label.configure(text = 'Resultado: '+ str(res))

def click_saludo(label, num3, num4,):

    valor1 = str(num3)
    valor2 = str(num4)

    label.configure(text = 'Hola '+str(valor1)+' '+str(valor2))



def main():
    init_window()

main()
