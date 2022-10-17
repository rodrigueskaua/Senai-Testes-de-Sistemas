from Destino import Destino
from DestinoRepository import DestinoRepository


def test_adicionar_destino():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    destino1 = Destino("75", "Feira de Santana")
    destino2 = Destino("85", "Fortaleza")
    destino3 = Destino("79", "Aracaju")
    
    # Act
    destino_repository.adicionar_destino(destino1)
    destino_repository.adicionar_destino(destino2)

    # Assert
    assert not destino3 in destino_repository.lista_destino
    assert len(destino_repository.lista_destino) == 2
    assert type(destino_repository.lista_destino) == list


def test_checa_se_destino_existe():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    destino1 = Destino("75", "Feira de Santana")
    destino2 = Destino("85", "Fortaleza")

    # Act
    destino_repository.adicionar_destino(destino1)
    resultOK = destino_repository.checa_se_destino_existe(destino1)
    resultNOK = destino_repository.checa_se_destino_existe(destino2)

    # Assert
    assert len(destino_repository.lista_destino) == 1
    assert resultOK == True
    assert resultNOK == False


def test_obter_destino_pelo_ddd():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    destino_cadastrado1 = Destino("75", "Feira de Santana")
    ddd_test1 = Destino("75")
    ddd_test2 = Destino("71")

    # Act
    destino_repository.adicionar_destino(destino_cadastrado1)

    # Assert
    assert destino_repository.obter_destino_pelo_ddd(ddd_test1) == "Feira de Santana"
    assert not destino_repository.obter_destino_pelo_ddd(ddd_test2) == "Salvador"


