from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://demoqa.com/buttons"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)

action = ActionChains(chrom_driver)
double = chrom_driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double).perform()

right_click = chrom_driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click).perform()


