import sqlite3

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def salvar(self):
      conn = sqlite3.connect('./supermecado.db')
      conn.row_factory = sqlite3.Row
      cursor = conn.cursor()
      cursor.execute('INSERT INTO Categorias (nome) VALUES (?)', (self.nome,))
      conn.commit()

    @staticmethod
    def listar():
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Categorias')
        categorias = cursor.fetchall()
        conn.close()
        return [Categoria(*categoria) for categoria in categorias]
    
    @staticmethod
    def buscar(id):
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Categorias WHERE id = ?', (id,))
        categoria = cursor.fetchone()
        conn.close()
        return Categoria(*categoria) if categoria else None

    def remover(self):
        conn = sqlite3.connect('./supermecado.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM Categorias 
            WHERE id = ? 
            AND NOT EXISTS (
                SELECT 1 FROM Produtos 
                WHERE categoria_id = Categorias.id
            )''', (self.id,))
        if cursor.rowcount == 0:
            return False, "Categoria não pode ser removida porque está sendo usada por um ou mais produtos."
        conn.commit()
        return True, "Categoria removida com sucesso."

    @staticmethod
    def listar():
        conn = sqlite3.connect('./supermecado.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Categorias')
        categorias = cursor.fetchall()
        conn.close()
        return [Categoria(*categoria) for categoria in categorias]
