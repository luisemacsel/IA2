import matplotlib.pyplot as plt
import numpy as np
def DectoRad(dec):
    rad=(dec*np.pi)/180
    return(rad)
def vecx(x0,xfin):
    x=[]
    while(x0<xfin):
        dt=0.0001
        xn=x0+dt
        x.append(float(x0))
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

graficar(vNG,NGVel,'NG','w [rad/s]')
graficar(vNP,NPVel,'NP','w [rad/s]')
graficar(vZ,ZVel,'Z','w [rad/s]')
graficar(vPP,NPVel,'PP','w [rad/s]')
graficar(vPG,PGVel,'PG','w [rad/s]')