import numpy as np         #Para trabajar con vectore de forma mas rapida y con mayor velocidad
import math                #Para realizar operaciones matematicas
import random              #permite trabajar con funciones q generan valores aleatorios

class Nodo:
    def __init__(self, padre=None, pos=[0,0,0,0,0,0]):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def calculate_h(self,objetivo): #Heuristica entre nodo actual y final
        self.h = math.sqrt((self.pos[0]-objetivo.pos[0])**2+(self.pos[1]-objetivo.pos[1])**2+(self.pos[2]-objetivo.pos[2])**2+(self.pos[3]-objetivo.pos[3])**2+(self.pos[4]-objetivo.pos[4])**2+(self.pos[5]-objetivo.pos[5])**2)
    def calculate_g(self,estado_actual,vecino): #camino recorrido
        self.g = estado_actual.g + math.sqrt((self.pos[0]-vecino.pos[0])**2+(self.pos[1]-vecino.pos[1])**2+(self.pos[2]-vecino.pos[2])**2+(self.pos[3]-vecino.pos[3])**2+(self.pos[4]-vecino.pos[4])**2+(self.pos[5]-vecino.pos[5])**2)
    def calculate_f(self): #Calculo de f
        self.f = self.g + self.h

def buscar_posicion(value, map):  #esta funcion nos devuelve la posicion ingresando la matriz y el numero cuya posicion se quiere encontrar
    if value == 0:  # 0 es numero no valido por lo que no retorna nada
        return (0, 0, 0, 0, 0, 0)
    else:
      result = np.argwhere(map == value)   #argwhere busca en la matriz "map" que posicion ocupa el valor "value" y devuelve la posicion
      return tuple(result[0])

def a_star(map,a,b): 
    OPEN = []   #lista de nodos por investigar (lista abierta)
    CLOSED = [] #lista de nosos ya investigados (lista cerrada)
    inicio = Nodo(None,buscar_posicion(a,map))  #armamos el objeto inicio
    objetivo = Nodo(None,buscar_posicion(b,map))  #armamos el objeto objetivo
    inicio.calculate_h(objetivo)        #calcula la heuristica del inicio
    inicio.calculate_f()
    estado_actual = inicio       #Decimos que el estado actual es el nodo inicio
    OPEN.append(estado_actual)   #agragamos el nodo inicio a la lista abierta
    flag = 0 

    def get_f(nodo):    #solo se usa para hacer el sorting de nodos.f (en simples paralabras: para obtener el f de un nodo)
      return nodo.f

    while estado_actual.pos != objetivo.pos: #mientras no se alcance la posicion objetivo:
        OPEN.sort(key=get_f)    #metodo sort ordena las posiciones de la lista open de acuerdo al nodo.f (ordena la lista de acuerdo a los valores f)
        estado_actual = OPEN[0] #toma como estado actual al primero de la lista "OPEN"
        OPEN.pop(0) #se elimina al primer nodo de la lista "OPEN"
        CLOSED.append(estado_actual)  #y lo ponemos en la lista de ya explorados

        if estado_actual.pos == objetivo.pos:  #si llegamos al objetivo
            path = []
            while estado_actual is not None:  #obtenemos el camino  optimo en una lista de padres de cada nodo
                path.append(estado_actual.pos) #añadimos a la lista la poscion actual
                estado_actual = estado_actual.padre #actualizamos la posicion actual por el padre
            return(path[-2:0:-1]) #retorna el camino "invertido" porque parte del final al inicio

        vecinos = []
        for i in (1,0,-1): #movimientos validos en X
            for j in (1,0,-1): #movimientos validos en Y
                for k in (1,0,-1): #movimientos validos en Z
                    for ii in (1,0,-1):
                        for jj in (1,0,-1):
                            for kk in (1,0,-1):
                                a=(i,j,k,ii,jj,kk)
                                if a==(0,0,0):
                                    break
                                else:
                                    pos = (a[0] + estado_actual.pos[0], a[1] + estado_actual.pos[1], a[2] + estado_actual.pos[2],a[3] + estado_actual.pos[3],a[4] + estado_actual.pos[4],a[5] + estado_actual.pos[5]) #Hace el movimiento
                                    if (0 <= estado_actual.pos[0]+a[0] < map.shape[0]) and (0 <= estado_actual.pos[1]+a[1] < map.shape[1]) and (0 <= estado_actual.pos[2]+a[2] < map.shape[2]) and (0 <= estado_actual.pos[3]+a[3] < map.shape[3]) and (0 <= estado_actual.pos[4]+a[4] < map.shape[4]) and (0 <= estado_actual.pos[5]+a[5] < map.shape[5]): #tomamos posiciones validas
                                        if map[pos]==0:
                                            vecinos.append(Nodo(estado_actual,pos))   #creamos nodos nuevos para cada posicion y los añadimos a la lista vecinos
                                        elif (map[pos]==map[objetivo.pos] and flag==1):  #si la posicion es el objetivo se agrega
                                            vecinos.append(Nodo(estado_actual,pos))
        flag = 1 # permite que no elija en el primer bucle  la solucion de al lado
        for vecino in vecinos:
            if vecino in CLOSED:    #si ya esta en lista de explorados saltamos esa iteracion
                continue 
            vecino.calculate_g(estado_actual,vecino) #Hacemos los calculos de g,h y f de cada uno de los vecinos
            vecino.calculate_h(objetivo)
            vecino.calculate_f()
            if vecino.g < estado_actual.g or vecino not in OPEN: 
                vecino.padre = estado_actual                #Asiganamos el padre a cada vecino
                if vecino not in OPEN and vecino not in CLOSED:
                    OPEN.append(vecino)                     #añadimos a cada vecino a la lista abierta

def main():
    print("Ejercicio 1")
    NposD=14        #Elegimos el numero de posiciones q se pueden tomar para cada direccion
    map = np.zeros([NposD,NposD,NposD,NposD,NposD,NposD]) #Generamos la matriz de 6D
    NposT=NposD**6       #Numero de posiciones
    print ("Numero de posiciones", NposT)
    inicio=1                 #inicio representado con '1'
    fin=3                    #fin representado con '3'
    map[0,0,0,0,0,0]=inicio           #pos inicial
    map[13,13,13,13,13,13]=fin        #pos final
    
    obstaculo=4   #generamos los obstaculos aleatorios
    PorcObst=80   #40% del mapa son obstaculos
    Nobstaculo=int(NposT*PorcObst/100)        #numero de obstaculos en la matriz
    print ("Numero de obstaculos", Nobstaculo)
    for i in range (Nobstaculo):
        x=random.randint(0, map.shape[0]-1) #generamos las 6 coordenadas aleatorias
        y=random.randint(0, map.shape[1]-1)
        z=random.randint(0, map.shape[2]-1)
        xx=random.randint(0, map.shape[3]-1)
        yy=random.randint(0, map.shape[4]-1)
        zz=random.randint(0, map.shape[5]-1)
        if map[x,y,z,xx,yy,zz]==0:
            map[x,y,z,xx,yy,zz]=obstaculo  #creamos un obstaculo en la posicion aleatoria

    solution = a_star(map,inicio,fin)  #llamamos a la funcion A* indicando el mapa, el inicio y el fin
    print("Camino optimo:")
    print(solution)
    for pos in solution:
        map[pos] = 2 #Camino optimo completar con dos

if __name__ == "__main__":
    main()