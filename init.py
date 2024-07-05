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

cursor.execute('''
INSERT INTO Categorias (nome) VALUES
('Alimentos'),
('Bebidas'),
('Limpeza'),
('Higiene'),
('Eletrônicos'),
('Outros')
''')

cursor.execute('''
INSERT INTO Produtos (Nome, Preco, Descricao, Quantidade, Categoria_id) VALUES
('Arroz', 10.0, 'Arroz branco', 100, 1),
('Feijão', 8.0, 'Feijão carioca', 100, 1),
('Macarrão', 5.0, 'Macarrão espaguete', 100, 1),
('Refrigerante', 5.0, 'Refrigerante de cola', 100, 2),
('Suco', 5.0, 'Suco de laranja', 100, 2),
('Água', 2.0, 'Água mineral', 100, 2),
('Sabão', 3.0, 'Sabão em pó', 100, 3),
('Detergente', 2.0, 'Detergente neutro', 100, 3),
('Desinfetante', 5.0, 'Desinfetante floral', 100, 3),
('Shampoo', 10.0, 'Shampoo para cabelos oleosos', 100, 4),
('Condicionador', 10.0, 'Condicionador para cabelos oleosos', 100, 4),
('Sabonete', 2.0, 'Sabonete de glicerina', 100, 4),
('Fone de ouvido', 50.0, 'Fone de ouvido sem fio', 100, 5),
('Carregador', 30.0, 'Carregador de celular', 100, 5),
('Mouse', 20.0, 'Mouse sem fio', 100, 5),
('Caneta', 5.0, 'Caneta esferográfica', 100, 6)
''')

conn.commit()
conn.close()
