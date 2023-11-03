import fonte.utils.constants as const
import requests


class WsAutorizador:
    def __init__(self, proposta: str) -> None:
        self._headers = {
            'Content-Type': 'application/json'
        }
        self._proposta = proposta

    def _gerar_token(self):
        token = const.TOKEN
        return token

    def consulta_proposta(self):
        payload = f""""
        xml>> token: {self._gerar_token()}
        proposta: {self._proposta}
        nome: Thomas dos Santos
        idade: 26
        cidade: Curitiba
        """
        print(payload)
        print('Proposta consultada com sucesso')

    def reprovar_proposta(self):
        print(f'Proposta: {self._proposta} reprovada com sucesso')
