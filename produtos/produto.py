import sqlite3

class Produto:
    def __init__(self, id, nome, preco, descricao, quantidade, categoria_id):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade
        self.categoria_id = categoria_id

    def salvar(self):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome, preco, descricao, quantidade, categoria_id) VALUES (?, ?, ?, ?, ?)',
                        (self.nome, self.preco, self.descricao, self.quantidade, self.categoria_id))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT produtos.*, categorias.nome AS categoria FROM produtos JOIN categorias ON produtos.categoria_id = categorias.id')
        produtos_rows = cursor.fetchall()
        conn.close()
        produtos = []
        for row in produtos_rows:
            produto = {
                "id": row["id"],
                "nome": row["nome"],
                "preco": row["preco"],
                "descricao": row["descricao"],
                "quantidade": row["quantidade"],
                "categoria": row["categoria"]
            }
            produtos.append(produto)
        return produtos

    @staticmethod
    def buscar(id):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
        produto = cursor.fetchone()
        conn.close()
        return Produto(*produto) if produto else None

    @staticmethod
    def busca_por_id_nome_categoria_descricao(input_buscar):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        parametros = (input_buscar, f'%{input_buscar}%', f'%{input_buscar}%')
        cursor.execute('SELECT produtos.*, categorias.nome AS categoria FROM produtos JOIN categorias ON produtos.categoria_id = categorias.id WHERE produtos.id = ? OR produtos.nome LIKE ? OR produtos.descricao LIKE ?', parametros)
        produtos_rows = cursor.fetchall()
        conn.close()
        produtos = []
        for row in produtos_rows:
            produto = {
                "id": row["id"],
                "nome": row["nome"],
                "preco": row["preco"],
                "descricao": row["descricao"],
                "quantidade": row["quantidade"],
                "categoria": row["categoria"]
            }
            produtos.append(produto)
        return produtos

    def atualizar(self):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('UPDATE produtos SET nome = ?, preco = ?, descricao = ?, quantidade = ?, categoria_id = ? WHERE id = ?',
                        (self.nome, self.preco, self.descricao, self.quantidade, self.categoria_id, self.id))
        conn.commit()
        conn.close()

    def remover(self):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
