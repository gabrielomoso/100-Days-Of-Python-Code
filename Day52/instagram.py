from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time


class Instagram:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.wait = WebDriverWait(self.driver, 20)  # 20 seconds timeout (adjust as needed)

    def login(self, credential: str, password: str):
        credentials = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]')))
        credentials.send_keys(credential)
        passwords = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Password"]')
        passwords.send_keys(password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        log_in.click()

        time.sleep(5)
        not_now1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
        not_now1.click()

        time.sleep(5)
        input("Wait for a while, you will see a pop up to accept notification\nClick Enter when you have accepted or declined: ")
        print("Login successful...")



    def find_followers(self, ig_handle):
        print(f"Going into @{ig_handle} followers")
        self.driver.get(f"https://www.instagram.com/{ig_handle}/followers")

        time.sleep(10)

        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button div div[class="_ap3a _aaco _aacw _aad6 _aade"]')))
        print(f"Found {ig_handle}'s followers")

        subscribed_to = 0

        def scrol():
            # Script to scroll down... FYI I dont know how it works but it works..lol
            scr1 = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

        while True:
            scrol()
            scrol()
            time.sleep(5)

            all_followers = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button div div[class="_ap3a _aaco _aacw _aad6 _aade"]')))
            not_following = [followers for followers in all_followers if "follow" == followers.text.lower()]
            if len(not_following) < 1:
                return subscribed_to

            for follow in not_following:
                time.sleep(2)
                try:
                    follow.click()
                    subscribed_to += 1
                    print(f"Followed {subscribed_to}")
                except ElementClickInterceptedException:
                    print("Haha... You have been Restricted")
                    return subscribed_to












    def follow(self):
        pass
