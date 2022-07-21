#Diana Quintana Gamboa
#programa 2.1
def media(a,n):
    s=0
    n=0
    for elemento in a:
           s = s+ elemento
           n=n+1
           
    mda=s/n
    return mda
def mediana(a,n):
    o=n/2
    if(n%2!=0):
        y=a[o]
        return y
    else:
        ym=(a[o]+a[o-1])/2
        return ym
def moda(a,n):
    aux=0
    ct=0
    mda=-1
    a.sort(cmp=None, key=None, reverse=False)
    for i in range(0,n-1):
        if (a[i]==a[i+1]):
            ct=ct+1
            if ct >= aux:
                aux = ct
                mda = a[i]
        else:
            ct=0
 
    return mda
        
#Preograma principal
print "CALCULAR LA MEDIA,MEDIANA Y MODA DE CIERTOS NUMEROS"
a=[7,5,9,10,8,6,6,7,9,12,9]
b=[8,12,23,12,10,16,26,12,14,8,16,23]
a.sort()
b.sort()
n=len(a)
nb=len(b)
print"la media de a:",media(a,n)
print"la media de b:",media(b,nb)
print"la mediana de a:",mediana(a,n)
print"la mediana de b:",mediana(b,nb)
print "La moda de a : ", moda(a,n)
print "La moda de b : ", moda(b,nb)

