from model.cartao import Cartao
from model.usuario import Usuario


class CartaoFactory:
    @staticmethod
    def criar(usuario: Usuario) -> Cartao:
        return Cartao(
            "4886123456789012",
            f"{usuario.primeiro_nome} {usuario.ultimo_nome}",
            "567",
            "122032"
        )
