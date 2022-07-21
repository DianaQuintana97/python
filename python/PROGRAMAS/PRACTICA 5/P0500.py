#DIANA QUINTANA GAMBOA
#Definicion de funciones
def memoria(memo,vm,wk,lissE):
    n=len(wk)
    m=checar(n,vm,memo,wk)
    if (m==-1):
        print "En espera"
def  checar(n,vm,memo,wk):
    j=0
    k=-1
    while (j<len(vm)):
        if(n<vm[j]):
            l=BusInt(j,vm)
            q=lleno(l,memo)
            if(q!=1):
                memo=llenar(memo,l,wk)
                return j
                break
            else:
                 j=j+1
        else:
            j=j+1
    return k
def BusInt(j,vm):
    r=0
    si=0
    y=0
    while (r!=j):
        si=si+vm[r]
        r=r+1
    if(r==0):
        y=0
        return y
    else:
        si=si+vm[j]
        y=si-vm[j]
        return y
def llenar(memo,l,wk):
    x=l
    u=0
    while(u<len(wk)):
        memo[x]=wk[u]
        x=x+1
        u=u+1
    return memo
def lleno (l,memo):
    if(memo[l]==0):
        return 0
    else:
        return 1
def meter(wk,lisE):
    i=0
    while (i<len(lisE)):
        if(lisE[i]=="0"):
            lisE[i]=wk
        i=i+1
#Programa Principal
p=int(raw_input("Dame numero de particiones: "))
i=1
vm=[]  #tam de particiones 
sm=0
while(i<=p):
    tm=int(raw_input("Inserte longitud de particion: "))
    vm.append(tm)
    sm=sm+tm
    i=i+1
memo=[0]*sm
lisE=[0]*sm
print "Para terminar de ingresar trabajos presione 0"
while True:
    wk=raw_input("Inserte trabajo: ")
    if (wk!="0"):
        memoria(memo,vm,wk,lisE)
        print "MEMORIA:"
        print memo
    else:
        break
    
