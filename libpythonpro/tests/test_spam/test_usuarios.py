from libpythonpro.spam.modelos import Usuario


def test_savlar_usuario(sessao):
    usuario = Usuario(nome='Vladimir', email = 'vladimirmaciel@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Vladimir', email='vladimirmaciel@gmail.com'),
        Usuario(nome='Davi', email='daviserra@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

