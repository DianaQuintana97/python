#Diana Quintana Gamboa
#definicion de funciones
def ordenamientoBurbuja(lst,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lst[j] > lst[j+1]):
                k = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = k
                print lst
 #Programa principal
print "===========Bubble Sort------------"
lst=[]
cn=int(raw_input("Cantidad de numeros a ingresar: "))
for i in range(0,cn):
        m=(int(raw_input("Ingrese numero: " )))
        lst.append(m)
ordenamientoBurbuja(lst,len(lst))
print lst
