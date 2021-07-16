import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape

# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)

#Datos continuos
def generar_datos_clasificacion(cantidad_ejemplos):
    
    x = np.zeros((cantidad_ejemplos,1))
    t = np.zeros((cantidad_ejemplos,1))   
    
    for i in range(cantidad_ejemplos):
        t[i] = i
        x[i] = t[i] + np.random.uniform(-1,1)
    return x, t


def inicializar_pesos(n_entrada, n_capa_2):
    randomgen = np.random.default_rng()

    w1 = 10*randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 10*randomgen.standard_normal((1, n_capa_2))

    w2 = 10*randomgen.standard_normal((n_capa_2, 1))
    b2 = 10*randomgen.standard_normal((1,1))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

def sigmoid(x): 
    z = np.exp(-x)
    sig = 1 / (1 + z)
    return sig

def ejecutar_adelante(x, pesos):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]

    # Funcion de activacion Sigmoide para la capa oculta (h -> "hidden")
    h = sigmoid(z)

    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t, pesos, learning_rate, epochs):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0) 
    
    for i in range(epochs):
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]

        # LOSS
        Li=np.power(t-y,2)
        loss=1/m*np.sum(Li)

        # Mostramos solo cada 1000 epochs
        if i %1000 == 0:
            print("Loss epoch", i, ":", loss)

        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dw2 = h.T.dot(2*(y-t)/m)         # Ajuste para w2
        dL_db2 = np.sum((2*(y-t)/m), axis=0, keepdims=True)   # Ajuste para b2

        dL_dy=-2/m*(t-y)
        dL_dh = dL_dy.dot(w2.T)

        dL_dz = dL_dh.dot(sigmoid(z).T).dot(1-sigmoid(z))      # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta

        dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1

        # Aplicamos el ajuste a los pesos
        w1 += -learning_rate * dL_dw1
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        # Actualizamos la estructura de pesos
        # Extraemos los pesos a variables locales
        pesos["w1"] = w1
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2


def iniciar(datos, graficar_datos):
    # Generamos datos
    x, t = generar_datos_clasificacion(datos)
    # Graficamos los datos si es necesario
    if graficar_datos:
        tamano = len(x)
        abcisa = list()
        for i in range(tamano):
            abcisa.append(i)
        plt.plot(abcisa,x,t)
        plt.xlabel('Dato N°')
        plt.ylabel('x vrs t')
        plt.show()

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 1
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA)

    # Entrena
    LEARNING_RATE=1
    EPOCHS=10000
    train(x, t, pesos, LEARNING_RATE, EPOCHS)


iniciar(datos=300, graficar_datos=True)