from UserInterface import UserInterface
from DestinoRepository import DestinoRepository
from Destino import Destino

def test_solicitar_input_usuario(monkeypatch):
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    user_interface = UserInterface(destino_repository)
    destino_cadastrado = Destino("75", "Feira de Santana")
    monkeypatch.setattr('builtins.input', lambda _: "75")

    # Act
    destino_repository.adicionar_destino(destino_cadastrado)    
    input_result = user_interface.solicitar_input_usuario()

    # Assert
    assert input_result.DDD == "75"
    assert user_interface.obter_destino_pelo_ddd(input_result) == "Feira de Santana"

def test_obter_destino_pelo_ddd():
    #Assert
    destino_repository = DestinoRepository()
    user_interface = UserInterface(destino_repository)
    destino_repository.lista_destino = []
    destino_cadastrado = Destino("71", "Salvador")
    ddd = Destino("71")

    # Act
    destino_repository.adicionar_destino(destino_cadastrado)

    # Assert
    assert user_interface.obter_destino_pelo_ddd(ddd) == "Salvador"

def test_obter_interacao(monkeypatch):
    # Arrange
    monkeypatch.setattr('builtins.input', lambda _: "71")
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    user_interface = UserInterface(destino_repository)
    destino_cadastrado = Destino("71", "Salvador")

    # Act
    destino_repository.adicionar_destino(destino_cadastrado)    
    resultOK = user_interface.obter_interacao()
  
    # Assert
    assert resultOK == True

