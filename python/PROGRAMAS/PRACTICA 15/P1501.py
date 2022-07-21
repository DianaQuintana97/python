#DIANA QUINTANA GAMBOA
#Def. de funciones
def llenarm1():
    k=n1/2
    while(k!=0):
        m1.append(k)
        k=k/2
        
def llenarm2():
    k=n2*2
    for i in range(1,len(m1)):
        m2.append(k)
        k=k*2

def checar():
    n=len(m1)
    v=[0]*n
    s=0
    for i in range(0,len(m1)):
        w=m1[i]%2
        if(w!=0):
            s=m2[i]+s
            a=m2[i]
            v[i]=a
    return s,v

#Programa principal
print "==========MULTIPLICACION RUSA=========="
n1=int(raw_input("Ingrese multiplicando: "))
n2=int(raw_input("Ingrese multiplicador: "))
m1=[]
m2=[]
m1.append(n1)
m2.append(n2)
llenarm1()
print"   Multiplicando(%2) ",m1
llenarm2()
print"   Multiplicador(*2) ",m2
s,v=checar()
print"  Multiplicando impar",v
print "RESULTADO=",s

