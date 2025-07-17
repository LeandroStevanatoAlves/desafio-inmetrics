from playwright.sync_api import Page, expect


class LoginModal:
    def __init__(self, page: Page):
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.sign_in_button = page.locator("#sign_in_btn")
        self.close_icon = page.locator(".closeBtn")

    def close_login_modal(self):
        self.close_icon.click()

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.sign_in_button.click()
