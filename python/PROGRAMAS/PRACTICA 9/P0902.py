#Diana Quintana Gamboa
#definicion de funciones
def llenarA(fA,cA):
    for i in range(fA):
        mA.append([])
        for j in range(cA):
            mA[i].append(None)
    for f in range(fA):
        for c in range(cA):
            mA[f][c]=int(raw_input("ingrese numero: "))
    return mA
def llenarB(fB,cB):
    for i in range(fB):
        mB.append([])
        for j in range(cB):
            mB[i].append(None)
    for f in range(fB):
        for c in range(cB):
            mB[f][c]=int(raw_input("ingrese numero: "))
    return mB
def mltp(fA,cB,cA,mA,mB):
    s=0
    for k in range(fA):
        mC.append([0]*cB)
        for i in range(cB):
            mC[k][i]=0
    for i in range(fA):
        for j in range(cA):
            s=0
            for k in range(cB):
                s+=(mA[i][k]*mB[k][j])
                mC[i][j]=s
    return mC
#Programa principal
print "MULTIPLICACION DE MATRICES"
mA=[]
mB=[]
mC=[]
fA=int(raw_input("Ingrese numero de filas en matriz A: "))
cA=int(raw_input("Ingrese numero de columnas en matrz A: "))
fB=int(raw_input("Ingrese numero de filas en matriz B: "))
cB=int(raw_input("Ingrese numero de columnas en matrz B: "))

if(cA==fB):
    print "*** DATOS DE LA MATRIZ A ***"
    mA=llenarA(fA,cA)
    print "*** DATOS DE LA MATRIZ B ***"
    mB=llenarB(fB,cB)
    print "*** PRODUCTO DE LA MULTIPLICACION DE MATRICES AxB ***"
    mltp(fA,cB,cA,mA,mB)
    print "-----MATRIZ RESULTANTE-----"
    for k in mC:
        print k
    print "------MATRIZ A--------"
    for k in mA:
        print k
    print "------MATRIZ B--------"
    for k in mB:
        print k
else:
    print "No teiene solucion"


    
