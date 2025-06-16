import time

import requests
from model.usuario import Usuario
from factory.cartao_factory import CartaoFactory
from environment import API_BASE_URL
from utils.logger import log_api

# API Account Service
class ApiAccountService:
    @staticmethod
    def criar_usuario(usuario: Usuario) -> int:
        endpoint = f"{API_BASE_URL}/register"
        payload = {
            "accountType": usuario.tipo,
            "address": usuario.endereco,
            "allowOffersPromotion": True,
            "aobUser": True,
            "cityName": usuario.cidade,
            "country": "BRAZIL_BR",
            "email": usuario.get_email(),
            "firstName": usuario.primeiro_nome,
            "lastName": usuario.ultimo_nome,
            "loginName": usuario.get_loginname(),
            "password": usuario.senha,
            "phoneNumber": usuario.telefone,
            "stateProvince": usuario.estado,
            "zipcode": usuario.cep
        }

        headers = {
            "accept": "*/*",
            "Content-Type": "application/json"
        }

        tempo_inicial = time.time()
        response = requests.post(endpoint, json=payload, headers=headers)
        response_data = response.json()
        tempo_total = time.time() - tempo_inicial

        log_api(
            f"Criando usuário {usuario.tipo}",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if not response_data["response"]["success"]:
            raise Exception(f"Erro na criação de usuário: {response_data}")

        user_id = response_data["response"]["userId"]
        print(f"Usuário criado com o userId: {user_id}\n")
        return user_id

    @staticmethod
    def login(usuario: Usuario) -> str:
        endpoint = f"{API_BASE_URL}/login"

        payload = {
            "email": usuario.get_email(),
            "loginPassword": usuario.senha,
            "loginUser": usuario.get_loginname()
        }

        headers = {
            "Content-Type": "application/json"
        }

        tempo_inicial = time.time()
        response = requests.post(endpoint, json=payload, headers=headers)
        response_data = response.json()
        tempo_total = time.time() - tempo_inicial

        log_api(
            f"Login usuário {usuario.tipo}",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if not response_data["statusMessage"]["success"]:
            raise Exception(f"Erro no login: {response_data}")

        token = response_data["statusMessage"]["token"]
        print(f"Usuário efetuou Login e recebeu o Token: {token}\n")
        return token

    @staticmethod
    def apagar_usuario(usuario: Usuario, token: str):
        endpoint = f"{API_BASE_URL}/delete"

        payload = {
            "accountId": usuario.user_id
        }
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        tempo_inicial = time.time()
        response = requests.delete(endpoint, json=payload, headers=headers)
        response_data = response.json()
        tempo_total = time.time() - tempo_inicial

        log_api(
            f"Apagando usuário com AccountId {usuario.user_id}",
            tempo_total,
            endpoint,
            headers, payload,
            response
        )

        response.raise_for_status()
        if not response_data["statusMessage"]["success"]:
            raise Exception(f"Erro ao apagar o usuário: {response_data}\n")

    @staticmethod
    def adicionar_master_credit(usuario: Usuario, token: str):
        endpoint = f"{API_BASE_URL}/addMasterCredit"

        cartao = CartaoFactory.criar(usuario)

        payload = {
            "accountId": usuario.user_id,
            "base64Token": usuario.get_base64_token(),
            "cardNumber": cartao.card_number,
            "customerName": cartao.customer_name,
            "cvvNumber": cartao.cvv,
            "expirationDate": cartao.expiration_date
        }

        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        tempo_inicial = time.time()
        response = requests.post(endpoint, json=payload, headers=headers)
        response_data = response.json()
        tempo_total = time.time() - tempo_inicial

        log_api(
            f"Adicionando Master Credit ao usuário com AccountId {usuario.user_id}",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if not response_data["response"]["success"]:
            raise Exception(f"Erro no login: {response_data}")

    @staticmethod
    def health_check():
        endpoint = f"{API_BASE_URL}/health-check"

        payload = {}
        headers = {}

        tempo_inicial = time.time()
        response = requests.get(endpoint, json=payload, headers=headers)
        response_data = response.json()
        tempo_total = time.time() - tempo_inicial

        # Log
        log_api(
            "Fazendo o Health Check em Account Service",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if response_data != "Success":
            raise Exception(f"Erro no health check: {response_data}")
