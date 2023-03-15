from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import os

evolucionError1 = []
evolucionError2 = []
evolucionError3 = []
evolucionError4 = []
evolucionError5 = []

def perceptron_ds_2():
    df = pd.read_csv('dataset.csv')
    x1 =df['X1'].to_numpy()
    Y_s =df['Y'].to_numpy()
    X_s = np.array([x1]).T
    
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1,input_dim=3,activation='linear', kernel_initializer='glorot_uniform',bias_initializer='ones'))
    alpha = 0.1
    model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(alpha))
    model.fit(X_s, Y_s, epochs=150,batch_size=25,verbose=False)
    
    W_F = model.get_weights()
    yc = model.predict(X_s)

    return W_F, yc


def PerceptronTenser1(file):
    print(f"esto es file {file}")
    df = pd.read_csv(file)
    X1 =df['x1'].to_numpy()
    X2 =df['x2'].to_numpy()
    X3 =df['x3'].to_numpy()
    Y_s =df['y'].to_numpy()
    alpha = 0.1
    epocas = 100
    X_s = np.array([X1,X2,X3]).T
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1,input_dim=3,activation='linear', kernel_initializer='glorot_uniform',bias_initializer='ones'))
    model.compile(loss = 'mean_squared_error',optimizer=tf.keras.optimizers.Adam(alpha),metrics=["accuracy"])
    modelado = model.fit(X_s, Y_s, epochs=epocas, batch_size=25,verbose=False)
    
    W_F = model.get_weights()
    yc = model.predict(X_s)

    return W_F, yc, modelado, Y_s

def PerceptronTenser2(file):
    print(f"esto es file {file}")
    df = pd.read_csv(file)
    X1 =df['x1'].to_numpy()
    X2 =df['x2'].to_numpy()
    X3 =df['x3'].to_numpy()
    Y_s =df['y'].to_numpy()
    alpha = 0.1
    epocas = 100
    X_s = np.array([X1,X2,X3]).T
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1,input_dim=3,activation='linear', kernel_initializer='glorot_uniform',bias_initializer='ones'))
    model.compile(loss = 'mean_squared_error',optimizer=tf.keras.optimizers.Adam(alpha),metrics=["accuracy"])
    modelado = model.fit(X_s, Y_s, epochs=epocas, batch_size=25,verbose=False)
    
    W_F = model.get_weights()
    yc = model.predict(X_s)

    return modelado

def PerceptronTenser3(file):
    print(f"esto es file {file}")
    df = pd.read_csv(file)
    X1 =df['x1'].to_numpy()
    X2 =df['x2'].to_numpy()
    X3 =df['x3'].to_numpy()
    Y_s =df['y'].to_numpy()
    alpha = 0.1
    epocas = 100
    X_s = np.array([X1,X2,X3]).T
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1,input_dim=3,activation='linear', kernel_initializer='glorot_uniform',bias_initializer='ones'))
    model.compile(loss = 'mean_squared_error',optimizer=tf.keras.optimizers.Adam(alpha),metrics=["accuracy"])
    modelado = model.fit(X_s, Y_s, epochs=epocas, batch_size=25,verbose=False)
    
    W_F = model.get_weights()
    yc = model.predict(X_s)

    return modelado

def PerceptronTenser4(file):
    print(f"esto es file {file}")
    df = pd.read_csv(file)
    X1 =df['x1'].to_numpy()
    X2 =df['x2'].to_numpy()
    X3 =df['x3'].to_numpy()
    Y_s =df['y'].to_numpy()
    alpha = 0.1
    epocas = 100
    X_s = np.array([X1,X2,X3]).T
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1,input_dim=3,activation='linear', kernel_initializer='glorot_uniform',bias_initializer='ones'))
    model.compile(loss = 'mean_squared_error',optimizer=tf.keras.optimizers.Adam(alpha),metrics=["accuracy"])
    modelado = model.fit(X_s, Y_s, epochs=epocas, batch_size=25,verbose=False)
    
    W_F = model.get_weights()
    yc = model.predict(X_s)

    return modelado

def PerceptronTenser5(file):
    print(f"esto es file {file}")
    df = pd.read_csv(file)
    X1 =df['x1'].to_numpy()
    X2 =df['x2'].to_numpy()
    X3 =df['x3'].to_numpy()
    Y_s =df['y'].to_numpy()
    alpha = 0.1
    epocas = 100
    X_s = np.array([X1,X2,X3]).T
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1,input_dim=3,activation='linear', kernel_initializer='glorot_uniform',bias_initializer='ones'))
    model.compile(loss = 'mean_squared_error',optimizer=tf.keras.optimizers.Adam(alpha),metrics=["accuracy"])
    modelado = model.fit(X_s, Y_s, epochs=epocas, batch_size=25,verbose=False)
    
    W_F = model.get_weights()
    yc = model.predict(X_s)

    return modelado

def GraficarYs(YcTenser,modelado,Y_s, yAlgebra):
    global evolucionError
    plt.title("Resultados comparativos")
    plt.plot(YcTenser, label="TenserFlow", color="Blue")
    #plt.plot(modelado.history["loss"], label="TenserFlow", color="Blue")
    plt.plot(yAlgebra, label="Algebra Líneal", color="Red")
    plt.plot(Y_s, label="Y deseada", color="Gray")
    #plt.xlim(0,100)
    #plt.ylim(0,1000)
    plt.xlabel("Epocas")
    plt.ylabel("Involución del error")
    #plt.ion()
    plt.legend()
    plt.show()

