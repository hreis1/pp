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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    descricao TEXT,
    quantidade INTEGER NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantidade INTEGER NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL,
    produto_id INTEGER,
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
INSERT INTO Produtos (nome, preco, descricao, quantidade, categoria_id) VALUES
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
