#Diana Quintana Gamboa
#definicion de funciones
def sort_numbers(lst):
    for i in range(1, len(lst)):
        v=lst[i]
        j=i-1
        while(j>=0)and(lst[j]>v):
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=v
        print lst
#Programa principal
print "***********Insertion Sort***********"
lst=[]
n=int(raw_input("Ingrese cuantos numeros desea ordenar: "))
for i in range(0,n):
    x=int(raw_input("Ingrese numero: "))
    lst.append(x)
sort_numbers(lst)
print(lst)

