from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://www.saucedemo.com"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)
user_name = chrom_driver.find_element(By.NAME, "user-name")
user_name.send_keys(login)
password_line = chrom_driver.find_element(By.NAME, "password")
password_line.send_keys(password)
login_button = chrom_driver.find_element(By.NAME, "login-button")
login_button.click()

"""INFO Product 1"""
product_1 = chrom_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)
price_product_1 = chrom_driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = chrom_driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()

cart = chrom_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()

"""INFO Cart Product 1"""
cart_product_1 = chrom_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
cart_value_product_1 = cart_product_1.text
print(cart_value_product_1)
cart_price_product_1 = chrom_driver.find_element(By.XPATH,
                                                 "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_value_price_product_1 = cart_price_product_1.text
print(cart_value_price_product_1)
