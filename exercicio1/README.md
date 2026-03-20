# Exercício 1: Sistema de Mensagens (Stub e Spy Simplificado)

## Contexto

Imagine que você tem um módulo simples responsável por enviar mensagens. Para testar a lógica que decide *quando* e *com o que* uma mensagem deve ser enviada, sem realmente disparar um e-mail ou SMS, usaremos **Stubs** e **Spies**.

## Objetivo

Testar uma função que processa o envio de mensagens, garantindo que a função de envio subjacente seja chamada com os parâmetros corretos e que o retorno seja o esperado.

## Estrutura do Projeto

```
exercicio1/
├── app.py
└── test_app.py
```

## Tarefas

1.  **No arquivo `app.py`:**
    *   Crie uma função `enviar_mensagem_externa(destinatario: str, conteudo: str) -> str`. Esta função deve apenas retornar uma string como `"Mensagem enviada para {destinatario}: {conteudo}"`. Pense nela como a dependência externa que não queremos chamar de verdade.
    *   Crie uma função `processar_envio(destinatario: str, texto: str) -> str`. Esta função deve chamar `enviar_mensagem_externa` e retornar o resultado.

2.  **No arquivo `test_app.py`:**
    *   Utilize `pytest` e `mocker` (do `pytest-mock`) para substituir a função `enviar_mensagem_externa` por um Stub/Spy.
    *   Crie um teste para verificar se `enviar_mensagem_externa` é chamada exatamente uma vez com os argumentos corretos (`destinatario` e `conteudo`).
    *   Configure o Stub para retornar um valor fixo e verifique se `processar_envio` retorna esse valor.

## Dicas

*   Use `mocker.patch('app.enviar_mensagem_externa')` para substituir a função.
*   Configure o retorno do seu mock com `mock_funcao.return_value = "..."`.
*   Verifique as chamadas com `mock_funcao.assert_called_once_with(arg1, arg2)`.
