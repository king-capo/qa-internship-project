from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from environment import PASSWORD


EMAIL_INPUT = (By.ID, 'email-2')
PASSWORD_INPUT = (By.NAME, 'Password')
LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
USR_NAME = 'Silas'

@given('Open Reelly login page')
def open_reelly_login_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')

@when('Input valid credentials')
def input_valid_credentials(context):
    email_input = context.driver.find_element(*EMAIL_INPUT)
    email_input.clear()
    email_input.send_keys('silasaction@gmail.com')

    password_input = context.driver.find_element(*PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys(PASSWORD)


@when('Click on login button')
def click_login_button(context):
    context.driver.find_element(*LOGIN_BUTTON).click()


@then('User is on Reelly homepage')
def verify_reelly_homepage(context):
    assert USR_NAME in context.driver.find_element(By.XPATH, '//span[@class="truncate block"]').text, \
        f'Expected query not displayed'
