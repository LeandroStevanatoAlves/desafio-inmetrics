from playwright.sync_api import Page


class ShoppingCartPage:
    def __init__(self, page: Page):
        self.checkout_button = page.locator("#checkOutButton")

    def proceed_to_checkout(self):
        self.checkout_button.click()
