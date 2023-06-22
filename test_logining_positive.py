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

text_products = chrom_driver.find_element(By.XPATH, "//span[@class='title']")
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == "Products"
print("Good")

url = "https://www.saucedemo.com/inventory.html"
get_url = chrom_driver.current_url
print(get_url)


