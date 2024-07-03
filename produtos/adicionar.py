import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto
from categorias.categoria import Categoria

add_page_title()

def interface_adicionar():
    nome = st.text_input("Nome")
    preco = st.number_input("Preço", min_value=0.01, value=0.01, step=0.01)
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=1, value=1)
    categorias = Categoria.listar()
    if not categorias:
        st.error("Cadastre uma categoria antes de adicionar um produto!")
        return

    opcoes_categoria = [(categoria.id, categoria.nome) for categoria in categorias]
    categoria_id, categoria_nome = st.selectbox("Categoria", opcoes_categoria, format_func=lambda x: x[1])

    if st.button("Adicionar"):
        Produto(id=None, nome=nome, preco=preco, descricao=descricao, quantidade=quantidade, categoria_id=categoria_id).salvar()
        st.success("Produto adicionado com sucesso!")

interface_adicionar()
