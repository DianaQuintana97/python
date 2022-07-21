#def. funciones
def dis(v):
    i=0
    j=2
    while(i<len(v)-1):
        j=2
        j=j+i
        while(j<len(v)-1):
            pi=(v[i]-v[j])**2
            pj=(v[i+1]-v[j+1])**2
            ds=(pi+pj)**(1.0/2)
            d.append(ds)
            j=j+2
        i=i+2
    return d
def final(d,v):
    aux=d[0]
    i=0
    while(i<len(d)):
        if(aux>d[i]):
            aux=d[i]
        i=i+1
    i=0
    j=2
    while(i<len(v)-1):
        j=2
        j=j+i
        while(j<len(v)-1):
            pi=(v[i]-v[j])**2
            pj=(v[i+1]-v[j+1])**2
            ds=(pi+pj)**(1.0/2)
            if(ds==aux):
                print "distancia menor:",ds
                print "Los puntos son:","(",v[i],",",v[i+1],")","-","(",v[j],",",v[j+1],")"
            j=j+2
        i=i+2
#Programa principal
print"ENCONTRAR LOS PUNTOS MAS CERCANOS "
x=int(raw_input("cuantos puntos desea ingresar:"))
v=[]
d=[]
i=0
f=0
while (i < x ):
    print "Punto",i+1
    j=int(raw_input("Ingrese coordenada x:"))
    v.append(j)
    f=f+1
    k=int(raw_input("Ingrese coordenada y:"))
    v.append(k)
    i=i+1
dis(v)
final(d,v)


    
    
        
        
        
