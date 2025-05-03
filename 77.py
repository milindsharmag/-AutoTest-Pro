from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service("C:\\Users\\ASUS\\Desktop\\browser\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.save_screenshot("HomePage.png")

driver.find_element(By.ID, "user-name").send_keys('visual_user')
driver.find_element(By.XPATH, "//*[@id='password']").send_keys('secret_sauce')
driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action").click()

driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div").click()

driver.find_element(By.ID, "add-to-cart").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

rooter = driver.find_element(By.ID, "checkout")
rooter.click()
time.sleep(10)

driver.find_element(By.ID, "first-name").send_keys("virat")

driver.find_element(By.ID, "last-name").send_keys("kohli")

driver.find_element(By.ID, "postal-code").send_keys("570088")

time.sleep(5)

driver.find_element(By.ID, "continue").click()

time.sleep(5)

driver.save_screenshot("Checkout.png")

driver.find_element(By.ID, "finish").click()

time.sleep(10)



