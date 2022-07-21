#Diana Quintana Gamboa
#programa 2.3
def facI(n):
    if(n==0):
      return 1
    else:
        i=1
        fac=1
        while(i<=n):
            fac=fac*i
            i=i+1
        return fac
    
def fac(n):
    if(n==0):
        return 1
    else:
        return n*fac(n-1) 
#Programa prncipal
print "FACTORIAL DE UN NUMERO "
n=int(raw_input("Ingrese numero:"))
print "el factorial recursivo es:",fac(n)
print "el factorial iterado es:",facI(n)





    
