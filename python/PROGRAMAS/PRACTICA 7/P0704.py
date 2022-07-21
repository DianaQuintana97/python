#Diana Quintana Gamboa
#Def. de funciones
def revers(wk):
    if (len(wk)==1):
        return wk
    else:
        return wk[-1]+revers(wk[:-1])

#Programa principal
print "INVIERTE LA PALABRA DADA"
wk=str(raw_input("Insete palabra: "))
i=1
s=1
print "Palabras invertida: ",revers(wk)
    
