from FAM import *

Thetanitida=0.6
Velnitida=2.8

A1=BorrosificadorSingleton(Thetanitida,PGTheta,xPG)
A2=BorrosificadorSingleton(Velnitida,PGVel,vPG)
vmed1=valormedio(fPG,PGF)
print('El valor de A1 es :'+str(A1)+' y el valor de A2 es :'+str(A2)+' Y el valor medio de la funcion f es : '+str(vmed1))
B1=BorrosificadorSingleton(Thetanitida,PGTheta,xPG)
B2=BorrosificadorSingleton(Velnitida,PPVel,vPP)
vmed2=valormedio(fPP,PPF)
print('El valor de B1 es :'+str(B1)+' y el valor de B2 es :'+str(B2)+' Y el valor medio de la funcion f es : '+str(vmed2))
if(FAM[3][4]==FAM[4][4]):
    maximo=Figual(A1,A2,B1,B2)
    resultado=max(Buscavalor(maximo,fPG,PGF))
    print('La fuerza resultante que se debe aplicar es :'+str(resultado))
if(FAM[3][4]!=FAM[4][4]):
    print('La fuerza resultante que se debe aplicar es :'+str(Fdistinto(A1,A2,B1,B2,vmed1,vmed2)))
