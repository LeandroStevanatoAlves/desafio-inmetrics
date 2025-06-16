# language: pt
Funcionalidade: Checkout

  Cenario: Checkout com sucesso usando MasterCredit(cartão de crédito)
    Dado que o cliente está logado
    E adiciona um produto no carrinho
    Quando realiza o checkout
    E realiza o pagamento com MasterCredit
    Então a compra é finalizada com sucesso

  Cenario: Checkout com sucesso usando SafePay
    Dado que o cliente está logado
    E adiciona um produto no carrinho
    Quando realiza o checkout
    E realiza o pagamento com SafePay
    Então a compra é finalizada com sucesso