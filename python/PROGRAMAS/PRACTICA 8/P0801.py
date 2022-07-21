#Diana Quintana Gamboa 
#Def. de funciones
def inserta(u, lst, i):
    return lst[:i] + [u] + lst[i:]
def insmultiple(u, lst):
    return [inserta(u,lst,i)for i in range(len(lst)+1)]
def permuta(c):
    if(len(c) == 0):
        return[[]]
    return sum([insmultiple(c[0],p)
                for p in permuta(c[1:])],[])
        
#Programa principal
print "  ********Anagramas******* "
c=str(raw_input("ingrese palabra"))
print permuta(c)
