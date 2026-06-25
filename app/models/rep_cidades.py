from app.bd_config import conectar_pymysql
from pprint import pprint

def select_todas_cidades():
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = "SELECT * FROM cidades"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    return(resultado)

def select_cidade(cidade_id):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = "SELECT * FROM cidades WHERE id_c = %s"
    cursor.execute(sql, (cidade_id))
    resultado = cursor.fetchone()

    return(resultado)

def select_imagens_cidade(cidade_id):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = "SELECT img_f, id_f FROM fotos WHERE cidade_f = %s"
    cursor.execute(sql, (cidade_id))
    resultado = cursor.fetchall()

    return(resultado)

if __name__ == "__main__":
    pprint(select_imagens_cidade(1)) # teste pra ver se está funcionando, escolhendo uma id de cidades