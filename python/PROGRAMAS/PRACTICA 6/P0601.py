#DIANA QUINTANA GAMBOA
#programa 6
#def. de funciones
def memoria(v,s):
    i=0
    r=0
    while(i<len(v)):
        k=0
        w=v[i]
        while(k<len(w)):
            memori[r]=w[k]
            r=r+1
            k=k+1
        i=i+1
def limpi(memori,ss,w):
    i=ss-1
    j=len(w)
    r=0
    while(r<j):
        memori[i]=0
        i=i-1
        r=r+1
    return memori
def limpiar(j,memori,trT,v):
    q=0
    ss=0
    while (q<len(trT)):
        w=v[q]
        ss=ss+len(w)
        if(trT[q]==j):
            memori=limpi(memori,ss,w)
        q=q+1
    return memori
def checar(memori,wk):
    i=0
    s=0
    while(i<len(memori)):
        if(memori[i]==0):
            s=s+1
        else:
            s=0
        if(s==len(wk)):
            return i
        i=i+1
    if (s==0):
        i=len(memori)
        print i
        return i
def llenar(wk,p):
    x=p
    if(p==0):
        x=len(wk)
        r=0
    else:
        r=p-len(wk)
    i=0
    while(r<x):
        memori[r]=wk[i]
        i=i+1
        r=r+1
    return memori
def recorre(LisE,wk):
    j=0
    k=1
    while(j<len(LisE)):
        if(LisE[k]!=" "):
            x=LisE[K]
            LisE[j]=x
        else:
            LisE[j]=wk
            break
        j=j+1
        k=j+k
def recorre2(wk):
    if(LisE[0]==" "):
        LisE[0]=wk
    else:
        for i in renge(0,len(LisE)):
            if(LisE[0]!=" "):
                LisE[i]=wk
                break
#programa principal
print "Para dejar de ingresar trabajos inserte -1"
s=0 #suma memoria
i=0
j=2
v=[] #guardar trabajos
LisE=[" "]*20
memori=[]
trT=[2,4,2,8,10]
while (i<5):
    wk=str(raw_input("Ingrese trabajo:"))
    if(wk!="0"):
        s=s+len(wk)
        v.append(wk)
        i=i+1
    else:
        break
memori=[0]*s
memoria(v,s) 
while True:
    wk=str(raw_input("Ingrese trabajo:"))
    if(wk!="-1"):
        memori=limpiar(j,memori,trT,v)
        j=j+2
        print "memoria:",memori
        if(LisE[0]!=" "):
            print "EN ESPERA"
            w=LisE[0]
            recorre(LisE,wk)
            p=checar(memori,w)
            print "p",p
            if(p!=len(memori)):
                memori=llenar(w,p)
                print "memoria:",memori
        else:
            p=checar(memori,wk)
            print "p",p
            if(p!=len(memori)):
                memori=llenar(wk,p)
                print "memoria:",memori
            else:
                recorre2(wk)
                print "EN ESPERA"
        if(j==12):
            j=0
    else:
        break

