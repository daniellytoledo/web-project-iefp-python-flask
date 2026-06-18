import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_pymysql():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        autocommit=False,
        cursorclass=pymysql.cursors.DictCursor
    )

sql = "SELECT * FROM cidades"
conexao = conectar_pymysql()

try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    print(resultado)

finally:
    cursor.close()
    conexao.close()