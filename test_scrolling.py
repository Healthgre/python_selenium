import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://www.saucedemo.com"
login = "standard_user"
password = "secret_sauce"

# chrom_driver.maximize_window()
chrom_driver.get(base_url)
user_name = chrom_driver.find_element(By.NAME, "user-name")
user_name.send_keys(login)
password_line = chrom_driver.find_element(By.NAME, "password")
password_line.send_keys(password)
login_button = chrom_driver.find_element(By.NAME, "login-button")
login_button.click()

time.sleep(2)
chrom_driver.execute_script('window.scrollTo(0, 100)')
time.sleep(2)
chrom_driver.execute_script('window.scrollTo(0, 200)')
time.sleep(2)
chrom_driver.execute_script('window.scrollTo(0, 300)')
time.sleep(2)


action = ActionChains(chrom_driver)
footer = chrom_driver.find_element(By.XPATH, "//div[@class='footer_copy']")
action.move_to_element(footer).perform()