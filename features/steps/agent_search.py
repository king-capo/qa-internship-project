from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


FILTER_AGENT = (By.CSS_SELECTOR, '[wized*=servicesOfferedFilterAgent]')
MARKET_BUTTON = (By.XPATH, '//span[(text()="Market")]')

@given('Open Reelly main page')
def open_reelly_main_page(context):
    context.driver.get('https://soft.reelly.io/')


@when('Click on market button')
def click_market_button(context):
    context.driver.find_element(*MARKET_BUTTON).click()


@when('Verify market page is open')
def verify_market_page(context):
    expected_text = 'Offers for you'
    actual_text = context.driver.find_element(By.XPATH, '//div[contains(@text(),"Offers for you")]').text
    context.driver.find_element(By.XPATH, '//div[contains(@text(),"Offers for you")]')
    assert expected_text == actual_text, f'Expected "{expected_text}" but got "{actual_text}"'


@when('Filter market results for Agent')
def filter_market_results_for_agent(context):
    context.driver.find_element(*FILTER_AGENT).click()


@then('Market results for Agent are shown')
def verify_market_results_for_agent(context):
    assert 'Agent' in context.driver.page_source, f'Expected "Agent" in {context.driver.page_source}'