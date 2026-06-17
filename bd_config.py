import pymysql

def conectar_pymysql():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="gAMOVER123.",
        database="cidades",
        autocommit=False,
        cursorclass=pymysql.cursors.DictCursor
    )

sql = "SELECT * FROM cidades"
conexao = conectar_pymysql()
cursor = conexao.cursor()
cursor.execute(sql)
resultado = cursor.fetchall()

print(resultado)