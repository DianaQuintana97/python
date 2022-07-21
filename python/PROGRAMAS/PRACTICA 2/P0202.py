#Diana Quintana Gamboa
#programa 2.2
def su(n):
    if(n==0):
        return 0
    else:
        return n+su(n-1) 
    
def suma(n):
    resultado=0
    i=1
    while(i<=n):
        resultado=resultado+i
        i=i+1
    return resultado
#programa principal
print "SUMA DE 1+23+...+N"
n=int(raw_input("Ingresa un tope: "))
print "La suma de los nummeros iterada es: ",suma(n)
print "La suma de los nummeros recursiva es: ",su(n)



