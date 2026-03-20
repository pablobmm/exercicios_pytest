# Exercício 2: Gerenciador de Usuários (Fake Simplificado)

## Contexto

Você está desenvolvendo um módulo simples para gerenciar usuários, onde cada usuário tem apenas um nome. Este módulo precisa interagir com um "repositório" para armazenar e recuperar os nomes dos usuários. Para testar a lógica do gerenciador sem a complexidade de um banco de dados real, você criará uma implementação **Fake** do repositório.

## Objetivo

Testar as operações de adicionar e buscar usuários, utilizando um repositório em memória que simula o comportamento de um banco de dados real, mas de forma simplificada.

## Estrutura do Projeto

```
exercicio2/
├── app.py
└── test_app.py
```

## Tarefas

1.  **No arquivo `app.py`:**
    *   Crie uma interface (ou classe abstrata) `IRepositorioUsuarios` com os métodos `adicionar_usuario(nome: str)` e `buscar_usuario(nome: str) -> Optional[str]`.
    *   Crie uma implementação **Fake** dessa interface, chamada `RepositorioUsuariosFake`. Esta classe deve usar uma lista ou um dicionário Python simples para armazenar os nomes dos usuários em memória.
    *   Crie uma classe `GerenciadorUsuarios` que recebe uma instância de `IRepositorioUsuarios` no seu construtor. Esta classe terá métodos como `registrar_usuario(nome: str)` e `encontrar_usuario(nome: str)` que utilizam o repositório.

2.  **No arquivo `test_app.py`:**
    *   Utilize `pytest` para testar a classe `GerenciadorUsuarios`.
    *   Nos testes, injete uma instância de `RepositorioUsuariosFake` no `GerenciadorUsuarios`.
    *   Crie um teste para adicionar um usuário e verificar se ele pode ser encontrado posteriormente.
    *   Crie um teste para tentar buscar um usuário que não foi adicionado e verificar se o retorno é `None`.

## Dicas

*   A implementação Fake deve ser o mais simples possível, focando apenas em simular o armazenamento e recuperação de nomes.
*   Use fixtures do `pytest` para instanciar o `RepositorioUsuariosFake` e o `GerenciadorUsuarios` em cada teste, garantindo isolamento.
