from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


FILTER_AGENT = (By.CSS_SELECTOR, 'div.new-market-tag[wized="servicesOffersFilterAgent"]')
MARKET_BUTTON = (By.XPATH, '//span[text()="Market"]')
offers_grid = (By.CSS_SELECTOR, 'div.w-layout-grid.new-market-offers-grid')


@when('Click on market button')
def click_market_button(context):
    context.driver.find_element(*MARKET_BUTTON).click()
    sleep(2)
    assert 'Offers for you' in context.driver.find_element(By.CSS_SELECTOR, 'div.new-market-h1').text, \
        f'Expected query not displayed'



@when('Filter market results for Agent')
def filter_market_results_for_agent(context):
    context.driver.find_element(*FILTER_AGENT).click()


@then('Market results for Agent are shown')
def verify_market_results_for_agent(context):
    context.driver.wait.until(
        EC.presence_of_element_located(offers_grid),
        message="Market results for Agent not shown"
    )
    #result_list={}
    mrkt_result = context.driver.find_elements(By.XPATH, '//div.new-market-card')
    for result in mrkt_result:
        assert 'Agent' in context.driver.find_element(
            By.XPATH, './/div[@wized="servicesOffersCardClientTagText"]').text, \
            f'Agent tag not found in result: {result.text}'
        print('All results verified with Agent tag!')

  ("Agent tag in all results shown")