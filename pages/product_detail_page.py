from playwright.sync_api import Page


class ProductDetailPage:
    def __init__(self, page: Page):
        self.add_to_cart_button = page.locator("#productProperties button[name='save_to_cart']")

    def add_to_cart(self):
        self.add_to_cart_button.click()
