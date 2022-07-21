#Diana Quintana Gamboa
#def. de funciones 
def mergeSort(alst):
    print("Dividiendo ",alst)
    if len(alst)>1:
        md = len(alst)//2
        deralf = alst[:md]
        izalf = alst[md:]

        mergeSort(deralf)
        mergeSort(izalf)

        i=0
        j=0
        k=0
        while i < len(deralf) and j < len(izalf):
            if deralf[i] < izalf[j]:
                alst[k]=deralf[i]
                i=i+1
            else:
                alst[k]=izalf[j]
                j=j+1
            k=k+1

        while i < len(deralf):
            alst[k]=deralf[i]
            i=i+1
            k=k+1

        while j < len(izalf):
            alst[k]=izalf[j]
            j=j+1
            k=k+1
    print("Uniendo ",alst)
#Programa principal
print "===========Merge Sort------------"
cn=int(raw_input("Ingrese cantidad de numeros a ordenar: "))
alst = []
for i in range(0,cn):
    c=(int(raw_input("Ingrese numero: " )))
    alst.append(c)
    
mergeSort(alst)
print(alst)

