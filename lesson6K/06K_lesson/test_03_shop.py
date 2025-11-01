from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Екатерина")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Тимофеева")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("96100")
driver.find_element(By.CSS_SELECTOR, "#continue").click()
text = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
text = text.replace("Total: $", "")  
total = float(text)
assert total == 58.29

sleep(3)
driver.quit()