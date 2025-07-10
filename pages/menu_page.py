from playwright.sync_api import Page, expect


class MenuPage:
    def __init__(self, page: Page):
        self.shopping_cart_icon = page.locator("#shoppingCartLink")
        self.user_icon = page.locator("#hrefUserIcon")

    def open_login_modal(self):
        self.user_icon.click()
        #expect(self.username_input).to_be_visible()

    def open_cart_modal(self):
        self.shopping_cart_icon.click()

    #def login(self, username: str, password: str):
    #    self.open_login_modal()
    #    self.username_input.fill(username)
    #    self.password_input.fill(password)
    #    self.sign_in_button.click()