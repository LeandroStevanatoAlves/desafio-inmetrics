from faker import Faker
from model.usuario import Usuario

fake = Faker("pt_BR")

class UsuarioFactory:
    @staticmethod
    def criar_usuario() -> Usuario:
        return UsuarioFactory.__criar("USER")

    @staticmethod
    def criar_admin() -> Usuario:
        return UsuarioFactory.__criar("ADMIN")

    @staticmethod
    def __criar(tipo: str) -> Usuario:
        return Usuario(
            fake.first_name(),
            fake.last_name(),
            "Aa123456",
            tipo,
            fake.street_address(),
            fake.city(),
            fake.estado_sigla(),
            fake.postcode(),
            fake.phone_number(),
            0
        )
