from selenium import webdriver
from credentials import CREDENTIALS

driver = webdriver.Chrome('<PATH TO CHROMEDRIVER>')
driver.get('https://www.linkedin.com')

username = driver.find_element_by_id('session_key')
username.send_keys(CREDENTIALS['LOGIN ID'])
password = driver.find_element_by_id('session_password')
password.send_keys(CREDENTIALS['PASSWORD'])
login_button = driver.find_element_by_class_name('sign-in-form__submit-button')
login_button.click()

code = input("Verification code:\t")
verify = driver.find_element_by_id('input__phone_verification_pin')
verify.send_keys(code)
confirm_button = driver.find_element_by_id('two-step-submit-button')
confirm_button.click()

session_url = driver.command_executor._url
session_id = driver.session_id

f = open("session.txt", "w")
f.write(session_url)
f.write("\n")
f.write(session_id)
f.close()
