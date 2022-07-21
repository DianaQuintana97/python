#Diana Quintana Gamboa
#proyecto 1
#definicion de funciones
def mem(work,n):
    pc=0
    while(pc<len(work)):
        memori[pc]=work[pc]
        pc=pc+1
    return memori      
    
#programa principal
n=int(raw_input( "ingrese el tamano de la memoria:"))
print "Para dejar de ingresar trabajos inserte 5"
memori=[]
while True:
    memori=[0]*n
    work=str(raw_input("Ingrese trabajo:"))
    if(work!="5"):
        if(len(work)<n):
             print mem(work,n)
        else:
            print "NO HAY ESPACIO EN LA MEMORIA"
    else:
        break
    
