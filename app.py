import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

add_page_title()
show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Section("Produtos", icon="🛍️"),
            Page("produtos/listar.py", "Listar", "📋"),
            Page("produtos/buscar.py", "Buscar", "🔍"),
            Page("produtos/adicionar.py", "Adicionar", "➕"),
            Page("produtos/atualizar.py", "Atualizar", "🔄"),
            Page("produtos/remover.py", "Remover", "❌"),
    ]
)

st.markdown('---')
st.markdown('''
# Sobre
Aplicação web desenvolvida para Controle de Estoque de Supermercado

## Funcionalidades
- Listar produtos
- Adicionar produtos
- Atualizar produtos
- Remover produtos

## Objetivo
Supermercados precisam gerenciar seus estoques, controlando produtos, fornecedores e categorias
de produtos, além de registrar as vendas diárias.

## Tecnologias
- Python
- Streamlit

## Desenvolvedor
- [Paulo](https://github.com/hreis1)
''')
