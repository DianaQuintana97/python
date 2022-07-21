#Diana Quintnaa Gamboa
#Def. de funciones
def sum(x):
    if (x==0):
        return 0
    else:
        return x+sum(x-1)
#Programa principal
print "Calcula la suma s=1+2+3+...+(n-1)+n"
x=int(raw_input("Dame numero:"))
print "la suma es: ",sum(x) 

