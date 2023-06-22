import time

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
time.sleep(2)
user_name.clear()



