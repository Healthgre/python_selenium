from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)
chrom_driver = webdriver.Chrome(options=chrom_options)

base_url = "https://demoqa.com/radio-button"
login = "standard_user"
password = "secret_sauce"

chrom_driver.maximize_window()
chrom_driver.get(base_url)

yes_radio_button = chrom_driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_radio_button.click()
try:
    message = chrom_driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "No"
except AssertionError as exception:
    chrom_driver.refresh()
    yes_radio_button = chrom_driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio_button.click()
    message = chrom_driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
    print("CheckBox Yes.")
print("Test Over.")