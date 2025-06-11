import sqlite3

def conectar():
    return sqlite3.connect("sonic.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        time TEXT,
        tipo TEXT,
        cor TEXT,
        poderes TEXT
    )
    """)

    conexao.commit()
    conexao.close()
