#Diana Quintnaa Gamboa
#Def. de funciones
def sum(x):
    if x==0:
        return 0
    else:
        return x+sum(x-2)
#Programa principal
print "Calcula la suma de los numeros pares hasta n:s=2+4+6+...+(n-2)+n"
x=int(raw_input("Dame numero:"))
if(x%2==0):
    print "la suma es: ",sum(x)
else:
    x=x-1
    print "la suma es: ",sum(x)


