from DestinoRepository import DestinoRepository
from Destino import Destino

class UserInterface:
    def __init__(self, destino_repository: DestinoRepository) -> None:
        self.destino_repository = destino_repository

    def solicitar_input_usuario(self) -> Destino:
        resultado = input("Informe o DDD (valido): ")
        return Destino(resultado)

    def obter_destino_pelo_ddd(self, destino: Destino) -> str:
        return self.destino_repository.obter_destino_pelo_ddd(destino)

    def obter_interacao(self) -> bool:
        destino = self.solicitar_input_usuario()

        if (self.destino_repository.checa_se_destino_existe(destino) == False):
            print("DDD inválido!")
            return False

        print(f"Destino: {self.obter_destino_pelo_ddd(destino)}")
        return True
