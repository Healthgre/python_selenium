import datetime

import pytz as pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://www.saucedemo.com"
login = "standard_user"
password = "secret_sauce"

chrom_driver.get(base_url)
user_name = chrom_driver.find_element(By.NAME, "user-name")
user_name.send_keys(login)
password_line = chrom_driver.find_element(By.NAME, "password")
password_line.send_keys(password)
login_button = chrom_driver.find_element(By.NAME, "login-button")
login_button.click()

zones = pytz.timezone("Europe/Bratislava")
time_zone_slovak = datetime.datetime.now(zones)
now_date = time_zone_slovak.strftime("%Y.%m.%d %H.%M.%S")
data_name = "screenshot " + now_date + " .png"
chrom_driver.save_screenshot('C:\\Pycharm\\python_selenium\\screens\\' + data_name)
chrom_driver.close()
