import tkinter as tk
from tkinter import messagebox
import math

# Colores y estilos
BG_COLOR = "#2C3E50"  # Azul oscuro
BTN_COLOR = "#ECF0F1"  # Blanco grisáceo
BTN_HOVER = "#BDC3C7"  # Gris claro
FONT = ("Arial", 18, "bold")
ENTRY_BG = "#34495E"  # Azul grisáceo
ENTRY_FG = "#ECF0F1"  # Blanco grisáceo

# Variable para controlar si la entrada debe limpiarse automáticamente
limpiar_auto = False

# Función para evaluar la expresión ingresada
def calcular():
    global limpiar_auto
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
        limpiar_auto = True  # Habilitar el borrado automático para la siguiente operación
    except Exception:
        messagebox.showerror("Error", "Expresión no válida")

# Función para calcular la raíz cuadrada
def raiz_cuadrada():
    global limpiar_auto
    try:
        numero = float(entrada.get())
        if numero < 0:
            messagebox.showerror("Error", "No se puede calcular la raíz de un número negativo")
            return
        resultado = math.sqrt(numero)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
        limpiar_auto = True
    except Exception:
        messagebox.showerror("Error", "Ingrese un número válido")

# Función para calcular exponentes
def exponente():
    agregar_texto("**")

# Función para agregar texto a la entrada
def agregar_texto(texto):
    global limpiar_auto
    if limpiar_auto:
        entrada.delete(0, tk.END)
        limpiar_auto = False  # Desactivar el borrado automático después de escribir
    entrada.insert(tk.END, texto)

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Elegante")
ventana.geometry("350x600")
ventana.resizable(False, False)
ventana.configure(bg=BG_COLOR)

# Entrada para mostrar la expresión
entrada = tk.Entry(ventana, font=FONT, justify="right", bd=10, bg=ENTRY_BG, fg=ENTRY_FG)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipadx=8, ipady=8)

# Botones
botones = [
    ('7', 1, 0), 
    ('8', 1, 1), 
    ('9', 1, 2), 
    ('/', 1, 3),
    ('4', 2, 0), 
    ('5', 2, 1), 
    ('6', 2, 2), 
    ('*', 2, 3),
    ('1', 3, 0), 
    ('2', 3, 1), 
    ('3', 3, 2), 
    ('-', 3, 3),
    ('C', 4, 0), 
    ('0', 4, 1), 
    ('=', 4, 2), 
    ('+', 4, 3),
    ('√', 5, 0),  # Botón para raíz cuadrada
    ('^', 5, 1)   # Botón para exponentes
]

# Crear y posicionar los botones
for (texto, fila, columna) in botones:
    def crear_comando(t=texto):
        if t == '=':
            return calcular
        elif t == 'C':
            return limpiar
        elif t == '√':
            return raiz_cuadrada
        elif t == '^':
            return exponente
        else:
            return lambda: agregar_texto(t)
    
    boton = tk.Button(
        ventana, 
        text=texto, 
        font=FONT, 
        bg=BTN_COLOR, 
        fg="#2C3E50", 
        activebackground=BTN_HOVER, 
        activeforeground="#2C3E50",
        command=crear_comando(), 
        relief="raised", 
        bd=5
    )
    boton.grid(
        row=fila, 
        column=columna, 
        sticky="nsew", 
        padx=5, 
        pady=5, 
        ipadx=10, 
        ipady=10
    )

# Configuración del tamaño de las filas y columnas
for i in range(6):  # Se aumentó a 6 para incluir los nuevos botones
    ventana.grid_rowconfigure(i, weight=1)

for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

# Ejecutar la aplicación
ventana.mainloop()



