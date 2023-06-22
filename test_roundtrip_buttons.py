from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://www.saucedemo.com"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)
chrom_driver.refresh()
chrom_driver.get(base_url)
user_name = chrom_driver.find_element(By.NAME, "user-name")
user_name.send_keys(login)
password_line = chrom_driver.find_element(By.NAME, "password")
password_line.send_keys(password)
password_line.send_keys(Keys.RETURN)

menu = chrom_driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
link_about = chrom_driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
time.sleep(1)
link_about.click()
time.sleep(3)
chrom_driver.back()
time.sleep(3)
chrom_driver.forward()

