'''
    Se implementa el algoritmo A*
'''
import numpy as np
from numpy import array
from numpy import *
import math


class Nodo:
    def __init__(self,padre=None,pos=(0,0)):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def calculate_h(self,objetivo): #Heuristica entre nodo actual y final
        self.h = math.sqrt((self.pos[0]-objetivo.pos[0])**2+(self.pos[1]-objetivo.pos[1])**2)
    def calculate_g(self,estado_actual): #camino recorrido
        self.g = estado_actual.g + 1
    def calculate_f(self): 
        self.f = self.g + self.h
def buscar_posicion(value,map, t=True):
    if value == 0:  # 0 es numero no valido por lo que no retorna nada
        return (14,0) #base de carga
    for index,fila in enumerate(map):
        if value in fila: #fila es la fila entera. index es el numero de la fila donde esta el valor buscado         
            columna = list(fila).index(value)    #columna en la que esta el valor buscado
            return (index,columna)
    else: return (0,0)

def a_star(map,a,b): 
    OPEN = []   #lista de nodos por investigar
    CLOSED = [] #lista de nosos ya investigados
    inicio = Nodo(None,buscar_posicion(a,map))
    objetivo = Nodo(None,buscar_posicion(b,map))
    inicio.calculate_f()
    inicio.calculate_h(objetivo)
    estado_actual = inicio
    OPEN.append(estado_actual)
    flag = 0

    def get_f(nodo):    #solo se usa para hacer el sorting de nodos.f
        return nodo.f
        
    while estado_actual.pos != objetivo.pos:
        OPEN.sort(key=get_f)    #metodo sort ordena la lista open de acuerdo al nodo.f
        estado_actual = OPEN[0]
        OPEN.pop(0)
        CLOSED.append(estado_actual)  #lo ponemos en la lista de ya explorados

        if estado_actual.pos == objetivo.pos:  #si llegamos al objetivo            
            return(estado_actual.f)           

        vecinos = []
        for a in [(1,0),(-1,0),(0,1),(0,-1)]: #movimientos validos
            pos = (a[0] + estado_actual.pos[0], a[1] + estado_actual.pos[1])
            if (0 <= estado_actual.pos[0]+a[0] < len(map)) and (0 <= estado_actual.pos[1]+a[1] < len(map[0])): #tomamos posiciones validas
                if map[pos]==0:
                    vecinos.append(Nodo(estado_actual,pos))   #creamos nodos nuevos para cada posicion
                elif (map[pos]==map[objetivo.pos] and flag==1):  #si la posicion es el objetivo se agrega
                    vecinos.append(Nodo(estado_actual,pos))
        flag = 1 # permite que no eliga en el primer bucle  la solucion de alado

        for vecino in vecinos:
            if vecino in CLOSED:    #si ya esta en lista de explorados saltamos esa iteracion
                continue 
            vecino.calculate_g(estado_actual)
            vecino.calculate_h(objetivo)
            vecino.calculate_f()
            if vecino.g < estado_actual.g or vecino not in OPEN: 
                vecino.padre = estado_actual
                if vecino not in OPEN and vecino not in CLOSED:
                    OPEN.append(vecino)

