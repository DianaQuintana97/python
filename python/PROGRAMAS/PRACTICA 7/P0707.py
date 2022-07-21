#Diana Quintana Gamboa
#Def. de funciones
def med(x,y):
    if(y==0):
        return x
    if(y>0):
        return med(y,x%y) 
#Programa principal
print "MAXIMO COMUN DIVISOR"
x=int(raw_input("Ingrese x: "))
y=int(raw_input("Ingrese y: "))
print" El numero es:", med(x,y)

