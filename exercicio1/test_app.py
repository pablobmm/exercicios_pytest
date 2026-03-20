from .app import processar_envio

def test_processar_envio_deve_chamar_funcao_externa_corretamente(mocker):
    destinatario_teste = "user@example.com"
    texto_teste = "Olá, mundo!"
    retorno_esperado = "Stub: Envio bem-sucedido"
    mock_envio = mocker.patch('exercicio1.app.enviar_mensagem_externa')
    mock_envio.return_value = retorno_esperado
    resultado = processar_envio(destinatario_teste, texto_teste)
    mock_envio.assert_called_once_with(destinatario_teste, texto_teste)
    assert resultado == retorno_esperado