from playwright.sync_api import Page

class CategoryPage:
    def __init__(self, page: Page):
        self.first_product_link = page.locator("div.categoryRight ul > li:nth-child(1)")

    def select_first_product(self):
        self.first_product_link.click()