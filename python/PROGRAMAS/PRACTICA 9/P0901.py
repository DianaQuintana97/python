#Diana Quintana Gamboa
#definicion de funciones
import math
def mcd(a,b):
    if(b==0):
        return a
    else:
        return mcd(b,a%b)
#Programa principal
print "Maxino comun divisor: "
a=int(raw_input("ingresa a:"))
b=int(raw_input("ingresa b:"))
print "Maxino comun divisor:",mcd(a,b)
