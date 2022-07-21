#DIANA QUINTANA GAMBOA
#Def. de funciones 
def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for  i in aList:
      tmp = i / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX

#Programa principal
print "***********Radix Sort***********"
lst=[]
n=int(raw_input("Ingrese cuantos numeros desea ordenar: "))
for i in range(0,n):
    print "Ingrese numero",i+1
    x=int(raw_input("- "))
    lst.append(x)
radixsort( lst )
print lst
