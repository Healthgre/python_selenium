import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)

chrom_driver = webdriver.Chrome(options=chrom_options)
chrom_driver.get("https://www.saucedemo.com")
chrom_driver.maximize_window()
# user_name = chrom_driver.find_element(By.ID, "user-name").send_keys("standard_user")  # ID
user_name = chrom_driver.find_element(By.NAME, "user-name").send_keys("standard_user")  # NAME
# user_name = chrom_driver.find_element(By.XPATH, "//*[@id=\"user-name\"]").send_keys("standard_user")  # Full XPATH
# user_name = chrom_driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")  # ID XPATH
password = chrom_driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")  # CSS_SELECTOR
button_jogin = chrom_driver.find_element(By.NAME, "login-button").click()
# time.sleep(3)
# chrom_driver.close()

# ff_driver = webdriver.Firefox()
# ff_driver.get("https://www.saucedemo.com")
# ff_driver.maximize_window()
# ff_driver.find_element('name', 'user-name').send_keys("standard_user")
# ff_driver.find_element('id', 'password').send_keys("secret_sauce")
# ff_driver.find_element(By.NAME, "login-button").click()
# time.sleep(1)
# ff_driver.close()
