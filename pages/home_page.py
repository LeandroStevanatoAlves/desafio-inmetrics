from playwright.sync_api import Page, expect

class HomePage():
    def __init__(self, page: Page):
        self.user_icon = page.locator("#hrefUserIcon")
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.sign_in_button = page.locator("#sign_in_btn")

    def open_page(self):
        self.pa

    def open_login_modal(self):
        self.user_icon.click()
        expect(self.username_input).to_be_visible()

    def login(self, username: str, password: str):
        self.open_login_modal()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.sign_in_button.click()