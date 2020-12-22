from libpythonpro.spam.modelos import Usuario


def test_savlar_usuario(sessao):
    usuario = Usuario(nome='Vladimir')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Vladimir'), Usuario(nome='Davi')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

