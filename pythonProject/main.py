from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.typescriptlang.org/")

assert "TypeScript" in driver.title

elem = driver.find_element(By.CLASS_NAME, "fluid-button")
print(elem.is_selected())
print(elem.is_displayed())

h2 = driver.find_element(By.TAG_NAME, "h2")
print(driver.title)
print(h2.get_attribute("innerHTML"))
assert "What is TypeScript?" in h2.get_attribute("innerHTML")

elem = driver.find_element(By.ID, "search-box-top")
elem.click()
elem.send_keys("interface")
elem.send_keys(Keys.ENTER)

assert "TypeScript: Documentation - DOM Manipulation" in driver.title
driver.close()