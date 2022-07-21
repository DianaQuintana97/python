#DIANA QUINTANA GAMBOA
#PRACTICA 1.3
import math
def DesEE(x1,x2,x3,x4,x5):
    sx=(x1+x2+x3+x4+x5)/5.0
    suma=(sx-x1)**2+(sx-x2)**2+(sx-x3)**2+(sx-x4)**2+(sx-x5)**2
    rho=math.sqrt((1/5.0)*suma)
    return rho
#programa principal
print "Calcular la deviacion estandar de 5 numeros"
x1=float(raw_input("Ingrese numero:"))
x2=float(raw_input("Ingrese numero:"))
x3=float(raw_input("Ingrese numero:"))
x4=float(raw_input("Ingrese numero:"))
x5=float(raw_input("Ingrese numero:"))
print "Desviacion estandar estadistica es:", DesEE(x1,x2,x3,x4,x5)




