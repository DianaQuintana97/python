#Diana Quintana Gamboa
#Def. de funciones
def chec(wk,i,s):
    if(s!=i):
        s=wk-i
        return chec(wk,i+1,s)
    else:
        return i
#Programa principal
print "ENLISTA LOS NUMERO ENTEROS POSITIVOS QUE SON LA SUMA DE UN NUMERO DADO"
wk=int(raw_input("Inserte numero: "))
i=1
s=0
v=chec(wk,i,s)
print "sumas:"
j=1
u=0
while(j<v):
    u=wk-j
    print wk,"=",u,"+",j,"\n"
    j=j+1
    
