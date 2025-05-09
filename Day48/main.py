from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

wait = WebDriverWait(driver, 20)  # 10 seconds timeout (adjust as needed)

# Waiting for the site to load in case of slow network
english = wait.until(EC.visibility_of_element_located((By.ID, "langSelect-EN")))
english.click()
cookie = wait.until(EC.visibility_of_element_located((By.ID, "bigCookie")))
cookie.click()

timeout = time.time() + 60 * 5
time_interval = time.time() + 5
while time.time() < timeout: # while time less than 30 seconds

    # clicking the cookie
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()

    # after 5secs it clicks something in the store
    if time.time() >= time_interval:
        # Getting all available items in the store
        prices = []
        store = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")

        # Getting each item prices and converting to int
        if store:
            for item in store:
                prices.append(int(item.text.split('\n')[1].replace(",", "")))

            # Getting the index of the max price in the list
            max_index = prices.index(max(prices))

            # Clicking the highest available item in the store
            highest_item = store[max_index]
            highest_item.click()
            print(f"\n{store[max_index].text} Active")

        time_interval = time.time() + 5  # Resetting the secs timer

cookies_per_sec = driver.find_element(By.ID, "cookies").text
print(f"\nHighScore in 5 minutes secs : {cookies_per_sec}")

driver.quit()
