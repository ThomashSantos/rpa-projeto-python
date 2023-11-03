from selenium import webdriver


class WebAutorizador():
    def __init__(self) -> None:
        self._driver = 'driver'

    def login(self):
        print('Login feito com sucesso')

    def validacao_dados(self):
        print('Dados validados com sucesso')
