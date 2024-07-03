### Tabela: Produtos
- `ProdutoID` (PK): Identificador único do produto
- `Nome` (VARCHAR): Nome do produto
- `CategoriaID` (FK): Identificador da categoria do produto
- `FornecedorID` (FK): Identificador do fornecedor do produto
- `Preco` (DECIMAL): Preço do produto
- `QuantidadeEstoque` (INT): Quantidade disponível em estoque

### Tabela: Categorias
- `CategoriaID` (PK): Identificador único da categoria
- `Nome` (VARCHAR): Nome da categoria

### Tabela: Vendas
- `VendaID` (PK): Identificador único da venda
- `Data` (DATE): Data da venda
- `Total` (DECIMAL): Valor total da venda

### Tabela: ItensVenda
- `ItemVendaID` (PK): Identificador único do item da venda
- `VendaID` (FK): Identificador da venda
- `ProdutoID` (FK): Identificador do produto vendido
- `Quantidade` (INT): Quantidade vendida
- `PrecoVenda` (DECIMAL): Preço do produto na venda

### Diagrama ER (Entidade-Relacionamento)

```plaintext
Produtos
-----------------------------------
ProdutoID (PK)
Nome
CategoriaID (FK)
FornecedorID (FK)
Preco
QuantidadeEstoque

Fornecedores
-----------------------------------
FornecedorID (PK)
Nome
Endereco
Telefone
Email

Categorias
-----------------------------------
CategoriaID (PK)
Nome

Vendas
-----------------------------------
VendaID (PK)
Data
Total

ItensVenda
-----------------------------------
ItemVendaID (PK)
VendaID (FK)
ProdutoID (FK)
Quantidade
PrecoVenda
```

### Relacionamentos
- Um produto pertence a uma categoria (`Produtos.CategoriaID` → `Categorias.CategoriaID`)
- Um produto é fornecido por um fornecedor (`Produtos.FornecedorID` → `Fornecedores.FornecedorID`)
- Uma venda pode ter vários itens de venda (`ItensVenda.VendaID` → `Vendas.VendaID`)
- Cada item de venda é referente a um produto (`ItensVenda.ProdutoID` → `Produtos.ProdutoID`)
