from tkinter import *

ventana = Tk()

ventana.title("Calculadora")

i = 0

# Entrada
entrada = Entry(ventana, font=("Calibri 20"))
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


# Funciones
def click_boton(valor):
    global i
    entrada.insert(i, valor)
    i += 1


def borrar():
    entrada.delete(0, END)
    i = 0


def operar():
    ecuacion = entrada.get()
    resultado = eval(ecuacion)
    borrar()
    entrada.insert(0, resultado)

# Botones
boton1 = Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1))
boton2 = Button(ventana, text="2", width=5, height=2,  command=lambda: click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2,  command=lambda: click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2,  command=lambda: click_boton(4))
boton5 = Button(ventana, text="5", width=5, height=2,  command=lambda: click_boton(5))
boton6 = Button(ventana, text="6", width=5, height=2,  command=lambda: click_boton(6))
boton7 = Button(ventana, text="7", width=5, height=2,  command=lambda: click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2,  command=lambda: click_boton(8))
boton9 = Button(ventana, text="9", width=5, height=2,  command=lambda: click_boton(9))
boton0 = Button(ventana, text="0", width=15, height=2,  command=lambda: click_boton(0))


boton_borrar = Button(ventana, text="AC", width=5, height=2,  command=lambda: borrar())
boton_parentesisis1 = Button(ventana, text="(", width=5, height=2,  command=lambda: click_boton("("))
boton_parentesisis2 = Button(ventana, text=")", width=5, height=2,  command=lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", width=5, height=2,  command=lambda: click_boton("."))

boton_division = Button(ventana, text="/", width=5, height=2,  command=lambda: click_boton("/"))
boton_multiplicacion = Button(ventana, text="x", width=5, height=2,  command=lambda: click_boton("*"))
boton_suma = Button(ventana, text="+", width=5, height=2,  command=lambda: click_boton("+"))
boton_resta = Button(ventana, text="-", width=5, height=2,  command=lambda: click_boton("-"))
boton_igual = Button(ventana, text="=", width=5, height=2,  command=lambda: operar())

# Agregar botones en pantalla

boton_borrar.grid(row=1, column=0, padx=3, pady=3)
boton_parentesisis1.grid(row=1, column=1, padx=3, pady=3)
boton_parentesisis2.grid(row=1, column=2, padx=3, pady=3)
boton_division.grid(row=1, column=3, padx=5, pady=5)
boton7.grid(row=2, column=0, padx=3, pady=3)
boton8.grid(row=2, column=1, padx=3, pady=3)
boton9.grid(row=2, column=2, padx=3, pady=3)
boton_multiplicacion.grid(row=2, column=3, padx=3, pady=3)
boton4.grid(row=3, column=0, padx=3, pady=3)
boton5.grid(row=3, column=1, padx=3, pady=3)
boton6.grid(row=3, column=2, padx=3, pady=3)
boton_suma.grid(row=3, column=3, padx=3, pady=3)
boton1.grid(row=4, column=0, padx=3, pady=3)
boton2.grid(row=4, column=1, padx=3, pady=3)
boton3.grid(row=4, column=2, padx=3, pady=3)
boton_resta.grid(row=4, column=3, padx=3, pady=3)

boton0.grid(row=5, column=0, columnspan=2, padx=3, pady=3)
boton_punto.grid(row=5, column=2, padx=3, pady=3)
boton_igual.grid(row=5, column=3, padx=3, pady=3)

ventana.mainloop()