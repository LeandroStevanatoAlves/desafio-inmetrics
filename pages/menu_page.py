from playwright.sync_api import Page, expect


class MenuPage:
    def __init__(self, page: Page):
        self.shopping_cart_icon = page.locator("#shoppingCartLink")
        self.user_icon = page.locator("#hrefUserIcon")

    def open_login_modal(self):
        self.user_icon.click()

    def open_cart_modal(self):
        self.shopping_cart_icon.click()