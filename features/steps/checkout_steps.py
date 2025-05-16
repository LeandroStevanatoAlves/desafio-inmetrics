from behave import given, when, then
from playwright.sync_api import sync_playwright


@given(u'que o cliente está logado')
def step_impl(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")


@given(u'adiciona um produto no carrinho')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given adiciona um produto no carrinho')


@when(u'realiza o checkout')
def step_impl(context):
    raise NotImplementedError(u'STEP: When realiza o checkout')


@when(u'realiza o pagamento com cartão de crédito')
def step_impl(context):
    raise NotImplementedError(u'STEP: When realiza o pagamento com cartão de crédito')


@then(u'a compra é finalizada com sucesso')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a compra é finalizada com sucesso')


@when(u'realiza o pagamento com SafePay')
def step_impl(context):
    raise NotImplementedError(u'STEP: When realiza o pagamento com SafePay')