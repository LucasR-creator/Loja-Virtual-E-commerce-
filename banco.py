
import sqlite3


def conectar():
    return sqlite3.connect("nexashop.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            cliente TEXT NOT NULL,
            nota INTEGER NOT NULL CHECK(nota BETWEEN 1 AND 5),
            comentario TEXT,
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    """)

    conexao.commit()
    conexao.close()

    print("Banco de dados criado com sucesso!")


if __name__ == "__main__":
    criar_tabelas()
