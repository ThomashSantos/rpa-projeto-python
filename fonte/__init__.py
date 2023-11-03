import logging
from datetime import datetime
from fonte.utils.constants import *
from fonte.modulos.funcao.ws_autorizador import WsAutorizador

hoje = datetime.today()
data_formatada = hoje.strftime("%d/%m/%Y")
