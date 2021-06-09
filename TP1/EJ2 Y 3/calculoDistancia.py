'''
    Se calculan todos las distancias optimas y se las introduce a una matriz de la siguiente forma
        elemento [0][0]=distancia de ir del producto 1 al producto 1
        elemento [3][40]=distancia de ir del producto 4 al 41
    Tambien se calcula un vector el cual nos otorga la distancia que hay de la posicion 
    deseada a la estacion de carga
        
'''
from Aestrella import *
import pandas as pd

def CalculoCosto(map):
    productos=100
    costoPosBaseCarga=np.array(zeros(productos)) #vector de 100 de ceros
    MatrizCostos=np.zeros((productos, productos)) #matriz de 100x100 de ceros                          
    k=0
    while(k<productos):
        a=0
        b=k+1
        costo=a_star(map,a,b)
        costoPosBaseCarga[k]=costo
        k=k+1     
    np.savetxt('costoBase.txt',costoPosBaseCarga,fmt='%d')
    CB=pd.DataFrame(data=costoPosBaseCarga)
    CB.to_csv('costoBase.csv',sep=' ',header=False,index=False,float_format='%d')
    #calcula matriz de 99x100
    j=0
    while(j<(productos-1)):
        i=0   
          
        while(i<(productos)):       
            a=j #inicio   
            b=i #fin    
            costo = a_star(map,a,b)        
            if(a!=i):
                MatrizCostos[j][i]=costo
            if(a==i):
                MatrizCostos[j][i]=0.0
            i=i+1            
            print(i)
        j=j+1 
        print('j= '+str(j))
    
    np.savetxt('MatrizCosto.txt',MatrizCostos,fmt='%d')
    MC=pd.DataFrame(data=MatrizCostos)
    MC.to_csv('MatrizCosto.csv',sep=' ',header=False,index=False,float_format='%d')
    
