import numpy as np
from numpy import *
import random as rd
from matplotlib import pyplot as plt
import math

def cantidadProductosLista(a,cantidadElementosFila):
    j=0
    cant=np.zeros(100)
    while(j<100):
        i=0
        aux=0
        while(i<cantidadElementosFila):
            if(a[j][i]!=0):
                aux+=1
            i+=1
        cant[j]=aux
        j+=1
    return (cant)
def cambioPos(matriz,cant):
    i=0
    ind=np.random.randint(1,cant,size=2)    
    while(i<2):            
        if(i==1):
            while(ind[i]==ind[i-1]):
                ind[i]=np.random.randint(1,cant,size=1)             
        i+=1
    aux=matriz[ind[0]]    
    matriz[ind[0]]=matriz[ind[1]]
    matriz[ind[1]]=aux    
    return matriz
def modificaActual(a,cant):
    k=0
    c=np.zeros((100,28))
    while(k<100):
        c[k]=(cambioPos(a[k],cant[k]))
        k+=1
    return c

def CostoActual(Sact,cant,MatrizCosto,CostoBaseCarga):
    CostoTotal=np.zeros(100)
    j=0
    while(j<100):
        i=0
        while(i<cant[i]):
            indx=int((Sact[j][i])-1)
            indy=int((Sact[j][i+1])-1)
            if(i==0):
                CostoTotal[j]=CostoTotal[j]+CostoBaseCarga[indx]+MatrizCosto[indx][indy]
            elif(i==cant[i]-1):
                CostoTotal[j]=CostoTotal[j]+CostoBaseCarga[indx]
            elif(i!=0 and i!=cant[i]-1):
                CostoTotal[j]=CostoTotal[j]+MatrizCosto[indx][indy]
            i=i+1
        j+=1
    return (CostoTotal)

def promedio(fitness):
    i=0
    aux=0
    while(i<100):
        aux+=fitness[i]
        i+=1
    fitness=aux/100
    return fitness

def TempleSimulado(TempInicial,TempFinal,SecEnfr,sinicial,MatrizCosto,CostoBaseCarga,cant):
    Temp=TempInicial
    iter=1
    cact=CostoActual(sinicial,cant,MatrizCosto,CostoBaseCarga) #costo de la solucion actual    
    #print('distancia inicial: '+str(promedio(cact))) 
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
            #plt.plot(it_list,temp_list)
            #plt.show()
            #plt.plot(it_list,solucion_list)
            #plt.show()

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