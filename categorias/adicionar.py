import streamlit as st
from st_pages import add_page_title
from categorias.categoria import Categoria

add_page_title()

def interface_adicionar():
    nome = st.text_input("Nome")
    if st.button("Adicionar"):
        Categoria(id=None, nome=nome).salvar()
        st.success("Categoria adicionada com sucesso!")

interface_adicionar()
