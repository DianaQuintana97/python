#Diana Quintnaa Gamboa
#Def. de funciones
def cont(x,i,s):
    if(i==(len(x)-1)):
        return s
    else:
        if(x[i]==" "):
            return cont(x,i+1,s+1)
        else:
            return cont(x,i+1,s)
    
#Programa principal
print "CUENTA EL NUMERO DE PALABRAS EN UNA FRASE"
x=str(raw_input("Insete frase:\n"))
i=1
s=1
print "Palabras existentes en la frase: ",cont(x,i,s)




