import streamlit as st
import pandas as pd
from st_pages import add_page_title
from produtos.produto import Produto

add_page_title()

def interface_listar():
    produtos = Produto.listar()
    if not produtos:
        st.error("Nenhum produto cadastrado!")
        return

    df_produtos = pd.DataFrame([produto for produto in produtos])
    html = df_produtos.to_html(index=False)
    st.markdown(html, unsafe_allow_html=True)

interface_listar()
