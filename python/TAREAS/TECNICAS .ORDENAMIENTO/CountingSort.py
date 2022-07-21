#DIANA QUINTANA GAMBOA 
def countingsort( aList, k ):
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i] += 1
 
    ndx = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        aList[ndx] = i
        ndx += 1
        counter[i] -= 1
def buscar():
    max=lst[0]
    i=1
    while(i<len(lst)):
        if(lst[i]>max):
            max=lst[i]
        i=i+1
    return max
#Programa principal
print "===========Counting Sort------------"
lst=[]
cn=int(raw_input("Cantidad de numeros a ingresar: "))
for i in range(0,cn):
        m=(int(raw_input("Ingrese numero: " )))
        lst.append(m)
max=buscar()
countingsort(lst,max)
print lst
