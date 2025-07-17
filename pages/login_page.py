from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.order_payment_message = page.get_by_role("heading", name="ORDER PAYMENT")
        self.registration_button = page.get_by_role("button", name="REGISTRATION")
        self.url = f"{base_url}/login"

    def new_user_registration(self):
        self.registration_button.click()

    def verify_order_payment_message(self):
        expect(self.order_payment_message).to_be_visible()
        expect(self.order_payment_message).to_contain_text("ORDER PAYMENT")

    def verify_url(self, page: Page):
        expect(page).to_have_url(self.url)