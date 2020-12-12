from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import login
import time

driver=webdriver.Chrome("C:\\Users\\my pc\\Desktop\\chromedriver.exe")
action = ActionChains(driver)
driver.get("http://127.0.0.1:8000/")
time.sleep(3)
sign_in= driver.find_element_by_link_text('Sign in')
sign_in.click()
time.sleep(3)
usernmae= driver.find_element_by_name('username')
usernmae.send_keys(login.USERNAME)
time.sleep(3)

password= driver.find_element_by_name('password')
password.send_keys(login.PASSWORD)
time.sleep(3)

log_in= driver.find_element_by_css_selector('#content > div > div > div > form > p > input[type=submit]')
log_in.click()
time.sleep(3)
product=driver.find_element_by_link_text('iPhone')
product.click()
time.sleep(3)
nego=driver.find_element_by_css_selector('#concard > div > p:nth-child(4) > button')
nego.click()
time.sleep(3)
message=driver.find_element_by_css_selector('#myForm > div > div > form > input[type=text]:nth-child(1)')
message.send_keys('hello')
submit=driver.find_element_by_css_selector('#myForm > div > div > form > input[type=submit]:nth-child(2)')
submit.click()




