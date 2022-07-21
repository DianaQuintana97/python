#Diana Quintana Gamboa
#programa 3.1
import math
dir(math)
#def. de funciones
def primo(a,n):
    s=int(math.sqrt(n))
    r=len(a)
    j=1
    a[0]=0
    while (j<=s-1):
        i=j+1
        if(a[j]!=0):
            p=a[j]
        while(i<=r-1):
            if(a[i]%p==0):
                a[i]=0
            i=i+1
        j=j+1
    return a
    
#programa principal
print "ENCONTRAR LOS NUMEROS PRIMOS MENORES AL NUMERO INSERTADO"
n=int(raw_input("ingrese el numero para encontrar los numeros primos menores a el :"))
a=range(1,n)
print a,"p"
print "numeros primos:",primo(a,n)


    
