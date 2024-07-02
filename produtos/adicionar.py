import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto

add_page_title()

def interface_adicionar():
    id = st.text_input("ID")
    nome = st.text_input("Nome")
    preco = st.text_input("Preço")
    descricao = st.text_input("Descrição")
    quantidade = st.text_input("Quantidade")
    categoria = st.text_input("Categoria")
    
    if st.button("Adicionar"):
        Produto(id, nome, preco, descricao, quantidade, categoria).adicionar_produto()
        st.success("Produto adicionado com sucesso!")

interface_adicionar()