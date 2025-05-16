# language: pt
Funcionalidade: Checkout

  Cenario: Checkout com sucesso usando cartão de crédito
    Dado que o cliente está logado
    E adiciona um produto no carrinho
    Quando realiza o checkout
    E realiza o pagamento com cartão de crédito
    Então a compra é finalizada com sucesso

  Cenario:
    Dado que o cliente está logado
    E adiciona um produto no carrinho
    Quando realiza o checkout
    E realiza o pagamento com SafePay
    Então a compra é finalizada com sucesso