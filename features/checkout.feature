# language: en
Feature: Checkout

  Scenario: Successful checkout using MasterCredit (credit card)
    Given the customer is logged in
    And adds a product to the cart
    When they proceed to checkout
    And make a payment with MasterCredit
    Then the purchase is completed successfully

  Scenario: Successful checkout using SafePay
    Given the customer is logged in
    And adds a product to the cart
    When they proceed to checkout
    And make a payment with SafePay
    Then the purchase is completed successfully

  Scenario: It is not possible to checkout without being logged in
    Given the customer is not logged in
    And adds a product to the cart
    When they proceed to checkout
    Then the customer is redirected to the login screen