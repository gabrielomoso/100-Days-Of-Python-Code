from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.tinder.com")
wait = WebDriverWait(driver, 10)  # 10 seconds timeout (adjust as needed)

log_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
log_in_button.click()
log_in_number = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Log in with phone number"]')))
log_in_number.click()

user_number = input("Input your Phone Number: ")
input_number = driver.find_element(By.CSS_SELECTOR, 'div[aria-labelledby="MODAL_LOGIN"] input[aria-label="Enter your mobile number"]')
input_number.send_keys(user_number)
continue_button = driver.find_element(By.CSS_SELECTOR, 'div[aria-labelledby="MODAL_LOGIN"] button')
continue_button.click()
print("If you get a CAPTCHA pop up. Do it manually")

# OPT Code
opt_codes = input("Enter The OPT Code Sent to Your Phone Number: ").strip()
for i in range(6):
    opt_code = driver.find_element(By.CSS_SELECTOR, f'input[aria-label="OTP code digit {i+1}"]')
    opt_code.send_keys(int(opt_codes[i]))

# This is where you stopped... complete it
next_button = driver.find_element(By.XPATH, '// *[ @ id = "c-1177047094"] / main / div[1] / div[1] / div / div[4] / button')
next_button.click()

time.sleep(1)
send_email_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c-1177047094"]/main/div/div/div[1]/div/div[2]/button')))
send_email_button.click()

# OPT Code
email_opt_codes = input("Enter The OPT Code Sent to Your Email: ").strip()
for i in range(6):
    opt_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'input[aria-label="OTP code digit {i+1}"]')))
    opt_code.send_keys(int(email_opt_codes[i]))

confirm_button = driver.find_element(By.XPATH, '//*[@id="c-1177047094"]/main/div[1]/div/div[1]/div/div[2]/div[2]/button')
confirm_button.click()

time.sleep(5)
# After Logged In
on_boarding_allow = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-labelledby="onboarding-title"] button[aria-label="Allow"]')))
on_boarding_allow.click()
on_boarding_enable = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-labelledby="onboarding-title"] button[aria-label="Not interested"]')))
on_boarding_enable.click()
on_boarding_accept = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c-1398387530"]/div/div[2]/div/div/div[1]/div[1]/button')))
on_boarding_accept.click()


for i in range(100):
    time.sleep(1)
    try:
        like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c-1398387530"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span')))
        like_button.click()
    except NoSuchElementException:
        cancel_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-hidden="false"]')))
        cancel_button.click()