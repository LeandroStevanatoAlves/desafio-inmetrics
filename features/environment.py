from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright = sync_playwright().start()

def before_scenario(context, scenario):
    print("Before")
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.base_url = "https://advantageonlineshopping.com/#/"

def after_scenario(context, scenario):
    print("After")
    context.browser.close()