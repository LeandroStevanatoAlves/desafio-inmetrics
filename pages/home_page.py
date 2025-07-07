from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.headphones_category = page.locator("#headphonesImg")
        self.laptops_category = page.locator("#laptopsImg")
        self.mice_category = page.locator("#miceImg")
        self.speakers_category = page.locator("#speakersImg")
        self.tablets_category = page.locator("#tabletsImg")

    def select_headphones_category(self):
        self.headphones_category.click()

    def select_laptops_category(self):
        self.laptops_category.click()

    def select_mice_category(self):
        self.mice_category.click()

    def select_speakers_category(self):
        self.speakers_category.click()

    def select_tablets_category(self):
        self.tablets_category.click()