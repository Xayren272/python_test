from sys import prefix

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

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

assert "https://www.typescriptlang.org/" in driver.current_url

link_finder = locate_with(By.TAG_NAME, "a").near({By.CLASS_NAME: "call-to-action"})
button1 = driver.find_element(link_finder)
button1.click()

button2 = driver.find_element(link_finder)
ActionChains(driver)\
    .click(button2)\
    .pause(4)\
    .perform()

ActionBuilder(driver).clear_actions()

assert "https://www.typescriptlang.org/play" in driver.current_url

input_field = driver.find_element(By.CLASS_NAME, "inputarea")
ActionChains(driver)\
    .click(input_field)\
    .key_down(Keys.CONTROL)\
    .send_keys("a")\
    .pause(1)\
    .key_up(Keys.CONTROL)\
    .send_keys("const test = true;")\
    .pause(2)\
    .perform()

ActionBuilder(driver).clear_actions()


driver.close()