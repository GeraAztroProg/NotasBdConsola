import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'master_python',
        port = 3306
    )

    # print(database) -> saber si se ha conectado

    cursor = database.cursor(buffered=True)

    return[database, cursor]