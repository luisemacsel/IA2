import numpy as np
from numpy import *
import numpy

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

