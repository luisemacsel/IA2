#from fitness import *
from Ffitness import *

MatrizCosto=np.loadtxt('MatrizCosto.txt',skiprows=0) #carga la matriz de costos generada en a*
CostoBaseCarga=np.loadtxt('costoBase.txt',skiprows=0) #carga el vector generado en a*
sinicial=np.loadtxt('listaPedidos.txt',skiprows=0)   #carga matriz de lista de pedidos
b=len(sinicial[0])  #longitud de cada fila
cant=np.zeros(100) #crea un vector para calcular la cantidad de productos !=0
cant=cantidadProductosLista(sinicial,b)        
MaxIterr=5
IndInicial=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
poblacion=np.zeros((MaxIterr,len(IndInicial)))
resultadoGeneracion=np.zeros(MaxIterr)
print("inicio de programa")
fitness=TempleSimulado(5000,0.01,0.8,sinicial,MatrizCosto,CostoBaseCarga,cant)
resultadoGeneracion[0]=promedio(fitness)
poblacion[0]=IndInicial
i=1
""" 
    Muta la configuracion del almacen
"""
while(i<MaxIterr):
    poblacion[i]=cambioPos(poblacion[i-1],len(poblacion[i-1]))
    i+=1
#print(poblacion)
"""
    Fitness
"""
j=1

while(j<MaxIterr-1):
    z=0
    ind=[]
    while(z<len(poblacion[0])):
        if(poblacion[j-1][z]!=poblacion[j][z]):
            ind.append(z)        
        z+=1
    #print(ind)
    aux=MatrizCosto[ind[0]]
    aux1=CostoBaseCarga[ind[0]]
    MatrizCosto[ind[0]]=MatrizCosto[ind[0]]
    MatrizCosto[ind[1]]=aux
    CostoBaseCarga[ind[0]]=CostoBaseCarga[ind[1]]
    CostoBaseCarga[ind[1]]=aux1    
    fitness=TempleSimulado(5000,0.01,0.8,sinicial,MatrizCosto,CostoBaseCarga,cant)
    resultadoGeneracion[j]=promedio(fitness)
    j+=1
print("Resultados por generacion")
print(resultadoGeneracion)
print("individuos de la generacion")
#print(poblacion)
#print("fin de programa")