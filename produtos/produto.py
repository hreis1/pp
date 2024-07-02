import json
import os

json_file_path = 'produtos/produtos.json'

class Produto:
    def __init__(self, id, nome, preco, descricao, quantidade, categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade
        self.categoria = categoria
    
    def adicionar_produto(self):
        produtos = Produto.carregar_produtos()
        produtos.append({'id': self.id, 'nome': self.nome, 'preco': self.preco, 'descricao': self.descricao, 'quantidade': self.quantidade, 'categoria': self.categoria})
        Produto.salvar_produtos(produtos)

    def atualizar_produto(id, nome, preco, descricao, quantidade, categoria):
        produtos = Produto.carregar_produtos()
        for produto in produtos:
            if produto['id'] == id:
                produto['nome'] = nome
                produto['preco'] = preco
                produto['descricao'] = descricao
                produto['quantidade'] = quantidade
                produto['categoria'] = categoria
                break
        Produto.salvar_produtos(produtos)

    def remover_produto(id):
        produtos = Produto.carregar_produtos()
        produtos = [produto for produto in produtos if produto['id'] != id]
        Produto.salvar_produtos(produtos)

    def carregar_produtos():
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def buscar_produto(id):
        produtos = Produto.carregar_produtos()
        for produto in produtos:
            if produto['id'] == id:
                return produto
        return None

    def salvar_produtos(produtos):
        with open(json_file_path, 'w') as file:
            json.dump(produtos, file)
