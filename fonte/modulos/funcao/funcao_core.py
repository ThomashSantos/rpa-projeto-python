from fonte.modulos.funcao.web_autorizador import WebAutorizador
from fonte.modulos.funcao.ws_autorizador import WsAutorizador


class CoreFuncao(WsAutorizador, WebAutorizador):
    def __init__(self, proposta: str = None) -> None:
        super().__init__(proposta=proposta)

    def tratativa_proposta(self):
        self.login() # WEB
        self.consulta_proposta() # API
        self.validacao_dados() # WEB
        self.reprovar_proposta() # API
