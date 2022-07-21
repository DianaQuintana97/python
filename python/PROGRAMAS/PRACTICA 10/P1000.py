#DIANA QUINTANA GAMABOA
#Def de Funciones
def variables(a):
    a=v[0]
    b=v[1]
    c=v[2]
    d=v[3]
    e=v[4]
    f=v[5]
    g=v[6]
    h=v[7]
    i=v[8]
    j=v[9]
    k=v[10]
    l=v[11]
    m=v[12]
    n=v[13]
    o=v[14]
    p=v[15]
    return circuito(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

def circuito(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    ab=a or b
    cd=c or d
    bd=(not b) or (not d)
    de=(not d) or (not e)
    ef=(not f) or g
    fg=f or g
    fnotg= f or (not g)
    hnoti=h or (not i)
    ij=i or j
    inotj=i or (not j)
    jk=(not j) or (not k)
    kl=k or l
    jl=j or l
    mn=m or n
    hn=(not h) or (not n)
    no=n or (not o)
    op=o or p
    gnotp=g or (not p)

    abbd=ab and bd
    cdde=cd and de
    effg=ef and fg
    fghi=fnotg and hnoti
    ijij=ij and inotj
    jkkl=jk and kl
    jlmn=jl and mn
    opgp=op and gnotp
    opgpno=opgp and no
    opgpnohn=opgpno and hn

    abcd=abbd and cdde
    efhi=effg and fghi
    ijjk=ijij and jkkl
    jlop=jlmn and opgpnohn

    abef=abcd and efhi
    ijjl=ijjk and jlop

    t=abef and ijjl
    if(t==False):
        return 0
    else:
        return 1
    
    

#Programa Principal
print "Obtener el resultado binario de una funcion binaria"
cad=str(raw_input("Ingresa una cadena binaria de 16 caracteres: "))
i=0
n=len(cad)
v=[0]*n
if(n!=16):
    print "La cadena incorrecta,debe contener 16 caracteres"
else:
    while(i<n):
        v[i]=cad[i]
        i=i+1
    print v
    r=variables(v)
    print "El resultado es: ",r
