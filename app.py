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
        Section("Categorias", icon="🏷️"),
            Page("categorias/listar.py", "Listar", "📋"),
            Page("categorias/adicionar.py", "Adicionar", "➕"),
            Page("categorias/remover.py", "Remover", "❌"),
        Section("Vendas", icon="💰"),
            Page("vendas/adicionar.py", "Vender", "💸"),
            Page("vendas/listar.py", "Listar", "📋")
    ]
)

st.markdown('''
# Sobre
Aplicação web desenvolvida para Controle de Estoque de Supermercado

## Funcionalidades
- Listar produtos
- Adicionar produtos
- Atualizar produtos
- Remover produtos
- Listar categorias
- Adicionar categorias
- Remover categorias se não estiver sendo usada
- Vincular um produto a uma categoria
- Vender um produto
- Listar vendas

## Objetivo
Supermercados precisam gerenciar seus estoques, controlando produtos e categorias
de produtos, além de registrar as vendas diárias.

## Tecnologias
- Python
- Streamlit
- Sqlite3

## Desenvolvedor
- [Paulo](https://github.com/hreis1)
''')
