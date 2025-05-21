from behave import given, when, then


@given(u'que o cliente está logado')
def step_impl(context):
    context.page.goto(context.base_url)

    username = "fulano1"
    password = "Aa123456"

    # Login
    context.page.click("#hrefUserIcon")
    context.page.fill("input[name='username']", username)
    context.page.fill("input[name='password']", password)
    context.page.click("#sign_in_btn")


@given(u'adiciona um produto no carrinho')
def step_impl(context):
    context.page.click("#tabletsImg")
    context.page.click("div.categoryRight li:nth-child(1)")
    context.page.click("#productProperties button[name='save_to_cart']")


@when(u'realiza o checkout')
def step_impl(context):
    context.page.click("#menuCart")
    context.page.click("#checkOutButton")
    context.page.click("#next_btn")
    #breakpoint()


@when(u'realiza o pagamento com cartão de crédito')
def step_impl(context):
    master_credit_nome = "Fulano da Silva"
    master_credit_numero = "1234 5678 9012"
    master_credit_cvv = "456"
    master_credit_mes = "09"
    master_credit_ano = "2028"
    context.page.get_by_role("img", name="Master credit").click()
    #context.page.get_by_text("Edit", exact=True).click()
    context.page.locator("#creditCard").fill(master_credit_numero)
    context.page.locator("input[name='cvv_number']").fill(master_credit_cvv)
    context.page.locator("select[name='mmListbox']").select_option(f"string:{master_credit_mes}")
    context.page.locator("select[name='yyyyListbox']").select_option(f"string:{master_credit_ano}")
    context.page.locator("input[name='cardholder_name']").fill(master_credit_nome)
    context.page.locator("#pay_now_btn_ManualPayment").click()


@when(u'realiza o pagamento com SafePay')
def step_impl(context):
    safepay_username = "12345"
    safepay_password = "Aa123456"
    context.page.get_by_role("img", name="Safepay").click()
    context.page.fill("input[name='safepay_username']", safepay_username)
    context.page.fill("input[name='safepay_password']", safepay_password)
    #context.page.get_by_role("checkbox", name="save_safepay").check()
    context.page.click("#pay_now_btn_SAFEPAY")


@then(u'a compra é finalizada com sucesso')
def step_impl(context):
    titulo_order_payment = context.page.locator("xpath=/html/body/div[3]/section/article/h3")
    assert "ORDER PAYMENT" in titulo_order_payment.inner_text()

    mensagem_thank_you = context.page.locator("xpath=//*[@id='orderPaymentSuccess']/h2/span")
    assert "Thank you for buying with Advantage" in mensagem_thank_you.inner_text()

    metodo_pagamento = context.page.locator("xpath=//*[@id='orderPaymentSuccess']/div/div[2]/div[1]/label")
    #assert "SafePay" in metodo_pagamento.inner_text()
