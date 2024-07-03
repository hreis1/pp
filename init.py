import sqlite3

conn = sqlite3.connect('./supermecado.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Produtos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Preco REAL NOT NULL,
    Descricao TEXT,
    Quantidade INTEGER NOT NULL,
    Categoria_id INTEGER,
    FOREIGN KEY (Categoria_id) REFERENCES Categorias(ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Vendas (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Produto_id INTEGER,
    Quantidade INTEGER NOT NULL,
    Valor REAL NOT NULL,
    Data TEXT NOT NULL,
    FOREIGN KEY (Produto_id) REFERENCES Produtos(ID)
)
''')

conn.commit()
cursor.close()