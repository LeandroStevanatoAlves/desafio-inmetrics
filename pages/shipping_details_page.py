from playwright.sync_api import Page


class ShippingDetailsPage:
    def __init__(self, page: Page):
        self.next_button = page.locator("button#next_btn.a-button.nextBtn")

    def click_next(self):
        self.next_button.click()
