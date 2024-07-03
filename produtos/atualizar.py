import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto

add_page_title()

def interface_atualizar():
    id = st.text_input("ID")
    nome = st.text_input("Nome")
    preco = st.number_input("Preço", min_value=0.01, value=0.01, step=0.01)
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=1, value=1)
    categoria = st.text_input("Categoria")

    if st.button("Atualizar"):
        Produto.atualizar_produto(id, nome, preco, descricao, quantidade, categoria)
        st.success("Produto atualizado com sucesso!")

interface_atualizar()
