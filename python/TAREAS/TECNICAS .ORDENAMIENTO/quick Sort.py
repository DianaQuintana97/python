#DIANA QUINTANA GAMBOA 
import os
import math
#Def. de Funciones
def quicksort(cadena):
    menor = []
    igual = []
    mayor = []

    if len(cadena) > 1:
        pivot = cadena[0]
        for x in cadena:
            if x < pivot:
                menor.append(x)
            if x == pivot:
                igual.append(x)
            if x > pivot:
                mayor.append(x)
        print quicksort(menor)+quicksort(igual)+quicksort(mayor) 
        return quicksort(menor)+quicksort(igual)+quicksort(mayor) 
    else:
        return cadena

#Programa principal
print "-------------ALGORITMO DE QUICKSORT-----------"
cadena=[]
x=int(raw_input("INGRESE EL NUMERO DE DATOS A INGRESAR: "))
i=1
while (i<=x):
    n=int(raw_input("INGRESE DATO:"))
    cadena.append(n)
    i+=1
cadena = quicksort(cadena)
print "SU LISTA ORDENADA CON EL METODO QUICKSORT ES:",  cadena

