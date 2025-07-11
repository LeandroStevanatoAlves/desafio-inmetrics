from playwright.sync_api import Page

from model.safe_pay import SafePay


class PaymentPage:
    def __init__(self, page: Page):
        self.master_credit_option = page.get_by_role("img", name="Master credit")
        self.master_credit_pay_now_button = page.locator("#pay_now_btn_MasterCredit")
        self.safepay_option = page.get_by_role("img", name="Safepay")
        self.safepay_username_input = page.locator("input[name='safepay_username']")
        self.safepay_password_input = page.locator("input[name='safepay_password']")
        self.safepay_pay_now_button = page.locator("#pay_now_btn_SAFEPAY")

    def select_master_credit_and_pay(self):
        self.master_credit_option.click()
        self.master_credit_pay_now_button.click()

    def select_safepay_and_pay(self, safepay: SafePay):
        self.safepay_option.click()
        self.safepay_username_input.fill(safepay.username)
        self.safepay_password_input.fill(safepay.password)
        self.safepay_pay_now_button.click()
