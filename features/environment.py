from playwright.sync_api import sync_playwright

from factory.cartao_factory import CardFactory
from factory.safe_pay_factory import SafePayFactory
from factory.usuario_factory import UsuarioFactory
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.product_detail_page import ProductDetailPage
from pages.shipping_details_page import ShippingDetailsPage
from pages.shopping_cart_page import ShoppingCartPage
from service.api_account_service import ApiAccountService
from service.api_mastercredit import ApiMasterCredit
from service.api_order import ApiOrder
from service.api_safepay import ApiSafePay
from constants import SITE_BASE_URL
from utils.logger import log


def before_all(context):
    # Performs Health Check on APIs
    ApiAccountService.health_check()
    ApiMasterCredit.health_check()
    ApiOrder.health_check()
    ApiSafePay.health_check()

    # Creates user of type USER
    context.usuario_user_valido = UsuarioFactory().criar_usuario()
    context.usuario_user_valido.user_id = ApiAccountService.create_user(context.usuario_user_valido)

    # Creates user of type ADMIN
    context.usuario_admin_valido = UsuarioFactory().criar_admin()
    context.usuario_admin_valido.user_id = ApiAccountService.create_user(context.usuario_admin_valido)

    # Master Credit
    master_credit = CardFactory.create(context.usuario_user_valido)

    # Safe Pay
    context.safe_pay = SafePayFactory.create(context.usuario_user_valido)

    # Log in with the Admin User to get the Token
    context.token_admin = ApiAccountService.login(context.usuario_admin_valido)

    # Add a card to the user User
    ApiAccountService.add_master_credit(context.usuario_user_valido, context.token_admin, master_credit)

    log("Starting Playwright")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    log("Creating a new Playwright page")
    context.page = context.browser.new_page()
    context.base_url = SITE_BASE_URL
    context.page.goto(f"{SITE_BASE_URL}/")

    log("Initializing Page Objects")
    context.menu_page = MenuPage(context.page)
    context.login_page = LoginPage(context.page)
    context.home_page = HomePage(context.page)
    context.category_page = CategoryPage(context.page)
    context.product_detail_page = ProductDetailPage(context.page)
    context.shopping_cart_page = ShoppingCartPage(context.page)
    context.shipping_details_page = ShippingDetailsPage(context.page)

def after_scenario(context, scenario):
    log("Closing the Playwright page")
    context.page.close()

def after_all(context):
    log("Finishing Playwright")
    context.browser.close()
    context.playwright.stop()

    # Delete all users that was created in this session
    ApiAccountService.delete_user(context.usuario_user_valido, context.token_admin)
    ApiAccountService.delete_user(context.usuario_admin_valido, context.token_admin)
