from playwright.sync_api import sync_playwright

def main():
    #print("Hello from desafio-inmetrics!")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    # Adiciona produto e acessa o checkout
    page.click("text=TABLETS")
    page.click("div.categoryRight li:nth-child(1)")
    page.click("#productProperties button[name='save_to_cart']")
    page.click("#menuCart")
    page.click("#checkOutPopUp")


if __name__ == "__main__":
    main()
