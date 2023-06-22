from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://demoqa.com/checkbox"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)

check_box = chrom_driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
check_box.click()

toggle = chrom_driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
toggle.click()
