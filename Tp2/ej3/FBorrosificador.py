import matplotlib.pyplot as plt
import numpy as np
"""
    La funcion se encarga de buscar el valor de fuerza que le corresponde para ese valor f en el rango elegido
    Buscavalor(max,rango,funcion):
    max:valor obtenido de la funcion figual
    rango: rango de la funcion de f de la FAM
    funcion: es la funcion dada para el rango de f de la FAM
"""
def Buscavalor(max,rango,funcion):
    fmax=[]
    i=0
    while(i<80001):
        x=round(funcion[i],3)      #redondea la funcion a 3 decimales como el valor maximo obtendio
        if(max==x):
            fmax.append(rango[i])
        i+=1
    return(fmax)

"""
    DectoRad(dec)
    dec: numero sexagecimal que desea convertir
    Convierte un valor de sexagecimal a radian
"""
def DectoRad(dec):
    rad=(dec*np.pi)/180
    return(rad)
"""
    vecx(x0,xfin)
    x0: valor incial del intervalo
    xfin: valor final del intervalo
    Genera los intervalos nitidos de la funcion borrosa
"""
def vecx(x0,xfin):
    x=[]
    while(x0<xfin):
        dt=0.0001
        xn=x0+dt
        x.append(round(x0,4))
        x0=xn
    return(x)

def hombroder(xfin,x0,xintermedio,pendiente,t):
    PGTheta=[]
    t=t
    while(x0<xfin):
        dt=0.0001
        if(x0>=xintermedio):
            PGTheta.append(1)
    
        else:
            nv=(1/pendiente)*t
            t+=dt
            PGTheta.append(nv)
        xn=x0+dt
        x0=xn
    return(PGTheta)

def hombroizq(xfin,x0,xintermedio,pendiente,t):
    NGTheta=[]
    t=t
    while(x0<xfin):
        dt=0.0001
        if(x0<=xintermedio):
            NGTheta.append(1)
    
        else:
            nv=1-(1/pendiente)*t
            t+=dt
            NGTheta.append(nv)
        xn=x0+dt
        x0=xn
    return(NGTheta)
 
def triangulo(x0,xintermedio,xfinal,dt,pendiente):
    NPTheta=[]
    t=0
    t1=0
    while(x0<xfinal):
        if(x0<xintermedio):
            nv=(pendiente)*t
            NPTheta.append(nv)
            t+=dt
        elif(x0<xfinal):
            nv=1-(pendiente)*t1
            NPTheta.append(nv)
            t1+=dt
        x0+=dt
    return(NPTheta)

def graficar(x,y,titulo,variable):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel=variable, ylabel='fborrosa', title=titulo)
    ax.grid()  
    plt.show()
"""
    valormedio(x,fbor):
    Entrega el valor medio de la funcion borrosa elegida
    x: intervalo de la funcion borrosa
    fbor: funcion borrosa
"""
def valormedio(x,fbor):
    i=0
    salida=True
    while(salida):
        if(fbor[i]==1):
            vmed=x[i]
            salida=False
        i+=1
    return(vmed)
"""
    BorrosificadorSingleton(variableNitida,fbor,x):
    variable nitida ejemplo : fuerza se coloca un valor con 4 cifras significativa
    fbor: funcion que desea borrosificar ej: NG,NP,Z,PP O PG
    x : intervalor de la funcion borrosa ej: vNG,vNP,vZ,vPP,vPG
"""
def BorrosificadorSingleton(variableNitida,fbor,x):
    i=0
    salida=True
    while(salida):
        if(variableNitida==x[i]):
            A=fbor[i]
            salida=False
        else:
            A=0
        i+=1
    return(round(A,3))

"""
    Calculo de la funcion del borrosificador de theta
"""
NGTheta=hombroizq(DectoRad(-30),DectoRad(-90),DectoRad(-60),DectoRad(30),0)
xNG=vecx(DectoRad(-90),DectoRad(-30))
xNP=vecx(DectoRad(-60),DectoRad(0))
NPTheta=triangulo(DectoRad(-60),DectoRad(-30),DectoRad(0),0.0001,DectoRad(110))
xZ=vecx(DectoRad(-30),DectoRad(30))
ZTheta=triangulo(DectoRad(-30),DectoRad(0),DectoRad(30),0.0001,DectoRad(110))
xPP=vecx(DectoRad(0),DectoRad(60))
PPTheta=triangulo(DectoRad(0),DectoRad(30),DectoRad(60),0.0001,DectoRad(110))
xPG=vecx(DectoRad(30),DectoRad(90))
PGTheta=hombroder(DectoRad(90),DectoRad(30),DectoRad(60),DectoRad(30),0)

graficar(xNG,NGTheta,'NG','theta [rad]')
graficar(xNP,NPTheta,'NP','theta [rad]')
graficar(xZ,ZTheta,'Z','theta [rad]')
graficar(xPP,NPTheta,'PP','theta [rad]')
graficar(xPG,PGTheta,'PG','theta [rad]')
"""
    Calculo de la funcion del borrosificador de velocidad
"""
NGVel=hombroizq(-2,-6,-4,2,0)
vNG=vecx(-6,-2)
vNP=vecx(-4,0)
NPVel=triangulo(-4,-2,0,0.0001,0.5)
vZ=vecx(-2,2)
ZVel=triangulo(-2,0,2,0.0001,0.5)
vPP=vecx(0,4)
PPVel=triangulo(0,2,4,0.0001,0.5)
vPG=vecx(2,6)
PGVel=hombroder(6,2,4,2,0)

#graficar(vNG,NGVel,'NG','w [rad/s]')
#graficar(vNP,NPVel,'NP','w [rad/s]')
#graficar(vZ,ZVel,'Z','w [rad/s]')
#graficar(vPP,NPVel,'PP','w [rad/s]')
#graficar(vPG,PGVel,'PG','w [rad/s]')

"""
    Calculo de la funcion del borrosificador de la fuerza
"""
NGF=hombroizq(-4,-12,-8,4,0)
fNG=vecx(-12,-4)
fNP=vecx(-8,0)
NPF=triangulo(-8,-4,0,0.0001,0.25)
fZ=vecx(-4,4)
ZF=triangulo(-4,0,4,0.0001,0.25)
fPP=vecx(0,8)
PPF=triangulo(0,4,8,0.0001,0.25)
fPG=vecx(4,12)
PGF=hombroder(12,4,8,4,0)
#print(len(PPF))
#graficar(fNG,NGF,'NG','f [N]')
#graficar(fNP,NPF,'NP','f [N]')
#graficar(fZ,ZF,'Z','f [N]')
#graficar(fPP,NPF,'PP','f [N]')
#graficar(fPG,PGF,'PG','f [N]')

