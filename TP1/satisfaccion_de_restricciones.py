import random
from collections import Counter
import matplotlib as plt

class Maquina(): 
    def __init__(self, estado):
        self.estado = estado
        self.tiempo = 0

def backtracking(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas):

    if len(asignamiento) == len(variables): #Si el asignamiento esta completo retornarlo
        return asignamiento

    var = seleccionar_variable_sin_asignar(variables, asignamiento, restricciones_precedencia)

    for tiempo in range(0, len(dominio)):
        if consistencia(variables, var, tiempo, asignamiento, restricciones_precedencia, restricciones_recursos, tiempo_limite) == True:
            asignamiento.append(var)
            resultado = backtracking(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas)
            if resultado != False:
                return resultado
            asignamiento.pop(asignamiento.index(var))
    else:
        resultado = backtracking(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas)
        if resultado != False:
            return resultado
    return False

    # elijo la variable mas restringida
#%%
def seleccionar_variable_sin_asignar(variables, asignamiento, restricciones_precedencia):
    aux = [item[1][0] for item in restricciones_precedencia.items()]  #Toma las primeras T de cada restriccion
    count = Counter(aux).items()    #Cuenta cuantos hay de cada T y lo pone en un diccionario
    count = sorted(count, key=lambda x: x[1], reverse=True) #Ordena de mayor a menor
    count = [i[0] for i in count if i[0] not in asignamiento]
    count += [item[0] for item in variables.items() if item[0] not in count and item[0] not in asignamiento]
    return count[0]
#%%
def consistencia(variables, var, tiempo, asignamiento, restricciones_precedencia, restricciones_recursos, tiempo_limite):
    for elemento in asignamiento:   #Calculamos el tiempo tomado de las asignaciones hasta el momento
        tiempo += variables[elemento]
    tiempo += variables[var]
    if tiempo > tiempo_limite:  #Si el tiempo de los elementos en el asignamiento supera el deadline
        return False
    for i in range(0, len(restricciones_precedencia)):
        if var == restricciones_precedencia[i][1]:
            if restricciones_precedencia[i][0] not in asignamiento:
                return False
    
    return True


if __name__ == '__main__':
    variables = {"T1": 5, "T2": 15, "T3": 10, "T4": 30, "T5": 25}
    tiempo_limite = 100
    asignamiento = []
    dominio = [i for i in range(0, tiempo_limite)]

    # T2 debe realizarse antes que T3
    # T4 debe realizarse antes que T1
    # T4 debe realizarse antes que T3

    # Restricciones:
    # T1 ocupa la máquina 1
    # T2 ocupa las máquinas 2 y 3
    # T3 ocupa la máquina 4
    # T4 ocupa las máquinas 1 y 3
    restricciones_precedencia = {0: ("T2", "T3"), 1: ("T4", "T1"), 2: ("T4", "T3")}
    restricciones_precedencia[0][1]
    M1 = Maquina(True)
    M2 = Maquina(True)
    M3 = Maquina(True)
    M4 = Maquina(True)

    maquinas = [M1, M2, M3, M4]

    restricciones_recursos = {"T1": (M1), "T2": (M1, M2, M3), "T3": (M1, M4), "T4": (M1, M3)}
    asignamiento = []
    tiempo_limite = 100
    value = backtracking(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas)
    print(f'Orden optimo: {value}')
# %%
