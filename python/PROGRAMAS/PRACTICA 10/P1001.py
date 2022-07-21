#DIANA QUINTANA GAMBOA 
#Def. de Funciones

def variables(v):
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
    if(t==1):
        print "Las combinaciones posibles son: ",v

#Programa Principal
print "Programa que lee un circuito con resultado 1"
c=65536
n=16
matriz=[]

for i in range (0,c):
    matriz.append([0]*n)

j=0
cb=c
while(j<n):
    k=0
    cb=cb/2
    l=1
    while(k<c):
        l=1
        while(l<=cb):
            matriz[k][j]=1
            k=k+1
            l=l+1
        l=1
        while(l<=cb):
            matriz[k][j]=0
            k=k+1
            l=l+1
    j=j+1
    
for i in range(0,c):
    variables(matriz[i])
        
