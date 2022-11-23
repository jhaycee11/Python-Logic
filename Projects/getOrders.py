from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import creds

#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
service = Service(executable_path="./chromedriver")
chrome_browser = webdriver.Chrome(service=service)#, chrome_options=chrome_options)
chrome_browser.get("https://akabanebussan.com/user-registration/")

username = chrome_browser.find_element(By.ID, "username")
username.send_keys(creds.user)

password = chrome_browser.find_element(By.ID, "password")
password.send_keys(creds.password)

login = chrome_browser.find_element(By.CLASS_NAME, "button")
login.click()



chrome_browser.get("https://akabanebussan.com/user-registration/orders/")
order_numbers = chrome_browser.find_elements(By.CLASS_NAME, "woocommerce-orders-table__cell-order-number")
for i in order_numbers:
    print(i.text)