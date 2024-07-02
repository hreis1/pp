import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto

add_page_title()

def interface_remover():
    id = st.text_input("ID")
    if st.button("Remover"):
        Produto.remover_produto(id)
        st.success("Produto removido com sucesso!")

interface_remover()