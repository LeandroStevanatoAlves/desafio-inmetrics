from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
from factory.usuario_factory import UsuarioFactory
from service.api_account_service import ApiAccountService
from constants import SITE_BASE_URL


def before_all(context):
    print("before_all")
    # Faz o Health Check da API Account Service
    ApiAccountService.health_check()

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

    context.playwright = sync_playwright().start()

def before_scenario(context, scenario):
    print("before_scenario")
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.base_url = SITE_BASE_URL

def after_scenario(context, scenario):
    print("after_scenario")
    context.browser.close()

def after_all(context):
    # Apaga os usuários
    ApiAccountService.apagar_usuario(context.usuario_user_valido, context.token_admin)
    ApiAccountService.apagar_usuario(context.usuario_admin_valido, context.token_admin)
