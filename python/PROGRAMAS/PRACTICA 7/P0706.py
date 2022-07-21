#Diana Quintana Gamboa 
#Def. de funciones
def Ackerman(i,j):
    if(i==1):
      return 2**j;
    elif(j==1  and i>=2):
        return Ackerman(i-1, 2)
    else:
        return Ackerman(i-1, Ackerman(i, j-1))
#Programa principal
print "FUNCION ACKERMAN"
i=int(raw_input("Ingrese i: "))
j=int(raw_input("Ingrese j: "))
print" El numero es:", Ackerman(i,j)

        
