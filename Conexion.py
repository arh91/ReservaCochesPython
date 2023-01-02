import mysql.connector

conexion = mysql.connector.connect(
    user='alvaro',
    password='castelao',
    host='localhost',
    database='UD02BDReservaCoches',
    port='3306')
print(conexion)


