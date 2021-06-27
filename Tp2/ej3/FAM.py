import numpy as np
"""
    Figual , funcion para cundo los consecuntes son iguales ej: F es PP Y F es PP
    Ai,Bi:valor borro de la variable nitida  ej: theta=20° theta es PP A1=0.7   
"""
def Figual(A1,A2,B1,B2):
    f=max(min(A1,A2),min(B1,B2))  #conjunto borroso de salida
    pass
"""
    Fdistinto , funcion para cundo los consecuntes son distintos ej: F es Z Y F es PP
    vmed :valor medio de la funcion borrosa ej:PP
    Ai,Bi:valor borro de la variable nitida  ej: theta=20° theta es PP A1=0.7   
"""
def Fdistinto(A1,A2,B1,B2,vmed1,vmed2):     
    vpertenecia1=min(A1,A2)   #disyuncion
    vpertenecia2=min(B1,B2)   #disyuncion
    f=((vmed1*vpertenecia1+vmed2*vpertenecia2)/(vpertenecia1+vpertenecia2))    #desborrosificador por media de centros
    
    pass
"""
FAM: tabla de doble entrada (desplazamiento angular y velocidad angular , salida fuerza)
    THETA NG NP Z PP PG
VEL 
NG        X  X  X  X  X
NP        X  X  X  X  X
Z         X  X  X  X  X
PP        X  X  X  X  X
PG        X  X  X  X  X
X puede ser NG,NP,Z,PP o PG ,
son los valores que toma la fuerza con sierta velocidad y desplazamiento angular 
"""
FAM=[["PP","PP","PP","PP","PP"],
     ["PP","PP","PP","PP","PP"],
     ["PP","PP","PP","PP","PP"],
     ["PP","PP","PP","PP","PP"],
     ["PP","PP","PP","PP","PP"]]
print(FAM)
