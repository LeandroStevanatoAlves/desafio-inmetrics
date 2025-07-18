import logging

import requests.models


logging.basicConfig(
    level=logging.INFO,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

def log_message(mensagem: str):
    logging.info(f"==========[ {mensagem} ]==========\n")


def log_api(mensagem: str, tempo_total: float, endpoint: str, request_headers: dict, request_body: dict, response: requests.models.Response):
    logging.info(f"==========[ {mensagem} ]==========")
    logging.info(f"Tempo de execução: {tempo_total:.3f}s")
    logging.info(f"Request URL: {endpoint}")
    logging.info(f"Headers: {request_headers}")
    logging.info(f"Request Body: \n{request_body}")
    logging.info(f"Response Code: {response.status_code}")
    logging.info(f"Response Body: \n{response.json()}\n")
