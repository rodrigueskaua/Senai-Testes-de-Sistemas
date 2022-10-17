from Destino import Destino
from DestinoRepository import DestinoRepository
from UserInterface import UserInterface


destino_repository = DestinoRepository()
destino_repository.adicionar_destino(Destino("61", "Brasilia"))
destino_repository.adicionar_destino(Destino("71", "Salvador"))
destino_repository.adicionar_destino(Destino("11", "São Paulo"))
destino_repository.adicionar_destino(Destino("21", "Rio de Janeiro"))
destino_repository.adicionar_destino(Destino("32", "Juiz de Fora"))
destino_repository.adicionar_destino(Destino("19", "Campinas"))
destino_repository.adicionar_destino(Destino("27", "Vitoria"))
destino_repository.adicionar_destino(Destino("31", "Belo Horizonte"))


user_interface = UserInterface(destino_repository)
while user_interface.obter_interacao():
    pass
