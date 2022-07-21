#Diana Quintana Gamboa 
#Definicion de funciones
def Monedas(N,n,dinero,c):
    for i in range(0,n):
        for j in range(0,N+1):
            if (j==0):
                c[i][j]=0
            elif (i==0):
                c[i][j]=j
            elif(j<dinero[i]):
                c[i][j]= c[i-1][j]
            else:
                c[i][j]=min(c[i-1][j],1+c[i][j-dinero[i]])
                
    return c

                
#Programa Principal
print "DAR CAMBIO CON PROGRAMACION DINAMICA"
cd=int(raw_input("Ingrese numero de monedas: "))
cant=['Cantidad']
dinero=[]
for i in range(0,cd):
    print "MONEDA",i+1
    x=int(raw_input("Ingrese valor: "))
    dinero.append(x)
N=int(raw_input("Ingrese cantidad a pagar: "))
m=[]
for i in range(cd+1):
    n=[]
    for i in range(N+1):
        n.append(0)
    m.append(n)
cambio=Monedas(N,cd,dinero,m)
for i in range(0,N+1):
    cant.append(i)
print cant
for i in range(0,cd):
    print "|  d",dinero[i],"   |",cambio[i]

