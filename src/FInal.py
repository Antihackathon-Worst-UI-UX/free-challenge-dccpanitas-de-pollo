import tkinter as tk
from tkinter import messagebox
from calculator import sumar, restar, multiplicacion, dividir
from binarizador import binarizador

def mostrar_error():
    error_img = tk.PhotoImage(file="MISH.png")
    label_error.config(image=error_img)
    label_error.image = error_img
    salida.config(text="")

def calcular():
    try:
        n1_str = entrada_num1.get()
        n2_str = entrada_num2.get()

        if not (n1_str.isdigit() and n2_str.isdigit()) or len(n1_str) > 2 or len(n2_str) > 2:
            mostrar_error()
            return
        
        n1 = int(n1_str)
        n2 = int(n2_str)
        op = operacion.get()
        
        if op == "+":
            resultado = sumar(n1, n2)
        elif op == "-":
            resultado = restar(n1, n2)
        elif op == "*":
            resultado = multiplicacion(n1, n2)
        elif op == "/":
            resultado = dividir(n1, n2)
        else:
            salida.config(text="Que haces chaval?")
            return

        binario = binarizador(int(resultado))
        salida.config(text=f"Burunya! {binario}")
        label_error.config(image="")
    except Exception as e:
        salida.config(text=f"Error: {e}")

ventana = tk.Tk()
ventana.title("Max 2 numeros :v")

logo = tk.PhotoImage(file="marciano.png")
ventana.iconphoto(False, logo)

tk.Label(ventana, text="Si es niño: Tom ->").grid(row=0, column=0)
entrada_num1 = tk.Entry(ventana)
entrada_num1.grid(row=0, column=1)

tk.Label(ventana, text="Si es niña: Nook ->").grid(row=1, column=0)
entrada_num2 = tk.Entry(ventana)
entrada_num2.grid(row=1, column=1)

tk.Label(ventana, text="operacionlay (+,-,*,/):").grid(row=2, column=0)
operacion = tk.Entry(ventana)
operacion.grid(row=2, column=1)

tk.Button(ventana, text="Raluclac", command=calcular).grid(row=3, column=0, columnspan=2, pady=5)

salida = tk.Label(ventana, text="", font=("Arial", 12))
salida.grid(row=4, column=0, columnspan=2)

label_error = tk.Label(ventana)
label_error.grid(row=5, column=0, columnspan=2)

ventana.mainloop()