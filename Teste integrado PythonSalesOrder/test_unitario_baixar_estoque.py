from Entities.Produto import Produto

def test_baixar_estoque():
    # Arrange
    produto = Produto(3, "Rice", 10.23, 9)

    # Act
    produto.baixar_estoque(3)

    # Assert
    assert produto.estoque == 6