from Destino import Destino

class DestinoRepository:
    lista_destino: Destino = []

    def __init__(self) -> None:
        pass

    def adicionar_destino(self, destino):
        self.lista_destino.append(destino)

    def checa_se_destino_existe(self, destino: Destino) -> bool:
            for item in self.lista_destino:
                if (destino.DDD == item.DDD):
                    return True

            return False

    def obter_destino_pelo_ddd(self, destino: Destino) -> str:
        for item in self.lista_destino:
            if (destino.DDD == item.DDD):
                return item.Destino


