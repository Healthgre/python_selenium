import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://demoqa.com/dynamic-properties"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)

try:
    visible_button = chrom_driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
except NoSuchElementException as exception:
    print("NoSuchElementException")
    time.sleep(5)
    visible_button = chrom_driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print("Click visible button.")




