from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SpeedTest:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.speedtest.net")
        self.wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout (adjust as needed)

    def get_internet_speed(self):
        time.sleep(10)
        cookie_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="onetrust-accept-btn'
                                                                                     '-handler"]')))
        cookie_button.click()
        start_speed_test = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="start speed '
                                                                                        'test - connection type '
                                                                                        'multi"]')))
        start_speed_test.click()

        time.sleep(60)
        download_speed = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "download-speed"))).text
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        return {
                    "download_speed": float(download_speed),
                    "upload_speed": float(upload_speed)
        }

