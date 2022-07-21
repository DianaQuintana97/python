#DIANA QUINTANA GAMBOA
import sqlite3 as dbapi
#Definicion de funciones
def fxcapProd():
    bdProd=dbapi.connect("bdTienda.db")
    cursor1= bdProd.cursor()
    cursor2=bdProd.cursor()
    wCveProd=int(raw_input("Clave Producto: "))

    cursor1.execute("""select * from tprod where CveProd = ?""",(wCveProd,))
    if (not cursor1.fetchone()):
        wNomProd= raw_input("Nombre Producto: ")
        wPreProd = float(raw_input("Precio Producto: "))

        cursor2.execute("""insert into tprod values
(?,?,?)""",(wCveProd,wNomProd,wPreProd))
        bdProd.commit()

        print " PRODUCTO AGREGADO EXITOSAMENTE"
    else:
        print "YA EXISTE PRODUCTO CON CLAVE ", wCveProd

    cursor1.close()
    cursor2.close()
    bdProd.close()

def fxBorraProd():
    bdProd=bdapi.connect("bdTienda.db")
    cursor=bdProd.cursor()
    wCveProd=int(raw_input("Clave Producto: "))
    cursor.execute("""select * from tprod where CveProd = ?""",(wCveProd,))
    if cursor.fetchone():
        cursor.execute("""delete form tprod where CveProd =?""",(wCveProd,))
        bdProd.commit()
        print "PRODUCTO BORRADO EXITOSAMENTE"
    else:
        print "NO EXISTE PRODUCTO CON CLAVE",wCveProd

def fxModProd():
    bdProd=dbapi.connect("bdTienda.db")
    cursor=bdProd.cursor()
    wCveProd=int(raw_input("Clave Producto: "))
    cursor.execute("""select * from tprod where CveProd = ?""",(wCveProd,))
    if cursor.fetchone():
        wNomProd=raw_input("Nuevo Nombre del Producto: ")
        wPreProd=float(raw_input("Nuevo precio del producto: "))

        cursor.execute("""update tprod set NomProd=?,PreProd=? where CveProd=?""",(wNomProd,wPredProd,wCveProd))
        bdProd.commit()
        print "PRODUCTO MODIFICADO EXITOSAMENTE"
    
    else:
        print "NO EXISTE PRODUCTO CON CLAVE ",wCveProd

def fxlisProd():
    bdProd = dbapi.connect("bdTienda.db")
    cursor = bdProd.cursor()
    cursor.execute("""select * from tprod""")
    print
    print"----------------------------------"
    print"CLAVE       NOMBRE          PRECIO"
    print"------ ------------------ --------"

    for tupla in cursor.fetchall():
        print tupla[0],tupla[1],tupla[2]
    print "---------------------------------"
    print
    cursor.close()
    bdProd.close()


#Programa Principal
while True:
    print """
                MENU DE OPCIONES
                1. CAPTURAR PRODUCTOS
                2. BORRAR PRODUCTOS
                3. MODIFICAR PRODUCTOS
                4. LISTAR PRODUCTOS
                5. SALIR
          """
    wopcion= int(raw_input("DAME TU OPCION: "))
    if (wopcion==1):
        print "CAPTURAR PRODUCTOS"
        fxcapProd()
    elif (wopcion==2):
        print "BORRAR PRODUCTOS..."
        fxBorraProd()
    elif(wopcion==3):
        print "MODIFICAR PRODUCTOS..."
        fxModProd()
    elif(wopcion==4):
        print "LISTAR PRODUCTOS"
        fxlisProd()
    else:
        break
