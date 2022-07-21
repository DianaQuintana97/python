#Diana Quintana Gamboa
#Def. de Funciones
import string
def ComenM(tex,sub):
    i=string.find(tex,sub)
    return i

#Programa Principal
print "Comparacion de cadenas"
tex=str(raw_input("Ingresa texto: "))
tex=tex.lower()
sub=str(raw_input("Ingresa la subcadena a buscar: "))
sub=sub.lower()
fd=ComenM(tex,sub)
new=[]
if(fd>=0):
    print "La sub cadena ",sub," esta en la palabra: "
    n=len(tex)
    i=fd
    for i in range(i,n):
        if(tex[i]!=" "):
            new.append(tex[i])
        else:
            print new
else:
    print "La sub cadena ",sub," no se encontro en ninguna posicion"
