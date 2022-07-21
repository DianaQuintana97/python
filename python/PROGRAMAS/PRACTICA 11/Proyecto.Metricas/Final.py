import math
import sqlite3 as dbapi
from math import log
import sys

def menu():
    while True :
        print """
                    MENU DE OPCIONES

                    1.CALCULAR METRICA
                    2.CONSULTAR BASE DE DATOS
                    3.SALIR
              """
        opc= int(raw_input("INGRESE OPCION:"))
        if opc==1:
           opc1()
        elif opc==2:
            opc2()
        elif opc==3:
            print "HASTA LUEGO"
            sys.exit(3)
        else:
            print "OPCION INVALIDA"

def opc1():
    while True :
        print"Has pulsado la opcion 1..."
        print "Seleccione una opcion."
        print "\t1 - Codigo 1"
        print "\t2 - Codigo 2"
        print "\t3 - Codigo 3"
        print "\t4 - Codigo 4"
        print "\t5 - Codigo 5"
        print "\t6 - Codigo 6"
        print "\t7 - REGRESAR"
        subopc=int(raw_input("INDIQUE OPCION:"))
        if subopc==1:
            imprim(subopc)
            calcular(subopc)
            opc1()
        elif subopc==2:
            imprim(subopc)
            calcular(subopc)
            opc1()
        elif subopc==4:
            imprim(subopc)
            calcular(subopc)
            opc1()
        elif subopc==5:
            imprim(subopc)
            calcular(subopc)
            opc1()
        elif subopc==6:
            imprim(subopc)
            calcular(subopc)
            opc1()
        elif(subopc==7):
            menu()
        else:
            print "***OPCION NO VALIDA***"
            opc1()

def imprim(subopc):
    if (subopc==1):
        fichero=open("p1.txt")
    elif (subopc==2):
        fichero=open("p2.txt")
    elif(subopc==3):
        fichero=open("p3.txt")
    elif(subopc==4):
         fichero=open("p4.txt")
    elif(subopc==5):
        fichero=open("p5.txt")
    else:
        fichero=open("p6.txt")
    print fichero.read()

def calcular(subopc):
    m=0
    u=0
    n1=0
    n2=0
    N1=0
    N2=0
    if (subopc==1):
        fichero=open("p1.txt")
    elif(subopc==2):
        fichero=open("p2.txt")
    elif(subopc==3):
        fichero=open("p3.txt")
    elif(subopc==4):
         fichero=open("p4.txt")
    elif(subopc==5):
        fichero=open("p5.txt")
    else:
        fichero=open("p6.txt")
    linea=fichero.readline()
    while linea!="":
        n1,N1=bucar1(linea)
        n2,N2=buscar2(linea)
        m=N1+m
        u=N2+u
        linea=fichero.readline()
    fichero.close()
    N1=m
    N2=u
    N=N1+N2
    n=n1+n2
    V=N*log(n,2)
    D=(n1/2)*(N2/n2)
    L=1.0/D
    E=D*V
    T=E/18.0
    B=E**(2.0/3)/3000.0
    print "Longitud del programa:",N
    print "Vocabulario del programa:",n
    print "Volumen del programa:",V
    print "Dificultad del programa:",D
    print "Nivel del programa:",L
    print "Esfuerzo de implementacion:",E
    print "Tiempo de implementacion:",T
    print "Numero de Bugs liberados:",B
    s=int(raw_input("Ingresa 1 si deseas guardar. Ingresa 0 de lo contrario: "))
    if(s==1):
        Guardar(subopc,N,n,V,D,L,E,T,B)
    else:
        menu()
    

def bucar1(linea):
    s1=0
    N1=0
    s=0
    for i in range (0,len(oprdores)):
        o=oprdores[i]
        N1=linea.count(o)
        s1=s1+N1
        if(N1!=0):
            s=llenar1(o,i)
    return s,s1

def buscar2(linea):
    s2=0
    N2=0
    s=0
    for i in range (0,len(oprndos)):
        o=oprndos[i]
        N2=linea.count(o)
        s2=s2+N2
        if(N2!=0):
            s=llenar2(o,i)
    return s,s2

def llenar1(o,i):
    v[i]=o
    q=0
    for j in range(0,len(v)):
        if v[j]!="!":
            q=q+1   
    return q

def llenar2(o,i):
    vv[i]=o
    q=0
    for j in range(0,len(vv)):
        if vv[j]!="!":
            q=q+1   
    return q

def Guardar(subopc,N,n,V,D,L,E,T,B):
    bdTabla=dbapi.connect("bdProye.db")
    cursor1=bdTabla.cursor()
    cursor2=bdTabla.cursor()

    wCveProd=subopc

    cursor1.execute("""select * from metricas where codigo = ?""",(wCveProd,))
    if(not cursor1.fetchone()):

        cursor2.execute("""insert into metricas values (?,?,?,?,?,?,?,?,?)""",(wCveProd,N,n,D,V,L,E,T,B))
        bdTabla.commit()
        print "METRICAS AGREGADAS EXITOSAMENTE"
    else:
        print "YA EXISTE CODIGO",wCveProd

    cursor1.close()
    cursor2.close()
    bdTabla.close()

def opc2():
    bdTabla=dbapi.connect("bdProye.db")
    cursor=bdTabla.cursor()
    cursor.execute("""select * from metricas""")
    print "--------------------------------------------------------------------------------------------------------"
    print "CODIGO   Longitud    Vocabulario     Volumen     Dificultad  Nivel   Esfuerzo    Tiempo  Numero de Bugs"
    print "--------------------------------------------------------------------------------------------------------"

    for tupla in cursor.fetchall():
        print tupla[0], tupla[1],   tupla[2],   tupla[3],   tupla[4],   tupla[5],   tupla[6],   tupla[7],   tupla[8]
        print "--------------------------------------------------------------------------------------------------------"
        print
        bdTabla.close()
        #cursor.close()


#progrma principal
oprdores=[]
oprndos=[]
oprdores=["def ",")",",",":","=","==",">=","<=","<",">","!=","while(",
            "if(","else:","elif","+","**","-","*","%","/","float","int",
            "str","raw_input","and","[","append(","len(","True","break",
            "print","sort(","reverse(","abs(","import","range("," in "]
oprndos=["ti(","a ","b ","c ","2 ","s1 ","s2 ","s3 ","0 ","1 ","s ","i ",
           "n ","principal(","may(","max ","x ","ant ","mayor(","j ","y ",
           "fmax(","fmin(","min ","mem(","pc ","work ","momori ","ordenamientoBurbuja",
         "lst","tam","k ","list ","cn ","m"]
s=len(oprdores)
v=["!"]*s
d=len(oprndos)
vv=["!"]*d
menu()
