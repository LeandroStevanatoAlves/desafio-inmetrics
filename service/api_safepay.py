import time

import requests
from constants import API_SAFEPAY
from utils.logger import log_api

# API SafePay
class ApiSafePay:
    @staticmethod
    def health_check():
        endpoint = f"{API_SAFEPAY}/healthcheck"

        payload = {}
        headers = {}

        tempo_inicial = time.time()
        response = requests.get(endpoint, json=payload, headers=headers)
        response_data = response.json()
        tempo_total = time.time() - tempo_inicial

        # Log
        log_api(
            "Fazendo o Health Check em SafePay",
            tempo_total,
            endpoint,
            headers,
            payload,
            response
        )

        response.raise_for_status()
        if response_data != "Success":
            raise Exception(f"Erro no health check: {response_data}")
