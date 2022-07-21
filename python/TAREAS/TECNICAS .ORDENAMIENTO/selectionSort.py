#Diana Quintana Gamboa
#definiciones de funciones
def selectionsort(lta,tam):
    for i in range(0,tam-1):
        min=i
        for j in range(i+1,tam):
            if lta[min] > lta[j]:
                min=j
        aux=lta[min]
        lta[min]=lta[i]
        lta[i]=aux
        print lta
#programa principal
print "===========Selection Sort------------"
lta=[]
cn=int(raw_input("Cantidad de numeros a ingresar: "))
for i in range(0,cn):
    m=(int(raw_input("Ingrese numero: ")))
    lta.append(m)
selectionsort(lta,len(lta))
print lta

