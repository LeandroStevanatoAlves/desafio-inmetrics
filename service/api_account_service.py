import time

import requests

from model.cartao import Cartao
from model.usuario import Usuario
from factory.cartao_factory import CardFactory
from constants import API_ACCOUNT_BASE_URL
from utils.logger import log_api

# API Account Service
class ApiAccountService:
    @staticmethod
    def create_user(user: Usuario) -> int:
        endpoint = f"{API_ACCOUNT_BASE_URL}/register"
        payload = {
            "accountType": user.tipo,
            "address": user.endereco,
            "allowOffersPromotion": True,
            "aobUser": True,
            "cityName": user.cidade,
            "country": "BRAZIL_BR",
            "email": user.get_email(),
            "firstName": user.primeiro_nome,
            "lastName": user.ultimo_nome,
            "loginName": user.get_loginname(),
            "password": user.senha,
            "phoneNumber": user.telefone,
            "stateProvince": user.estado,
            "zipcode": user.cep
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
            f"Creating user {user.tipo}",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if not response_data["response"]["success"]:
            raise Exception(f"Error creating user: {response_data}")

        user_id = response_data["response"]["userId"]
        print(f"User created with userId: {user_id}\n")
        return user_id

    @staticmethod
    def login(usuario: Usuario) -> str:
        endpoint = f"{API_ACCOUNT_BASE_URL}/login"

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
            f"Login with user {usuario.tipo}",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if not response_data["statusMessage"]["success"]:
            raise Exception(f"Login error: {response_data}")

        token = response_data["statusMessage"]["token"]
        print(f"User logged in and received the Token: {token}\n")
        return token

    @staticmethod
    def delete_user(user: Usuario, token: str):
        endpoint = f"{API_ACCOUNT_BASE_URL}/delete"

        payload = {
            "accountId": user.user_id
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
            f"Deleting user with AccountId {user.user_id}",
            tempo_total,
            endpoint,
            headers, payload,
            response
        )

        response.raise_for_status()
        if not response_data["statusMessage"]["success"]:
            raise Exception(f"Error deleting user: {response_data}\n")

    @staticmethod
    def add_master_credit(user: Usuario, token: str, credit_card: Cartao):
        endpoint = f"{API_ACCOUNT_BASE_URL}/addMasterCredit"

        payload = {
            "accountId": user.user_id,
            "base64Token": user.get_base64_token(),
            "cardNumber": credit_card.card_number,
            "customerName": credit_card.customer_name,
            "cvvNumber": credit_card.cvv,
            "expirationDate": credit_card.expiration_date
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
            f"Adding Master Credit to User with AccountId {user.user_id}",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if not response_data["response"]["success"]:
            raise Exception(f"Login error: {response_data}")

    @staticmethod
    def health_check():
        endpoint = f"{API_ACCOUNT_BASE_URL}/health-check"

        payload = {}
        headers = {}

        tempo_inicial = time.time()
        response = requests.get(endpoint, json=payload, headers=headers)
        response_data = response.json()
        tempo_total = time.time() - tempo_inicial

        # Log
        log_api(
            "Performing the Health Check in Account Service",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if response_data != "Success":
            raise Exception(f"Health check error: {response_data}")
