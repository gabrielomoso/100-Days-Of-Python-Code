EMAIL = "example@gmail.com"
PASSWORD = "******"
PHONE_NUMBER = "******"
JOB_ROLE = "Python Developer" # Input The Job role you like to search for

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time



# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com")
wait = WebDriverWait(driver, 10)  # 10 seconds timeout (adjust as needed)

# Logging into Linked
email = wait.until(EC.visibility_of_element_located((By.ID, "session_key")))
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "session_password")
password.send_keys(PASSWORD)
submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit.click()

# Navigating to the Jobs Section
input("Please press enter if completed the CAPTCHA: ")
time.sleep(5)
jobs = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')))
jobs.click()
search = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "jobs-search-box__text-input")))
search.send_keys(JOB_ROLE)

# Simulate pressing the "Enter" key for the search Bar
search_enter = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-search-box__text-input")))
search_enter.send_keys(Keys.ENTER)

# Clicking Easy Apply Search Option
easy_apply = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Easy Apply filter."]')))
easy_apply.click()

time.sleep(5)

# Finding all Available Jobs
all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_jobs[1::]:
    job.click()

    # Getting the name of the job, so I can use to locate the apply button associated with it
    names = job.text.split("\n")

    time.sleep(2)
    easy_apply_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label="Easy Apply to {names[0].strip()} at {names[1].strip()}"]')))
    easy_apply_button.click()
    time.sleep(2)
    phone_number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
    phone_number.send_keys(PHONE_NUMBER)
    time.sleep(2)
    next_button = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
    next_button.click()

    try:
        # Check if the Review button is found on this page
        time.sleep(2)
        review_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
        review_button.click()
    except NoSuchElementException:
        # If not found, exit page and go to the next Job
        print("Review button not found. Going to the next Application")
        time.sleep(2)
        dismiss_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
        dismiss_button.click()
        time.sleep(2)
        discard_button = driver.find_element(By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]')
        discard_button.click()
        time.sleep(2)
    else:
        # If found, proceed with application
        time.sleep(2)
        submit_application = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
        submit_application.click()
        time.sleep(2)
        print(f"Your Application has been successful to {names[0].strip()} at {names[1].strip()}")
        break


time.sleep(2)
#Ending Program
driver.quit()


