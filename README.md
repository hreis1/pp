### Tabela: Categorias
- `id` (PK): Identificador único da categoria
- `nome` (TEXT): Nome da categoria

### Tabela: Produtos
- `id` (PK): Identificador único do produto
- `nome` (TEXT): Nome do produto
- `preco` (REAL): Preço do produto
- `descricao` (TEXT): Descrição do produto
- `quantidade` (INTEGER): Quantidade em estoque
- `categoria_id` (FK): Identificador da categoria do produto

### Tabela: Vendas
- `id` (PK): Identificador único da venda
- `quantidade` (INTEGER): Quantidade vendida
- `valor` (REAL): Valor total da venda
- `data` (TEXT): Data da venda
- `produto_id` (FK): Identificador do produto vendido

### Relacionamentos

- Um produto pertence a uma categoria
- Um produto pode ser vendido várias vezes

### Requisitos

- python3
- sqlite3
- pip3
- streamlit
- stpages

### Instalação

```bash
pip install sqlite3 streamlit stpages
```

### Execução

Rodar o comando abaixo para iniciar o banco de dados
```bash
python3 init.py
```

Rodar o comando abaixo para iniciar a aplicação
```bash
streamlit run app.py
```

### Uso

- Acesse o endereço `http://localhost:8501/` no seu navegador

### Autor
- [Paulo Henrique](https://github.com/hreis1)
