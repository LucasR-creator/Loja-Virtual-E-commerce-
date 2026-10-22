import sqlite3
from pathlib import Path

DB = Path(__file__).with_name('nexashop.db')

def conectar():
    return sqlite3.connect(DB)

def criar_tabelas():
    with conectar() as conexao:
        conexao.execute('''CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL CHECK(preco > 0),
            estoque INTEGER NOT NULL CHECK(estoque >= 0),
            imagem TEXT DEFAULT ''
        )''')
        colunas = [col[1] for col in conexao.execute('PRAGMA table_info(produtos)')]
        if 'imagem' not in colunas:
            conexao.execute("ALTER TABLE produtos ADD COLUMN imagem TEXT DEFAULT ''")
        conexao.execute('''CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            cliente TEXT NOT NULL,
            nota INTEGER NOT NULL CHECK(nota BETWEEN 1 AND 5),
            comentario TEXT,
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )''')

if __name__ == '__main__':
    criar_tabelas()
    print('Banco de dados pronto!')
