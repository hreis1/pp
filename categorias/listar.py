import streamlit as st
from st_pages import add_page_title
from categorias.categoria import Categoria

add_page_title()

def interface_listar():
    st.write('## Lista de Categorias')
    categorias = Categoria.listar()
    for categoria in categorias:
        st.write(f'**{categoria.id}** - {categoria.nome}')

interface_listar()
