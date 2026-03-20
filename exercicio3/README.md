# Exercício 3: Processador de Ações (Mock Simplificado)

## Contexto

Você tem um processador de ações que precisa executar duas etapas em uma ordem muito específica: primeiro, `validar_dados` e, em seguida, `salvar_dados`. A ordem é crucial para evitar salvar dados inválidos. Para garantir que essa sequência de chamadas seja rigorosamente seguida, você utilizará **Mocks**.

## Objetivo

Testar uma função `executar_processo` para garantir que as funções `validar_dados` e `salvar_dados` sejam chamadas na ordem correta e com os parâmetros esperados.

## Estrutura do Projeto

```
exercicio3/
├── app.py
└── test_app.py
```

## Tarefas

1.  **No arquivo `app.py`:**
    *   Crie uma classe `ProcessadorDeAcoes`.
    *   Dentro dela, crie dois métodos: `validar_dados(dados: dict) -> bool` e `salvar_dados(dados: dict) -> bool`. Ambos devem apenas simular a operação, retornando `True`.
    *   Crie um método `executar_processo(dados: dict)` que chama `validar_dados` e, se for bem-sucedido, chama `salvar_dados`. Ele deve retornar uma mensagem de sucesso ou falha.

2.  **No arquivo `test_app.py`:**
    *   Utilize `pytest` e `mocker` (do `pytest-mock`) para criar um Mock da classe `ProcessadorDeAcoes`.
    *   Crie um teste que chame `executar_processo` com o Mock.
    *   Use `mock_objeto.assert_has_calls(roteiro_esperado, any_order=False)` para verificar a ordem exata das chamadas e os parâmetros passados para os métodos do Mock.
    *   Verifique se a função `executar_processo` retorna a mensagem de sucesso esperada.

## Dicas

*   Lembre-se de importar `call` de `unittest.mock` para construir o `roteiro_esperado`.
*   O foco principal deste exercício é a **verificação da ordem das interações** e dos **parâmetros** passados, que é a principal força dos Mocks.
