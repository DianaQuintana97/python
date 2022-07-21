import random
#DIANA QUINTANA GAMBOA
#Def. de funciones 
def bogosort(l):
    while not in_order(l):
        random.shuffle(l)
    return l
 
def in_order(l):
    if not l:
        return True
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True

def in_order(l):
    return all( l[i] <= l[i+1] for i in xrange(0,len(l)-1))

#Programa principal
print "===========Bogo Sort------------"
lst=[]
cn=int(raw_input("Cantidad de numeros a ingresar: "))
for i in range(0,cn):
        m=(int(raw_input("Ingrese numero: " )))
        lst.append(m)
bogosort(lst)
print lst
