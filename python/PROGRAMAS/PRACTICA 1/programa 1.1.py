#DIANA QUINTANA GAMBOA
#PRACTICA 1.1
import math
def area(S1,S2,S3):
    T= (S1+S2+S3)/2.0
    ar=math.sqrt(T*abs(T-S1)*abs(T-S2)*abs(T-S3))
    return ar
#programa principal
print "Calcular area de un triangulo"
S1=float(raw_input("Ingrese lado 1:"))
S2=float(raw_input("Ingrese lado 2:"))
S3=float(raw_input("Ingrese lado 3:"))
print "Area del triangulo es:",area(S1,S2,S3)


