import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("sonic.db")

# Função para criar a tabela (caso ainda não exista)
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT,
        time TEXT,
        cor TEXT,
        poderes TEXT
    )
    """)

    conexao.commit()
    conexao.close()

# Função para adicionar um novo personagem
def adicionar_personagem(nome, tipo, time, cor, poderes):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO personagens (nome, tipo, time, cor, poderes)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, tipo, time, cor, poderes))

    conexao.commit()
    conexao.close()

# Função para listar todos os personagens
def listar_personagens():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM personagens")
    resultados = cursor.fetchall()

    conexao.close()
    return resultados

# Função para atualizar um personagem existente
def atualizar_personagem(id, nome, tipo, time, cor, poderes):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE personagens
        SET nome = ?, tipo = ?, time = ?, cor = ?, poderes = ?
        WHERE id = ?
    """, (nome, tipo, time, cor, poderes, id))

    conexao.commit()
    conexao.close()

# Função para deletar um personagem
def deletar_personagem(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM personagens WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()


# Função para verificar se um personagem existe pelo ID
def buscar_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM personagens WHERE id = ?", (id,))
    resultado = cursor.fetchone()

    conexao.close()
    return resultado  # Retorna None se não achar

# Função que realiza uma busca por campo e valor
def buscar_por_campo(campo, valor):
    conexao = conectar()
    cursor = conexao.cursor()

    query = f"SELECT * FROM personagens WHERE {campo} LIKE ?"
    cursor.execute(query, (f"%{valor}%",))

    resultados = cursor.fetchall()
    conexao.close()
    return resultados


# Função para importar dados de um arquivo SQL
def importar_sql(caminho_arquivo):
    conexao = conectar()
    cursor = conexao.cursor()

    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        sql = f.read()
        cursor.executescript(sql)

    conexao.commit()
    conexao.close()


# Função para apagar todos os dados da tabela
def limpar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM personagens")
    conexao.commit()
    conexao.close()

