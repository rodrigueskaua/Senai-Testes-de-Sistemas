from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository
from datetime import datetime

def test_integracao_baixar_estoque():
    # Arrange
    cliente = Cliente(1,"Kaua")
    customer_repository = ClienteRepository()
    customer_repository.adicionar_cliente(cliente)

    produto = Produto(1, "Rice", 10.23, 9)
    product_repository = ProdutoRepository()
    product_repository.adicionar_produto(produto)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()

    # Act
    pedido_produto.adicionar_produto(produto,3)
    pedido.adicionar_produto_pedido(pedido_produto)
    
    # Assert
    assert produto.estoque == 6

