from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository
from datetime import datetime

def test_integracao_processar_produto():
    # Arrange
    cliente = Cliente(1,"Kaua")
    customer_repository = ClienteRepository()
    customer_repository.adicionar_cliente(cliente)

    produto = Produto(1, "Rice", 10.23, 9)
    product_repository = ProdutoRepository()
    product_repository.adicionar_produto(produto)

    pedido_produto = PedidoProduto()
    pedido = Pedido(1, cliente, datetime.today)
    pedido.adicionar_produto_pedido(pedido_produto)

    # Act
    pedido_produto.processar_pedido(produto, 3)

    # Assert
    assert pedido_produto.quantidade == 3
    assert pedido_produto.valor_item == 30.69
