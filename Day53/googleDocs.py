from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdB9QbQGvAYFJVD9kuiaT3hgR96ebGasZkm5WdDO_ZzLfF1OQ/viewform?usp=sf_link"

class GoogleDocs:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(LINK)
        self.wait = WebDriverWait(self.driver, 20)  # 20 seconds timeout (adjust as needed)

    def fill_form(self, datas: list):
        print("Opening Google Docs")
        time.sleep(5)

        for data in datas:
            input_fields = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[type="text"]')))

            # Enumerate() keeps track of the index of each data in the list of data so it can be used to specify which input it will fall in
            for i, value in enumerate(data):
                input_fields[i].send_keys(value)

            submit = self.driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
            submit.click()
            print("Submitted data...")
            time.sleep(2)
            another_response = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Submit another response")))
            another_response.click()
            time.sleep(2)

        self.driver.quit()