from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
from factory.usuario_factory import UsuarioFactory
from pages.home_page import HomePage
from service.api_account_service import ApiAccountService
from service.api_mastercredit import ApiMasterCredit
from service.api_order import ApiOrder
from service.api_safepay import ApiSafePay
from constants import SITE_BASE_URL
from utils.logger import log


def before_all(context):
    # Faz o Health Check nas APIs
    ApiAccountService.health_check()
    ApiMasterCredit.health_check()
    ApiOrder.health_check()
    ApiSafePay.health_check()

    # Cria usuário do tipo USER
    context.usuario_user_valido = UsuarioFactory().criar_usuario()
    context.usuario_user_valido.user_id = ApiAccountService.criar_usuario(context.usuario_user_valido)

    # Cria usuário do tipo ADMIN
    context.usuario_admin_valido = UsuarioFactory().criar_admin()
    context.usuario_admin_valido.user_id = ApiAccountService.criar_usuario(context.usuario_admin_valido)

    # Loga com o Usuário Admin para pegar o Token
    context.token_admin = ApiAccountService.login(context.usuario_admin_valido)

    # Adiciona um cartão ao usuário User
    ApiAccountService.adicionar_master_credit(context.usuario_user_valido, context.token_admin)

    log("Starting Playwright")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    log("Creating a new Playwright page")
    context.page = context.browser.new_page()
    context.base_url = SITE_BASE_URL
    context.page.goto(f"{SITE_BASE_URL}/")

def after_scenario(context, scenario):
    log("Closing the Playwright page")
    context.page.close()

def after_all(context):
    log("Finishing Playwright")
    context.browser.close()
    context.playwright.stop()

    # Apaga os usuários
    ApiAccountService.apagar_usuario(context.usuario_user_valido, context.token_admin)
    ApiAccountService.apagar_usuario(context.usuario_admin_valido, context.token_admin)
