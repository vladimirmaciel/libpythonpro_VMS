import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session') #utilizar este decorate
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()  #se o objeto ficar com mesmo nome da funcao da  problema
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()