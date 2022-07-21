#DIANA QUINATANA GAMBOA
#programa 1.2
import math
def op(C,X,Y):
    cx=(X/100.0)*C
    cy=(Y/100.0)*C
    CT=cy+cx+C
    return CT

#programa principal
print "CALCULAR COSTO DE UN VEHICULO"
C=float(raw_input("Ingrese costo del vehiculo:"))
X=float(raw_input("Ingrese el porcentaje de ganacias del vendedor:"))
Y=float(raw_input("Ingrese el porcentaje de los impuestos locales o estatales aplicables:"))
print "Costo del vehiculo:",op(C,X,Y)


