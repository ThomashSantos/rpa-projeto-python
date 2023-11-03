from fonte.modulos.funcao.funcao_core import CoreFuncao


if __name__ == "__main__":
    for proposta in ['12345678', '987654321', '111111111']:
        core = CoreFuncao(proposta)
        core.tratativa_proposta()
