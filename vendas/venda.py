import sqlite3

class Vendas:
    def __init__(self, id, produto_id, quantidade, valor, data):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.valor = valor
        self.data = data

    def vender(self):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT quantidade FROM Produtos WHERE id = ?', (self.produto_id,))
        quantidade = cursor.fetchone()['quantidade']
        if quantidade < self.quantidade:
            return False, 'Quantidade insuficiente'
        cursor.execute('UPDATE Produtos SET quantidade = ? WHERE id = ?', (quantidade - self.quantidade, self.produto_id))
        conn.commit()
        self.salvar()
        conn.close()
        return True, 'Venda realizada com sucesso!'

    def salvar(self):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Vendas (produto_id, quantidade, valor, data) VALUES (?, ?, ?, ?)', (self.produto_id, self.quantidade, self.valor, self.data))
        conn.commit()
        conn.close()


    @staticmethod
    def listar():
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Vendas.id, Produtos.nome, Vendas.quantidade, Vendas.valor, Vendas.data
            FROM Vendas
            JOIN Produtos ON Produtos.id = Vendas.produto_id
        ''')
        vendas_rows = cursor.fetchall()
        vendas = []
        for venda in vendas_rows:
            vendas.append({
                'id': venda['id'],
                'produto': venda['nome'],
                'quantidade': venda['quantidade'],
                'valor': venda['valor'],
                'data': venda['data']
            })
        conn.close()
        return vendas
