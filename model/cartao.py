class Cartao:
    def __init__(self, card_number: str, customer_name: str, cvv: str, expiration_date: str):
        self.card_number = card_number
        self.customer_name = customer_name
        self.cvv = cvv
        self.expiration_date = expiration_date