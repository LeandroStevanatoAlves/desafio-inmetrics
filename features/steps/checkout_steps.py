from behave import given, when, then
from playwright.sync_api import expect


@given(u'que o cliente está logado')
def step_impl(context):
    context.menu_page.open_login_modal()
    context.login_page.login(context.usuario_user_valido.get_loginname(), context.usuario_user_valido.senha)


@given(u'adiciona um produto no carrinho')
def step_impl(context):
    context.home_page.select_tablets_category()
    context.category_page.select_first_product()
    context.product_detail_page.add_to_cart()


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