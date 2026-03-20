import pytest
from .app import GerenciadorUsuarios, RepositorioUsuariosFake

@pytest.fixture
def gerenciador():
    repo_fake = RepositorioUsuariosFake()
    return GerenciadorUsuarios(repo_fake)

def test_deve_registrar_e_encontrar_usuario(gerenciador):
    gerenciador.registrar_usuario("Alice")
    resultado = gerenciador.encontrar_usuario("Alice")

    assert resultado == "Alice"

def test_deve_retornar_none_quando_usuario_nao_existe(gerenciador):
    resultado = gerenciador.encontrar_usuario("Bob")

    assert resultado is None