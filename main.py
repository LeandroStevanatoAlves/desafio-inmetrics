from playwright.async_api import expect
from playwright.sync_api import sync_playwright

def main():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    # Login
    page.click("#hrefUserIcon")
    page.fill("input[name='username']", "fulano5")
    page.fill("input[name='password']", "Aa123456")
    page.click("#sign_in_btn")

    # Adiciona produto no carrinho
    page.click("#tabletsImg")
    page.click("div.categoryRight li:nth-child(1)")
    page.click("#productProperties button[name='save_to_cart']")

    # Realiza o checkout
    page.click("#menuCart")
    page.click("#checkOutButton")

    # Página Shipping Details
    page.click("#next_btn")

    # Seleciona MasterCredit
    page.get_by_role("img", name="Master credit").click()
    #page.get_by_text("Edit", exact=True).click()
    #page.locator("input[name='card_number']").click()
    #page.locator("input[name='card_number']").fill("1234 5678 9012")
    #page.locator("input[name='cvv_number']").fill("456")
    #page.locator("select[name='mmListbox']").select_option("string:09")
    #page.locator("select[name='yyyyListbox']").select_option("string:2028")
    #page.locator("input[name='cardholder_name']").fill("Fulano da Silva")
    page.locator("#pay_now_btn_ManualPayment").click()

    # Seleciona SafePay
    #safepay_username = "12345"
    #safepay_password = "Aa123456"
    #page.get_by_role("img", name="Safepay").click()
    #page.fill("input[name='safepay_username']", safepay_username)
    #page.fill("input[name='safepay_password']", safepay_password)
    ##page.get_by_role("checkbox", name="save_safepay").check()
    #page.click("#pay_now_btn_SAFEPAY")

    titulo_order_payment = page.locator("xpath=/html/body/div[3]/section/article/h3")
    assert "ORDER PAYMENT" in titulo_order_payment.inner_text()

    mensagem_thank_you = page.locator("xpath=//*[@id='orderPaymentSuccess']/h2/span")
    assert "Thank you for buying with Advantage" in mensagem_thank_you.inner_text()

    metodo_pagamento = page.locator("xpath=//*[@id='orderPaymentSuccess']/div/div[2]/div[1]/label").inner_text()
    metodo_pagamento2 = page.locator("xpath=//*[@id='orderPaymentSuccess']/div/div[2]/div[1]/label").all_inner_texts()
    print("----------")
    print(f"{metodo_pagamento2[0]}\n")
    print("----------")
    #assert "SafePay" in metodo_pagamento.inner_text()
    #expect(metodo_pagamento).to_have_text("SafePay")
    #assert "SafePay" == metodo_pagamento.inner_text(), f"esperado: 'SafePay' - recebido: '{metodo_pagamento}'"

if __name__ == "__main__":
    main()
