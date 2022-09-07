from distutils.cmd import Command
import tkinter
from typing import final

#Componente raíz
raiz = tkinter.Tk()
raiz.title("Calculator")
raiz.geometry('410x300')
raiz.resizable(False,False)
raiz.configure(background='gray')

#Funciones
operacion = ""
resultado = tkinter.StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0,tkinter.END)

def pulsar(valor):
    global operacion
    global resultado
    operacion += str(valor)
    pantalla.delete(0, tkinter.END)
    pantalla.insert(0, operacion)

def calcular():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado="Error"
    finally:
        pantalla.delete(0, tkinter.END)
        pantalla.insert(0, resultado)
        operacion = resultado

#Display de los resultados:
pantalla = tkinter.Entry(raiz, font=('arial', 20, 'bold'), borderwidth=2)
pantalla.grid(row=0, column=0, columnspan=3, pady=10, padx = 5)

#Boton reset:
reset = tkinter.Button(raiz, text='AC', width=7, height=1, command=lambda:borrar())
reset.grid(row=0, column=3, padx=1, pady=3)

#Digitos:
boton1 = tkinter.Button(raiz, text="1", width=5, height=2, command=lambda:pulsar(1))
boton1.config(fg="orange")
boton1.grid(row=1, column=0, columnspan=1, padx=1, pady=3)
boton2 = tkinter.Button(raiz, text="2", width=5, height=2, command=lambda:pulsar(2))
boton2.config(fg="orange")
boton2.grid(row=1, column=1, columnspan=1, padx=1, pady=3)
boton3 = tkinter.Button(raiz, text="3", width=5, height=2, command=lambda:pulsar(3))
boton3.config(fg="orange")
boton3.grid(row=1, column=2, columnspan=1, padx=1, pady=3)
boton4 = tkinter.Button(raiz, text="4", width=5, height=2, command=lambda:pulsar(4))
boton4.config(fg="orange")
boton4.grid(row=2, column=0, columnspan=1, padx=1, pady=3)
boton5 = tkinter.Button(raiz, text="5", width=5, height=2, command=lambda:pulsar(5))
boton5.config(fg="orange")
boton5.grid(row=2, column=1, columnspan=1, padx=1, pady=3)
boton6= tkinter.Button(raiz, text="6", width=5, height=2, command=lambda:pulsar(6))
boton6.config(fg="orange")
boton6.grid(row=2, column=2, columnspan=1, padx=1, pady=3)
boton7 = tkinter.Button(raiz, text="7", width=5, height=2, command=lambda:pulsar(7))
boton7.config(fg="orange")
boton7.grid(row=3, column=0, columnspan=1, padx=1, pady=3)
boton8 = tkinter.Button(raiz, text="8", width=5, height=2, command=lambda:pulsar(8))
boton8.config(fg="orange")
boton8.grid(row=3, column=1, columnspan=1, padx=1, pady=3)
boton9 = tkinter.Button(raiz, text="9", width=5, height=2, command=lambda:pulsar(9))
boton9.config(fg="orange")
boton9.grid(row=3, column=2, columnspan=1, padx=1, pady=3)
boton0 = tkinter.Button(raiz, text="0", width=5, height=2, command=lambda:pulsar(0))
boton0.config(fg="orange")
boton0.grid(row=4, column=0, columnspan=1, padx=1, pady=3)

#Operaciones
botoncoma = tkinter.Button(raiz, text=".", width=5, height=2, command=lambda:pulsar("."))
botoncoma.config(fg="orange")
botoncoma.grid(row=4, column=1, columnspan=1, padx=1, pady=3)

botonequal = tkinter.Button(raiz, text="=", width=5, height=2, command=lambda:calcular())
botonequal.config(fg="orange")
botonequal.grid(row=4, column=2, columnspan=1, padx=1, pady=3)

botonsum = tkinter.Button(raiz, text="+", width=5, height=2, command=lambda:pulsar("+"))
botonsum.config(fg="orange")
botonsum.grid(row=1, column=3, columnspan=1, padx=1, pady=3)

botondif = tkinter.Button(raiz, text="-", width=5, height=2, command=lambda:pulsar("-"))
botondif.config(fg="orange")
botondif.grid(row=2, column=3, columnspan=1, padx=1, pady=3)

botonmult = tkinter.Button(raiz, text="x", width=5, height=2, command=lambda:pulsar("*"))
botonmult.config(fg="orange")
botonmult.grid(row=3, column=3, columnspan=1, padx=1, pady=3)

botondiv = tkinter.Button(raiz, text="/", width=5, height=2, command=lambda:pulsar("/"))
botondiv.config(fg="orange")
botondiv.grid(row=4, column=3, columnspan=1, padx=1, pady=3)

raiz.mainloop()