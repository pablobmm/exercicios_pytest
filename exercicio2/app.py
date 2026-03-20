from typing import Optional, Protocol

class IRepositorioUsuarios(Protocol):
    def adicionar_usuario(self, nome: str) -> None:
        ...
    def buscar_usuario(self, nome: str) -> Optional[str]:
        ...

class RepositorioUsuariosFake:
    def __init__(self):
        self._usuarios = []

    def adicionar_usuario(self, nome: str) -> None:
        self._usuarios.append(nome)

    def buscar_usuario(self, nome: str) -> Optional[str]:
        if nome in self._usuarios:
            return nome
        return None

class GerenciadorUsuarios:
    def __init__(self, repositorio: IRepositorioUsuarios):
        self.repositorio = repositorio

    def registrar_usuario(self, nome: str):
        self.repositorio.adicionar_usuario(nome)

    def encontrar_usuario(self, nome: str) -> Optional[str]:
        return self.repositorio.buscar_usuario(nome)