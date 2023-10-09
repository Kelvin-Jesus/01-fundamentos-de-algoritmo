from dataclasses import dataclass
from typing import Dict


@dataclass
class Pedido:
    quantidade: int
    produto: str

@dataclass
class Totalizacao:
    total: int
    produtos: Dict[str, int]

def totaliza_pedidos(pedidos: list[Pedido]) -> Totalizacao:
    '''
    Produz uma estrutura que totaliza a demanda de cada produto
    a partir de *pedidos*.
    >>> totaliza_pedidos([
    ...     Pedido(produto='Bobina', quantidade=100),
    ...     Pedido(produto='Chapa', quantidade=50),
    ...     Pedido(produto='Bobina', quantidade=30),
    ...     Pedido(produto='Painel', quantidade=20),
    ...     Pedido(produto='Chapa', quantidade=15),
    ...     Pedido(produto='Bobina', quantidade=17),
    ... ])
    Totalizacao(total=232, produtos={'Bobina': 147, 'Chapa': 65, 'Painel': 20})

    '''
    total = 0
    produtos = {}

    for pedido in pedidos:
        total += pedido.quantidade
        produtos[pedido.produto] = produtos.get(pedido.produto, 0) + pedido.quantidade
    
    return Totalizacao(total, produtos)


@dataclass
class TipoProduto:
    nome: str
    quantidade: int

def ha_ruptura(estoque: Totalizacao, demanda: Totalizacao) -> list[TipoProduto]:
    '''
    Gera a partir do *estoque* e *demanda*, uma lista com os tipos de produtos
     com ruptura do estoque.
    >>> ha_ruptura(
    ...    estoque=Totalizacao(
    ...         total=100, 
    ...         produtos={'Bobina': 50, 'Chapa': 30, 'Painel': 20}
    ...     ),
    ...     demanda=Totalizacao(
    ...         total=232,
    ...         produtos={'Bobina': 147, 'Chapa': 65, 'Painel': 20}
    ...     )
    ... )
    [TipoProduto(nome='Bobina', quantidade=147), TipoProduto(nome='Chapa', quantidade=65)]
    '''
    ruptura = []
    for produto, quantidade in demanda.produtos.items():
        if quantidade > estoque.produtos.get(produto, 0):
            ruptura.append(TipoProduto(produto, quantidade))

    return ruptura

@dataclass
class NotaDeVenda:
    vendedor: str
    produto: str
    quantidade: int
    valor: float

@dataclass
class Produto:
    nome: str
    quantidade: int
    custo: float
    preco: float

def receita_e_lucro(vendas: list[NotaDeVenda]) -> list:
    '''
    Produz a receita e o lucro líquido a partir de *vendas*, *estoque*, *custo* e *preco*.
    >>> papel = Produto(nome='Papel', quantidade=100000, custo=50.00, preco=60.00)
    >>> papelao = Produto(nome='Papelão', quantidade=50000, custo=40.00, preco=48.00)
    >>> painel = Produto(nome='Painel', quantidade=30000, custo=75.00, preco=90.00)

    >>> receita_e_lucro(
    ...     vendas=[
    ...         NotaDeVenda(vendedor='João', produto=papel, quantidade=180, valor=52.00),
    ...         NotaDeVenda(vendedor='João', produto=papelao, quantidade=346, valor=42.00),
    ...         NotaDeVenda(vendedor='João', produto=painel, quantidade=673, valor=80.00),
    ...         NotaDeVenda(vendedor='Maria', produto=papel, quantidade=234, valor=52.00),
    ...         NotaDeVenda(vendedor='Maria', produto=papelao, quantidade=63, valor=42.00),
    ...         NotaDeVenda(vendedor='Maria', produto=painel, quantidade=235, valor=80.00),
    ...         NotaDeVenda(vendedor='José', produto=papel, quantidade=462, valor=52.00),
    ...         NotaDeVenda(vendedor='José', produto=papelao, quantidade=324, valor=42.00),
    ...         NotaDeVenda(vendedor='José', produto=painel, quantidade=123, valor=80.00),
    ...     ],
    ... )
    (158818.0, 8373.0)

    '''
    receita = 0
    lucro = 0

    for venda in vendas:
        receita += venda.quantidade * venda.valor
        lucro += venda.quantidade * (venda.valor - venda.produto.custo)
        
    return (receita, lucro)