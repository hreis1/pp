import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto
from categorias.categoria import Categoria

add_page_title()

def interface_atualizar():
    id = st.text_input("ID")
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

    if st.button("Atualizar"):
        Produto(id, nome, preco, descricao, quantidade, categoria_id).atualizar()
        st.success("Produto atualizado com sucesso!")

interface_atualizar()
