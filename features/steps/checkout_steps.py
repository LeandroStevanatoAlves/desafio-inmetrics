from behave import given, when, then
from playwright.sync_api import expect


@given(u'que o cliente está logado')
def step_impl(context):
    context.page.click("#hrefUserIcon")
    context.page.fill("input[name='username']", context.usuario_user_valido.get_loginname())
    context.page.fill("input[name='password']", context.usuario_user_valido.senha)
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


@when(u'realiza o pagamento com MasterCredit')
def step_impl(context):
    context.page.get_by_role("img", name="Master credit").click()
    context.page.locator("#pay_now_btn_MasterCredit").click()


@when(u'realiza o pagamento com SafePay')
def step_impl(context):
    safepay_username = "12345"
    safepay_password = "Aa123456"
    context.page.get_by_role("img", name="Safepay").click()
    context.page.fill("input[name='safepay_username']", safepay_username)
    context.page.fill("input[name='safepay_password']", safepay_password)
    context.page.click("#pay_now_btn_SAFEPAY")


@then(u'a compra é finalizada com sucesso')
def step_impl(context):
    expect(context.page).to_have_url(f"{context.base_url}/orderPayment")

    titulo_order_payment = context.page.locator("xpath=/html/body/div[3]/section/article/h3")
    assert "ORDER PAYMENT" in titulo_order_payment.inner_text()

    mensagem_thank_you = context.page.locator("xpath=//*[@id='orderPaymentSuccess']/h2/span")
    assert "Thank you for buying with Advantage" in mensagem_thank_you.inner_text()