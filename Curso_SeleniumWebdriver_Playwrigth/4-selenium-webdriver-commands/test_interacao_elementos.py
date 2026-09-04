import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get("https://www.saucedemo.com/")

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# send_keys envia o texto para o elemento
username.send_keys("standard_user")
password.send_keys("secret_sauce")
# click() clica no elemento
btn_login.click()
time.sleep(2)

# text = browser.find_element(By.CLASS_NAME, "title")
product_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(product_title.text)
assert product_title.text == "Products"


# get_attribute() retorna o valor do atributo do elemento
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("alt"))
assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack"
