from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")
button.click()

assert "alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")
assert "alert-success" in driver.find_element(By.ID, "first-name").get_attribute("class")
assert "alert-success" in driver.find_element(By.ID, "last-name").get_attribute("class")
assert "alert-success" in driver.find_element(By.ID, "address").get_attribute("class")
assert "alert-success" in driver.find_element(By.ID, "city").get_attribute("class")
assert "alert-success" in driver.find_element(By.ID, "country").get_attribute("class")
assert "alert-success" in driver.find_element(By.ID, "job-position").get_attribute("class")
assert "alert-success" in driver.find_element(By.ID, "company").get_attribute("class")




driver.quit()







