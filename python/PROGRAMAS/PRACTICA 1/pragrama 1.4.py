#DIANA QUINTANA GAMBOA
#PRACTICA 1.4
import math
def are(b,a):
    area=(b*a)/2.0
    return area
#programa principal
print "AREA DE UN RECTANGULO"
b=float(raw_input("Ingrese base:"))
a=float(raw_input("Ingrese altura:"))
if (b<0 or a<0):
    print "Error inserto un numero negativo el area no se puede calcular"
else:
    print "El area es:",are(b,a)
