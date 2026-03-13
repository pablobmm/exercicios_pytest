def test_conexao_usuario(db_connection):
    assert db_connection == "Conexão Global Estabelecida"
    print("Executando Teste 1")

def test_conexao_admin(db_connection):
    assert "Estabelecida" in db_connection
    print("Executando Teste 2")