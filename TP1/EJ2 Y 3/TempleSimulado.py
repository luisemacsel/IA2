import numpy as np
import random as rd
from matplotlib import pyplot as plt
import math
from numpy import *
MatrizCosto=np.loadtxt('MatrizCosto.txt',skiprows=0) #carga la matriz de costos generada en a*
CostoBaseCarga=np.loadtxt('costoBase.txt',skiprows=0) #carga el vector generado en a*
cant=5   #cantidad de ordenes
SolucionInicial=np.array([37,47,11,48,24])   #solucion inicial de lista de ordenes


"""
    Esta funcion intercambia dos elementos de la lista del recorrido al alzar
"""
def intercambiarPosicion(Sol):
    aux_list = Sol.copy()
    idx = range(len(aux_list))
    i1, i2 = rd.sample(idx, 2)
    aux_list[i1], aux_list[i2] = aux_list[i2], aux_list[i1]
    return aux_list

"""
    Esta funcion calcula el costo del recorrido de la lista
"""
def CostoActual(Sact):
    i=0
    CostoTotal=0
    while(i<cant):
        if(i==0):
            CostoTotal=CostoTotal+CostoBaseCarga[Sact[i]-1]+MatrizCosto[Sact[i]-1][Sact[i+1]-1]
        elif(i==cant-1):
            CostoTotal=CostoTotal+CostoBaseCarga[Sact[i]-1]
        elif(i!=0 and i!=cant-1):
            CostoTotal=CostoTotal+MatrizCosto[Sact[i]-1][Sact[i+1]-1]
        i=i+1
    return (CostoTotal)

def TempleSimulado(TempInicial,TempFinal,SecEnfr,SolucionInicial):
    Temp=TempInicial
    iter=1
    Sact=CostoActual(SolucionInicial)   
    print('distancia inicial: '+str(Sact)+' con la lista: '+str(SolucionInicial)) 
    SolucionActual=SolucionInicial  
 
    max_it = TempInicial
    it_list = []
    prob_list = []
    temp_list=[]
    solucion_list=[]
    while True:
        it_list.append(iter)
        temp_list.append(Temp)
        solucion_list.append(Sact)
        if(Temp<TempFinal or iter>max_it):
            minDist=CostoActual(SolucionActual)
            print("distancia minima: "+str(Sact)+' con la lista: '+str(SolucionActual))
            plt.plot(it_list,temp_list)
            plt.show()
            plt.plot(it_list,solucion_list)
            plt.show()

            return (minDist)
        SolucionCandidato=intercambiarPosicion(SolucionActual)
        Scand=CostoActual(SolucionCandidato)
        #print(Scand)
        delta=Scand-Sact
        if(delta<=0):
            SolucionActual=SolucionCandidato
        else:               # Si la solucion no es mejor, acepta pero con una probabilidad de  e^(-cost/temp)
            prob = math.exp(-delta / Temp)
            prob_list.append(prob)
            if rd.uniform(0, 1) < prob:
                SolucionActual = SolucionCandidato
        Sact=CostoActual(SolucionActual)
        Temp=Temp*SecEnfr
        iter+=1
        
TempleSimulado(2500,0.01,0.8,SolucionInicial)

