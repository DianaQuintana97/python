#Diana Quintana Gamboa
#Practica 5
#definiciones de funciones
def com(vm):
    for j in range(0,len(sm)):
        vm=sm[j]
        print "vm",vm
        if (memori[vm]==0):
            b=0
        else:
            b=1
        if (b!=1):
            print "b",b
            return vm
            break
def insert(vm,y):
    pc=vm
    i=0
    while (i<len(y)):
        memori[pc]=y[i]
        pc=pc+1
        i=i+1
    return memori
def chec(v,vm,vwk,lonwk):
    u=len(lonwk)
    p=len(v)
    for l in range(0,u):
        vm=com(sm)
        if(l<len(v)):
            for t in range(0,p):
                print "t",t
                for i in range(0,p):
                    print"i",i
                    if(lonwk[t] <= v[i]):
                        print "pos",lonwk[t]
                        y=vwk[t]
                        t=insert(vm,y)
                        return t
                    break
        else:
            break

#programa principal
p=int(raw_input("cuantas particiones desea:"))
v=[]
sm=[]
listE=[]
lonwk=[]
vwk=[]
s=0
for i in range(0,p):
    r=int(raw_input("Ingrese espacio de particion: "))
    v.append(r)
    sm.append(s)
    s=s+r
print "Para dejar de ingresar trabajos inserte 5"
memori=[0]*s
n=0
while True:
    wk=str(raw_input("Ingrese trabajo:"))
    if(wk!="5"):
       n=n+1
       vwk.append(wk)
       lonwk.append(len(wk))
    else:
        break
print "vwk",vwk
print "lon",lonwk
print "memoria:",chec(v,sm,vwk,lonwk)
print "Lista en espera:",listE

    
