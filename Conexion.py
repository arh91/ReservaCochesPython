"""Comprobamos que se establezca correctamente la conexión entre Python y MySQL"""

import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='castelao',
        db='UD02BDReservaCoches')

    if conexion.is_connected():
        print("Conexión exitosa")
        info_server = conexion.get_server_info()
        print(info_server)
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
        print("Conectado a la base de datos: {}".format(row))
except Exception as ex:
    print(ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexión finalizada.")


