import pandas as pd
import streamlit as st
from st_pages import add_page_title
from vendas.venda import Vendas

add_page_title()

def interface_listar():
    vendas = Vendas.listar()
    if not vendas:
        st.error("Nenhuma venda cadastrada!")
        return

    df_vendas = pd.DataFrame([venda for venda in vendas])
    html = df_vendas.to_html(index=False)
    st.markdown(html, unsafe_allow_html=True)

interface_listar()
