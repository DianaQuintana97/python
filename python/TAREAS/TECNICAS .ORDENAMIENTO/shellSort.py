#DIANA QUINTANA GAMBOA
#Def. de funciones 
def shellSort(lista):
    n = len(lista)
    gap = n / 2
    while gap > 0:
        for i in xrange(gap, n):
            val = lista[i]
            j = i
            while j >= gap and lista[j-gap] > val:
                lista[j] = lista[j-gap]
                j -= gap

            lista[j] = val
            print lista

        gap /= 2

#Programa principal
print "===========Shell Sort------------"
lst=[]
cn=int(raw_input("Cantidad de numeros a ingresar: "))
for i in range(0,cn):
        m=(int(raw_input("Ingrese numero: " )))
        lst.append(m)

shellSort(lst)
print "Lista ordenada:"
print lst, "\n"

