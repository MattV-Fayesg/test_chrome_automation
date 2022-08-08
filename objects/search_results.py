from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class SearchResults:

    def __init__(self, driver):
        self.driver = driver

        webview = self.driver.instance.contexts[1]
        self.driver.instance.switch_to.context(webview)
        self.img_button = WebDriverWait(self.driver.instance, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#hdtb-msb > div:nth-child(3) > a'))
        )

    def change_to_img(self):
        self.img_button.click()

