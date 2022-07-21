#DIANA QUINTANA GAMBOA
#Def.de funciones 
def heapsort( aList ):
  length = len( aList ) - 1
  leastParent = length / 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )
 
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )
 
 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1
 
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      first = largest;
      largest = 2 * first + 1
    else:
      return
    
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
#PROGRAMA PRINCIPAL
print "==================HEAP SORT---------------------"
T = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
print T
heapsort(T )
print T

