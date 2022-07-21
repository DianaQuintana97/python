#Diana Quintana Gamboa 

import sqlite3 as dbapi

bdProd = dbapi.connect("bdTienda.db")
cursor = bdProd.cursor()
cursor.execute("""create table tprod(cveProd integer(6),
                nomProd char(40),
                preProd fload(6,2))""")

bdProd.commit()
cursor.close()
bdProd.close()
