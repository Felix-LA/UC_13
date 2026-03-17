import mysql.connector

def conectar():
    # Estabelece conexão com o servidor MySQL.
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crud_usuario"
    )

def criar_banco_e_tabela():
    conn = mysql.connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS crud_usuario")
    cursor.execute("USE crud_usuario")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            endereco VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def inserir_usuario(nome, email, endereco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO usuario (nome, email, endereco) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, email, endereco))
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    dados = cursor.fetchall()
    conn.close()
    return dados

def atualizar_usuario(id, nome, email, endereco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE usuario SET nome=%s, email=%s, endereco=%s WHERE id=%s"
    cursor.execute(sql, (nome, email, endereco, id))
    conn.commit()
    conn.close()

def excluir_usuario(id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM usuario WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()

criar_banco_e_tabela()