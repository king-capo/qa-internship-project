from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


MARKET_BUTTON = (By.XPATH, '//span[(text()="Market")]')
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://soft.reelly.io/sign-in')

# click "email" input field
driver.find_element(By.ID,"email-2").click()
driver.find_element(By.ID,"email-2").clear()
driver.find_element(By.ID,"email-2").send_keys('silasaction@gmail.com')
# click "password" input field
driver.find_element(By.NAME,"Password").click()
driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys('713-Chill')
# click "submit"
driver.find_element(By.XPATH, '//a[@wized="loginButton"]').click()
sleep(4)

# click "market" button on sidebar
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MARKET_BUTTON)).click()

# verify market page is open
expected_text = 'Offers for you'
actual_text = driver.find_element(By.XPATH, '//div[@class="new-market-h1"]').text
assert expected_text == actual_text, f'Expected "{expected_text}" but got "{actual_text}"'
sleep(4)

# filter market results for Agent
driver.find_element(By.CSS_SELECTOR, '[wized*=servicesOffersFilterAgent]').click()
sleep(4)

# click "Agent" button
assert driver.quit()