#DIANA QUINTANA GAMBOA 
def mochila(w,p,capacidadW,T):
    for c in range(capacidadW+1):
      T[0][c]=0
    for j in range(1,len(w)+1):
      for c in range(capacidadW+1):
        if c >= w[j-1]:
            T[j][c]=max(T[j-1][c],T[j-1][c-w[j-1]]+p[j-1])
        else:
            T[j][c]=T[j-1][c]
    for i in range(len(w)+1):
        print T[i]
#PROGRAMA PRINCIPAL 
w=[]
p=[]
n=int(raw_input("Ingrese numero de objetos: "))
capacidadW=int (raw_input("Ingrese capasidad total de la mochola : "))
for i in range(0,n):
    print "Objeto:",i+1
    x=int(raw_input("Ingrese peso: "))
    w.append(x)
    xx=int(raw_input("Ingrese costo: "))
    p.append(xx)

T = []
for i in range(len(w)+1):
  ea_row = []
  for j in range(capacidadW+1):
    ea_row.append(0)
  T.append(ea_row)


mochila(w,p,capacidadW,T)
