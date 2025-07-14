from playwright.sync_api import Page, expect


class OrderConfirmationPage:
    def __init__(self, page: Page):
        self.order_confirmation_title = page.locator("xpath=/html/body/div[3]/section/article/h3")
        self.thank_you_message = page.locator("#orderPaymentSuccess h2 span")
        self.order_number_label = page.locator("#orderNumberLabel")
        self.tracking_number_label = page.locator("#trackingNumberLabel")

    def verify_order_payment_title(self):
        expect(self.order_confirmation_title).to_be_visible()
        expect(self.order_confirmation_title).to_contain_text("ORDER PAYMENT")

    def verify_thank_you_message(self):
        expect(self.thank_you_message).to_be_visible()
        expect(self.thank_you_message).to_contain_text("Thank you for buying with Advantage")

    def verify_order_number_label(self):
        expect(self.order_number_label).not_to_be_empty()

    def verify_tracking_number_label(self):
        expect(self.tracking_number_label).not_to_be_empty()
