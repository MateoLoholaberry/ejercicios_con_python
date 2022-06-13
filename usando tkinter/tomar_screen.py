import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import time


# Interfaz

def crear_widget():
    etiquetaGuardar = Label(vn, text="Guardar como: ", font=("", 10, "bold"))
    etiquetaGuardar.grid(row=0, column=0, padx=5, pady=5)

    vn.textoGuardar = Entry(vn, width=30)
    vn.textoGuardar.grid(row=0, column=1, padx=5, pady=5)

    botonGuardar = Button(vn, text="Buscar", width=10, command=navegar)
    botonGuardar.grid(row=0, column=2, padx=5, pady=5)

    botonCaptura = Button(vn, text="Capturar pantalla", width=20, command=captura)
    botonCaptura.grid(row=1, column=1, padx=5, pady=5)


# Función para navegar o buscar entre los ficheros y guardar la imagen
def navegar():
    vn.archivoNombre=filedialog.asksaveasfilename(title="Guardar como", initialdir="C:\\Users\\Usuario\\Desktop", defaultextension=".png", filetypes= (("Archivo Png", "*.png"), ("Todos los archivos", "*.*")))

    vn.textoGuardar.insert("1", vn.archivoNombre)


def captura():
    vn.iconify()
    time.sleep(0.5)
    captura = pyautogui.screenshot()
    captura.save(vn.archivoNombre)
    messagebox.showinfo("Exito", "Captura guardada")


vn = tk.Tk()
vn.title("Captura de pantalla")
crear_widget()

vn.mainloop()