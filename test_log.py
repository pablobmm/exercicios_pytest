import pytest
import os

@pytest.fixture
def log_file():
    arquivo = "test_log.txt"
    f = open(arquivo, "w")
    
    yield f 
    
    f.close()
    if os.path.exists(arquivo):
        os.remove(arquivo)

def test_escrita_log(log_file):
    log_file.write("Teste de log")
    assert not log_file.closed
    assert log_file.name == "test_log.txt"