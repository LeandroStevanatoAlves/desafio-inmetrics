from behave import given, when, then
from playwright.sync_api import expect


@given(u'the customer is logged in')
def step_impl(context):
    context.menu_page.open_login_modal()
    context.login_page.login(context.usuario_user_valido.get_loginname(), context.usuario_user_valido.senha)


@given(u'adds a product to the cart')
def step_impl(context):
    context.home_page.select_tablets_category()
    context.category_page.select_first_product()
    context.product_detail_page.add_to_cart()


@when(u'they proceed to checkout')
def step_impl(context):
    context.menu_page.open_cart_modal()
    context.shopping_cart_page.proceed_to_checkout()
    context.shipping_details_page.click_next()


@when(u'make a payment with MasterCredit')
def step_impl(context):
    context.payment_page.select_master_credit_and_pay()
    #context.page.get_by_role("img", name="Master credit").click()
    #context.page.locator("#pay_now_btn_MasterCredit").click()


@when(u'make a payment with SafePay')
def step_impl(context):
    context.payment_page.select_safepay_and_pay(context.safepay)
    #context.page.get_by_role("img", name="Safepay").click()
    #context.page.fill("input[name='safepay_username']", context.safepay.username)
    #context.page.fill("input[name='safepay_password']", context.safepay.password)
    #context.page.click("#pay_now_btn_SAFEPAY")


@then(u'the purchase is completed successfully')
def step_impl(context):
    expect(context.page).to_have_url(f"{context.base_url}/orderPayment")
    context.order_confirmation_page.verify_order_payment_title()
    context.order_confirmation_page.verify_thank_you_message()
    context.order_confirmation_page.verify_order_number_label()
    context.order_confirmation_page.verify_tracking_number_label()