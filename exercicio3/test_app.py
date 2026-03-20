from unittest.mock import call
from .app import ProcessadorDeAcoes

def test_deve_validar_e_salvar_na_ordem_correta(mocker):
    dados = {"id": 123, "valor": 50.0}
    
    mock_processador = mocker.Mock(spec=ProcessadorDeAcoes)
    mock_processador.validar_dados.return_value = True
    mock_processador.salvar_dados.return_value = True

    resultado = ProcessadorDeAcoes.executar_processo(mock_processador, dados)

    roteiro_esperado = [
        call.validar_dados(dados),
        call.salvar_dados(dados)
    ]

    mock_processador.assert_has_calls(roteiro_esperado, any_order=False)
    
    assert resultado == "Sucesso"