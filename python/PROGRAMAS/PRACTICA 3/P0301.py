#Diana Quintana Gamboa
#programa 3.1
#def. de funciones

def may(a,n):
    a.sort()
    a.reverse()
    max=a[0]
    ant=a[1]
    i=1
    while(i<n):
        if(a[i]>max):
            ant=[i]
            max=a[i]
        i=i+1
    return max,ant
    
#programa principal
print "ENCONTRAR EL PRIMERR Y SEGUNDO DATO MAYOR"
print "Para dejar de ingresar numeros inserte 0"
a=[]
while True:
    x=int(raw_input("Dame numero:"))
    if(x>0):
        a.append(x)
        n=len(a) 
    else:
        break
print "El primer y segundo elemento mayores son:",may(a,n)

