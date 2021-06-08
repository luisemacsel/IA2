import numpy as np
import random as rd
from matplotlib import pyplot as plt
import math
from numpy import *
from Ffitness import *

MatrizCosto=np.loadtxt('MatrizCosto.txt',skiprows=0) #carga la matriz de costos generada en a*
CostoBaseCarga=np.loadtxt('costoBase.txt',skiprows=0) #carga el vector generado en a*
sinicial=np.loadtxt('listaPedidos.txt',skiprows=0)   #carga matriz de lista de pedidos
b=len(sinicial[0])  #longitud de cada fila
cant=np.zeros(100) #crea un vector para calcular la cantidad de productos !=0
cant=cantidadProductosLista(sinicial,b)

def TempleSimulado(TempInicial,TempFinal,SecEnfr):
    Temp=TempInicial
    iter=1
    cact=CostoActual(sinicial,cant,MatrizCosto,CostoBaseCarga) #costo de la solucion actual    
    print('distancia inicial: '+str(promedio(cact))) 
    sact=sinicial
    max_it = TempInicial
    it_list = []
    prob_list = []
    temp_list=[]
    solucion_list=[]
    while True:
        it_list.append(iter)
        temp_list.append(Temp)
        solucion_list.append(cact[10])
        if(Temp<TempFinal or iter>max_it):
            minDist=CostoActual(sact,cant,MatrizCosto,CostoBaseCarga) #costo de la solucion actual    
            #print("distancia minima: "+str(minDist)+' con la lista: '+str(sact))
            plt.plot(it_list,temp_list)
            plt.show()
            plt.plot(it_list,solucion_list)
            plt.show()

            return (minDist)
        smod=modificaActual(sact,cant) #solucion modificada
        cmod=CostoActual(smod,cant,MatrizCosto,CostoBaseCarga) #costo de la solucion modificada
        #print(Scand)
        delta=cmod[0]-cact[0]
        if(delta<=0):
            sact=smod
        else:               # Si la solucion no es mejor, acepta pero con una probabilidad de  e^(-cost/temp)
            prob = math.exp(-delta / Temp)
            prob_list.append(prob)
            if rd.uniform(0, 1) < prob:
                sact = smod
        cact=CostoActual(sact,cant,MatrizCosto,CostoBaseCarga) #costo de la solucion actual
        Temp=Temp*SecEnfr
        iter+=1
        
fitness=TempleSimulado(5000,0.01,0.8)
print(fitness)
fitness=promedio(fitness)
print(fitness)

