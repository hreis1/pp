import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto

add_page_title()

def interface_buscar():
    input_buscar = st.text_input("ID, Nome ou Descrição")
    if st.button("Buscar"):
        produtos = Produto.busca_por_id_nome_categoria_descricao(input_buscar)
        if produtos:
            for produto in produtos:
                st.write(f"ID: {produto['id']}")
                st.write(f"Nome: {produto['nome']}")
                st.write(f"Preço: {produto['preco']}")
                st.write(f"Descrição: {produto['descricao']}")
                st.write(f"Quantidade: {produto['quantidade']}")
                st.write(f"Categoria: {produto['categoria']}")
                st.write("---")
                
        else:
            st.warning("Produto não encontrado!")

interface_buscar()
