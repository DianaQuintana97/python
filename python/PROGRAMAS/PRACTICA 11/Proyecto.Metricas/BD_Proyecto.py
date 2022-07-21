import sqlite3 as dbapi

#Programa principal
bdTabla=dbapi.connect("bdProye.db")
cursor=bdTabla.cursor()


cursor.execute("""create table metricas (codigo integer(1),LP integer(3), VP integer(3),VolP float(6,2),DP float(6,2),NP float(10,2), EI float(6,2), TI float(6,2), NBL float(6,2))""")

bdTabla.commit()
cursor.close()
bdTabla.close()
