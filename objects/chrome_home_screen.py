from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class ChromeHome:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = WebDriverWait(self.driver.instance, 20).until(EC.presence_of_element_located((
            By.ID, 'com.android.chrome:id/search_box_text')))

        # self.back_action = driver.tap([(242, 1844)])

    def search(self, string):
        string = str(string)
        self.search_box.send_keys(string)
        send_search = WebDriverWait(self.driver.instance, 20).until(
            EC.presence_of_element_located((By.ID, 'com.android.chrome:id/line_1')))
        send_search.click()

