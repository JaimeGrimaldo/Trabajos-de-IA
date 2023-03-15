import pandas as pd
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt

ventana = Tk()
ventana.title("Red neuronal")

textoIngresarTaza = Label(ventana, font=("Arial 15"), text="Ingresar taza de aprendizaje:")
textoIngresarError = Label(ventana, font=("Arial 15"), text="Ingresar error de tolerancia:")
entradaTaza = Entry(ventana,font=("Arial 15"))
entradaError = Entry(ventana,font=("Arial 15"))

textoIngresarTaza.grid(row=0, column=0, columnspan=1, padx=5,pady=10)
textoIngresarError.grid(row=1, column=0, columnspan=1, padx=5,pady=10)
entradaTaza.grid(row=0, column=1, columnspan=1, padx=5,pady=10)
entradaError.grid(row=1, column=1, columnspan=1, padx=5,pady=10)

#holi

evolucionError = []
def linear(u):
    return u

def Perceptron(X,W):
    u = X.dot(W)
    return linear(u)

def Entrenar(X,W, taza_aprendizaje, yd):
    global evolucionError
    epocas = 100
    norm_err = 1
    tolerancia = float(entradaError.get())
    Wk = W
    """""
    while norm_err > tolerancia:
        yc = Perceptron(X,Wk)   
        ek = yd - yc
        norm_err = np.linalg.norm(ek)
        evolucionError.append(norm_err)
        Wk = Wk  + (taza_aprendizaje*(ek.dot(X)))
    """""
    for i in range(epocas):
        yc = Perceptron(X,Wk)   
        ek = yd - yc
        norm_err = np.linalg.norm(ek)
        evolucionError.append(norm_err)
        Wk = Wk  + (taza_aprendizaje*(ek.dot(X)))
    return Wk, yc

def GenerarGrafica(evolucionError,wf):
    plt.title(f'Coordenadas del mejor caso: X ={wf}')
    plt.plot(evolucionError, label="Mejor", color="Blue")
    plt.xlabel("Generaciones")
    plt.ylabel("Evolucion del Fitness")
    plt.ioff()
    plt.ion()
    plt.legend()
    plt.show()

def LeerArchivo():
    global evolucionError
    df = pd.read_csv('191214.csv')
    x1 =df['x1'].to_numpy()
    x2 =df['x1'].to_numpy()
    x3 =df['x1'].to_numpy()
    Y_s =df['y'].to_numpy()
    tazaAprendizaje = float(entradaTaza.get())
    bias =  np.ones(len(x1))
    W = np.random.uniform(-1,1,4)
    ENTRADAS = np.array([x1,x2,x3,bias])
    WF, y_f = Entrenar(ENTRADAS.T,W,tazaAprendizaje,Y_s)
    GenerarGrafica(evolucionError,WF)
    print('Pesos finales:', WF)
    
#if __name__ == '__main__':

boton = Button(ventana, text="Entrenar", width=10, height=1, font=("Arial 12"), command = lambda: LeerArchivo())
boton.grid(row=2, column=0, columnspan=3)
ventana.mainloop()
