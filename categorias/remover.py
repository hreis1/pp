import streamlit as st
from st_pages import add_page_title
from categorias.categoria import Categoria

add_page_title()

def interface_remover():
    id = st.text_input("ID")
    if st.button("Remover"):
        categoria = Categoria.buscar(id)
        if categoria:
            sucesso, mensagem = categoria.remover()
            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)
        else:
            st.error("Categoria não encontrada")

interface_remover()
