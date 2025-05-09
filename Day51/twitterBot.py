from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


class TwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.twitter.com")
        self.wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout (adjust as needed)

    def tweet_at_provider(self, twitter_handle: str, internet_speed: float, location: str, email: str, password: str):

        time.sleep(5)
        sign_in = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')))
        sign_in.click()

        time.sleep(10)
        username = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     '//*[@id="layers"]/div['
                                                                     '2]/div/div/div/div/div/div[2]/div['
                                                                     '2]/div/div/div[2]/div[2]/div/div/div/div['
                                                                     '5]/label/div/div[2]/div/input')))
        username.send_keys(email)
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                               '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()

        password_label = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     '//*[@id="layers"]/div['
                                                                     '2]/div/div/div/div/div/div[2]/div['
                                                                     '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                                     '3]/div/label/div/div[2]/div[1]/input')))
        password_label.send_keys(password)
        log_in = self.driver.find_element(By.XPATH,
                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                          '2]/div[2]/div[2]/div/div[1]/div/div/div')
        log_in.click()

        time.sleep(20)

        try:
            content = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                        '//*[@id="react-root"]/div/div/div['
                                                                        '2]/main/div/div/div/div/div/div[3]/div/div['
                                                                        '2]/div[1]/div/div/div/div[2]/div['
                                                                        '1]/div/div/div/div/div/div/div/div/div/div'
                                                                        '/label/div[1]/div/div/div/div/div/div['
                                                                        '2]/div/div/div/div')))
            content.send_keys(
                f"Hello, {twitter_handle}\nMy Internet speed is currently at, Download_speed: {internet_speed['download_speed']} and Upload_speed: {internet_speed['upload_speed']}\nThis is slow for a 4G Connection. I stay at {location}")
            post_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="react-root"]/div/div/div['
                                                   '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                   '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div['
                                                   '3]/div/span/span')
            post_button.click()
            print("Contents have been posted successfully!")
        except NoSuchElementException:
            print("Content could not be posted... Moving on")
        finally:
            pass
