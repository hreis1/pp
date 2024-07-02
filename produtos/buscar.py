import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto

add_page_title()

def interface_buscar():
    id = st.text_input("ID")
    produto = Produto.buscar_produto(id)
    if produto:
        st.write(f"Nome: {produto['nome']}")
        st.write(f"Preço: {produto['preco']}")
        st.write(f"Descrição: {produto['descricao']}")
        st.write(f"Quantidade: {produto['quantidade']}")
        st.write(f"Categoria: {produto['categoria']}")
    else:
        st.warning("Produto não encontrado!")

interface_buscar()