import requests.models


def log_api(mensagem: str, tempo_total: float, endpoint: str, request_headers: dict, request_body: dict, response: requests.models.Response):
    print(f"==========[ {mensagem} ]==========")
    print(f"Tempo de execução: {tempo_total:.3f}s")
    print(f"Request URL: {endpoint}")
    print(f"Headers: {request_headers}")
    print(f"Request Body: {request_body}")

    print(f"Response Code: {response.status_code}")
    print("Response:")
    print(f"{response.json()}\n")
