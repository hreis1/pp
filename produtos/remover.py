import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto

add_page_title()

def interface_remover():
    id = st.text_input("ID")
    if st.button("Remover"):
        produto = Produto.buscar(id)
        if produto:
            produto.remover()
            st.success("Produto removido com sucesso")
        else:
            st.error("Produto não encontrado")

interface_remover()
