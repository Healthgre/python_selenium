from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://demoqa.com/date-picker"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)


new_data = chrom_driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
for i in range(10):
    new_data.send_keys(Keys.BACKSPACE)
new_data.send_keys("01.01.1992")
new_data.send_keys(Keys.ENTER)
chrom_driver.refresh()


"""Выбрать дату на календаре"""
new_data = chrom_driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_data.click()

day_1 = chrom_driver.find_element(By.XPATH, "//div[@aria-label='Choose Saturday, July 1st, 2023']")
day_1.click()

#  XPath с очень длинным названием класса
#  // div[contains(@class,'кусок длинного кода который нужен']

new_data = chrom_driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_data.click()

#  Сумел выбрать нужный год.
year = chrom_driver.find_element(By.XPATH, "//option[@value='2034']")
year.click()




