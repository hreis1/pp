import streamlit as st
from st_pages import add_page_title
from produtos.produto import Produto
from vendas.venda import Vendas

add_page_title()

def interface_adicionar():
    produtos = Produto.listar()
    if not produtos:
        st.error("Cadastre um produto antes de adicionar uma venda!")
        return

    opcoes_produto = [(produto['id'],f"{produto['nome']} | Preço: {produto['preco']} R$ | Estoque: {produto['quantidade']}") for produto in produtos]
    produto_selecionado = st.selectbox("Produto", opcoes_produto, format_func=lambda x: x[1])

    quantidade = st.number_input("Quantidade", min_value=1, value=1)
    valor = st.number_input("Valor", min_value=0.01, value=0.01, step=0.01)
    data = st.date_input("Data", format="DD/MM/YYYY")

    produto_id = produto_selecionado[0]

    if st.button("Adicionar"):
        venda, mensagem = Vendas(None, produto_id, quantidade, valor, data).vender()
        if venda:
            st.success(mensagem)
        else:
            st.error(mensagem)

interface_adicionar()