def GraficarErroresAlgebra():
    global evolucionError1, evolucionError2, evolucionError3, evolucionError4
    plt.title("Resultados de errores usando Algebra Lineal")
    plt.plot(evolucionError1, label="Error 1", color="Blue")
    plt.plot(evolucionError2, label="Error 2", color="Red")
    plt.plot(evolucionError3, label="Error 3", color="Green")
    plt.plot(evolucionError4, label="Error 4", color="Orange")
    plt.plot(evolucionError5, label="Error 5", color="Gray")
    plt.xlabel("Epocas")
    plt.ylabel("Error")
    plt.legend()
    plt.show()

def GraficarErroresTenser(modelado,modelado2,modelado3,modelado4,modelado5):
    plt.title("Errores de Tenser")
    plt.plot(modelado.history["loss"], label="Error: 1",color="Blue")
    plt.plot(modelado2.history["loss"], label="Error: 2",color="Red")
    plt.plot(modelado3.history["loss"], label="Error: 3",color="Green")
    plt.plot(modelado4.history["loss"], label="Error: 4",color="Orange")
    plt.plot(modelado5.history["loss"], label="Error: 5",color="Yellow")
    plt.xlabel("Epocas")
    plt.ylabel("Involución del error")
    plt.legend()
    plt.show()



def linear(u):
    return u

def Perceptron(X,W):
    u = X.dot(W)
    return linear(u)

def Entrenar(X,W, taza_aprendizaje, yd):
    epocas = 100
    #global evolucionError
    norm_err = 1
    Wk = W
    for i in range(epocas):
        yc = Perceptron(X,Wk)   
        ek = yd - yc
        norm_err = np.linalg.norm(ek)
        #evolucionError.append(norm_err)
        Wk = Wk  + (taza_aprendizaje*(ek.dot(X)))
    return Wk, yc

def EntrenarVarios(X,W,W2,W3,W4,W5,taza1,yd):
    epocas = 100
    global evolucionError1, evolucionError2, evolucionError3, evolucionError4, evolucionError5
    norm_err = 1
    Wk = W
    Wk2 = W2
    Wk3 = W3
    Wk4 = W4
    Wk5 = W5
    for i in range(epocas):
        yc = Perceptron(X,Wk)   
        ek = yd - yc
        norm_err = np.linalg.norm(ek)
        evolucionError1.append(norm_err)
        Wk = Wk  + (taza1*(ek.dot(X)))

    for i in range(epocas):
        yc2 = Perceptron(X,Wk2)   
        ek = yd - yc2
        norm_err = np.linalg.norm(ek)
        evolucionError2.append(norm_err)
        Wk2 = Wk2  + (taza1*(ek.dot(X)))
    

    for i in range(epocas):
        yc3 = Perceptron(X,Wk3)   
        ek = yd - yc3
        norm_err = np.linalg.norm(ek)
        evolucionError3.append(norm_err)
        Wk3 = Wk3  + (taza1*(ek.dot(X)))

    for i in range(epocas):
        yc4 = Perceptron(X,Wk4)   
        ek = yd - yc4
        norm_err = np.linalg.norm(ek)
        evolucionError4.append(norm_err)
        Wk4 = Wk4  + (taza1*(ek.dot(X)))

    for i in range(epocas):
        yc5 = Perceptron(X,Wk5)   
        ek = yd - yc5
        norm_err = np.linalg.norm(ek)
        evolucionError5.append(norm_err)
        Wk5 = Wk5  + (taza1*(ek.dot(X)))
    return Wk, Wk2, Wk3, Wk4, Wk5, yc, yc2, yc3, yc4, yc5

def LeerArchivoAlgebra():
    global evolucionError
    df = pd.read_csv('191214.csv')
    X1 =df['x1'].to_numpy()
    X2 = df['x2'].to_numpy()
    X3 = df['x3'].to_numpy()
    Y_s =df['y'].to_numpy()
    tazaAprendizaje = 0.00001
    bias =  np.ones(len(X1))
    W = np.random.uniform(-1,1,4)
    W2 = np.random.uniform(-1,1,4)
    W3 = np.random.uniform(-1,1,4)
    W4 = np.random.uniform(-1,1,4)
    W5 = np.random.uniform(-1,1,4)
    ENTRADAS = np.array([X1,X2,X3,bias])
    WF, y_f = Entrenar(ENTRADAS.T,W,tazaAprendizaje,Y_s)
    wFP = EntrenarVarios(ENTRADAS.T, W, W2, W3, W4, W5, tazaAprendizaje, Y_s)
    print('Pesos finales con algebra:', WF)
    print('Ys finales con algebra:', y_f)
    print('===================================== ERRORES ===================================')
    print('Pesos finales de n5:', wFP)
    return y_f

if __name__ == '__main__':
    final_weights_ds1, predictions_ds1, modelado, Y_s = PerceptronTenser1('191214.csv')
    modelado2 = PerceptronTenser2('191214.csv')
    modelado3 = PerceptronTenser3('191214.csv')
    modelado4 = PerceptronTenser4('191214.csv')
    modelado5 = PerceptronTenser5('191214.csv')
    #os.system('cls')

    print(f'Pesos finales para dataset01: : {final_weights_ds1[0][0]} , {final_weights_ds1[0][1]},{final_weights_ds1[0][2]}, {final_weights_ds1[1]}')
    yAlgebra = LeerArchivoAlgebra()
    GraficarYs(predictions_ds1,modelado, Y_s, yAlgebra)
    GraficarErroresAlgebra()
    GraficarErroresTenser(modelado,modelado2,modelado3,modelado4,modelado5)
    
    