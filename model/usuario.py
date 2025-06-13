import base64

from unidecode import unidecode

class Usuario:
    def __init__(self, primeiro_nome: str, ultimo_nome: str, senha: str, tipo: str, endereco: str, cidade: str, estado: str, cep: str, telefone: str, user_id: int):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.senha = senha
        self.tipo = tipo
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.user_id = user_id

    def get_email(self):
        email_primeiro_nome = unidecode(self.primeiro_nome).replace(" ","").lower()
        email_ultimo_nome = unidecode(self.ultimo_nome).replace(" ","").lower()
        return f"{email_primeiro_nome}{email_ultimo_nome}@test.com"

    def get_loginname(self):
        login_name_primeiro_nome = unidecode(self.primeiro_nome).replace(" ", "").lower()
        login_name_ultimo_nome = unidecode(self.ultimo_nome).replace(" ", "").lower()
        login_name = f"{login_name_primeiro_nome}{login_name_ultimo_nome}"
        # A documentação da API não especifica, mas o tamanho máximo do loginname é 15.
        # Se usa uma string maior a API retorna erro 403.
        return login_name[: 15]

    def get_base64_token(self):
        # O base64 token é utilizado ao adicionar um Master Credit a um usuário
        encoded = base64.b64encode(f"{self.get_loginname()}:{self.senha}".encode("utf-8"))
        return encoded.decode("utf-8")
