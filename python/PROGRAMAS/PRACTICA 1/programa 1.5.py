#DIANA QUINTANA GAMBOA
#PRACTICA 1.5
import math
def ti(a,b,c):
    if(a>=(b+c)):
        print"NO ES UN TRIANGULO"
    elif(a**2==b**2+c**2):
        print "ES UN TRIANGULO RECTANGULO"
    elif(a**2>b**2+c**2):
        print " ES UN TRIANGULO OBTUSANGULO"
    elif(a**2<b**2+c**2):
        print"ES UN TRIAMGULO ACUTANGULO"
#programa principal
print "Indicar que tipo de triangulo es"
s1=float(raw_input("Ingrese lado 1:"))
s2=float(raw_input("Ingrese lado 2:"))
s3=float(raw_input("Ingrese lado 3:"))   
if(s1>=s2 and s1>=s3):
    a=s1
    b=s2
    c=s3
    print "El TRIANGULO ES:", ti(a,b,c)
else:
    if(s2>=s1 and s2>=s3):
        a=s2
        b=s3
        c=s1
        print "El TRIANGULO ES:", ti(a,b,c)
    else:
        if(s3>=s1 and s3>=s2):
            a=s3
            b=s1
            c=s2
            print "El TRIANGULO ES:", ti(a,b,c)


