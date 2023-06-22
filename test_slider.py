from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "http://www.automationpractice.pl/index.php?id_category=3&controller=category"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)

range_price = chrom_driver.find_element(By.XPATH, "//div[@id='layered_price_slider']")
range_price.click()


action = ActionChains(chrom_driver)

action.click_and_hold(range_price).move_by_offset(200, 0).release().perform()

#  XPath с очень длинным названием класса
#  // div[contains(@class,'кусок длинного кода который нужен']

