#Diana Quintana Gamboa
#porgrama 3.2
#definicion de funciones
def mayor ( a ,n ):
    b = []
    i = 0
    j = 1
    while ( i <= n and j < n ):
        y = abs( a [i] - a [j] )
        b.append( y )
        i = i + 1
        j = j + 1
    max = fmax( b )
    return max

def fmax ( b ):
    n = len( b )
    max = b [0]
    i = 1
    while ( i < n ):
        if( b [i] > max):
            max = b [i]
        i = i + 1
    return max

def menor( a ,n ):
    b = []
    i = 0
    j = 1
    while (i <= n and j < n):
        y=abs( a [i] - a [j] )
        b.append(y)
        i=i+1
        j=j+1
    min=fmin(b)
    return min

def fmin(b):
    n=len(b)
    min=b[0]
    i=1
    while(i<n):
        if(b[i]<min):
            min=b[i]
        i=i+1
    return min

#Programa Principal
print "ENCONTRAR LA DIFERENCIA MAS GRANDE Y LA MENOR DE N NUMEROS "
print "Para dejar de ingresar datos inserte 0"
a=[]
while True:
    x=int(raw_input("Dame numero: "))
    if(x>0):
        a.append(x)
    else:
        break
n=len(a)
print "La diferencia mas grande es: ",mayor(a,n)
print "La diferencia menor es: ",menor(a,n)
