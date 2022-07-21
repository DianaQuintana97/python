#DIANA QUINTANA GAMBOA
#Def. de funciones 
from fractions import *
def encontrarMV():
    MV[0]=" MAX  VI "
    peso=0
    valor=0
    r=0
    for i in range (0,len(V)):
        antp=peso
        ant=valor
        max,l=buscarMV()
        valor=max+valor
        peso=W[l]+peso
        if(peso<w):
            l=l+1
            MV[l]="1"
        else:
            r=w-antp
            l=l+1
            x=(r*1.0)/W[l-1]
            valor=ant+max*x
            MV[l]=x
            break
    a=len(V)+1
    MV[a]="Valor:",valor
    print MV

def buscarMV():
    max=b[0]
    i=1
    l=0
    while(i<len(b)):
        if(b[i]>max):
            max=b[i]
            l=i
        i=i+1
    b[l]=0
    return max,l

def encontrarMW():
    MW[0]=" MAX  WI "
    peso=0
    valor=0
    for i in range (1,len(W)):
        ant=valor
        max,l=buscarMW()
        peso=max+peso
        valor=V[l]+valor
        if (peso==100):
            l=l+1
            MW[l]="1"
            break
        if(peso<w):
            l=l+1
            MW[l]="1"
        else:
            r=w-max
            x=(r*1.0)/max
            valor=ant+V[l]*x
            l=l+1
            MW[l]=x
    a=len(V)+1
    MW[a]="Valor:",valor
    print MW
        
def buscarMW():
    max=c[0]
    i=1
    l=0
    while (i<len(c)):
        if(c[i]<max):
            max=c[i]
            l=i
        i=i+1
    c[l]=" "
    return max,l

def encontrarMVW():
    MVW[0]="MAX Vi/Wi"
    peso=0
    valor=0
    for i in range(0,len(V)):
        antp=peso
        ant=valor
        l=buscarMVW()
        valor=V[l]+valor
        peso=W[l]+peso
        if(peso<w):
            l=l+1
            MVW[l]="1"
        else:
            r=w-antp
            l=l+1
            x=(r*1.0)/W[l-1]
            valor=ant + V[l-1]*x
            MVW[l]=x
            break
    a=len(VW)+1
    MVW[a]="Valor:",valor
    print MVW
   
def buscarMVW():
    max=d[0]
    i=1
    l=0
    while (i<len(b)):
        if(d[i]>max):
            max=d[i]
            l=i
        i=i+1
    d[l]=0
    return l
    
def llenar():
    p=0
    while (p<len(V)):
        b[p]=V[p]
        p=p+1
    return b

def llenarc():
    p=0
    while (p<len(W)):
        c[p]=W[p]
        p=p+1
    return c

def llenard():
    p=0
    while (p<len(VW)):
        d[p]=VW[p]
        p=p+1
    return d
        
#Programa principal
print "*****Problema de la mochila*****"
n=int(raw_input("Ingrese numero de objetos: "))
w=int (raw_input("Ingrese capasidad total de la mochola : "))
W=[]
V=[]
VW=[]
b=[0]*n
c=[0]*n
d=[0]*n
e=[0]*n
MV=["-"]*(n+2)
MW=["-"]*(n+2)
MVW=["-"]*(n+2)
for i in range(0,n):
    print "Objeto:",i+1
    x=int(raw_input("Ingrese peso: "))
    W.append(x)
    xx=int(raw_input("Ingrese costo: "))
    V.append(xx)
    VW.append(xx*1.0/x)
for i in range(1,n):
    e[i]=i
print " W ", W
print " V ",V
print "V/W",VW
print "Seleccionar",  "          Xi              "," Valor "
b=llenar()
c=llenarc()
d=llenard()
encontrarMV()
encontrarMW()
encontrarMVW()

