from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class ChromeBTN_Acceptance:
    def __init__(self, driver):
        self.driver = driver
        self.accept_btn_button = WebDriverWait(self.driver.instance, 20).until(
            EC.presence_of_element_located((By.ID, 'com.android.chrome:id/terms_accept')))

    def accept_terms(self):
        if self.accept_btn_button.is_displayed():
            self.accept_btn_button.click()


class ChromeSyncAccount:

    def __init__(self, driver):
        self.driver = driver
        self.accept_sync_button = WebDriverWait(self.driver.instance, 20).until(EC.presence_of_element_located((
            By.ID, 'com.android.chrome:id/positive_button'
        )))
        self.deny_sync_button = WebDriverWait(self.driver.instance, 20).until(
            EC.visibility_of_element_located((By.ID, 'com.android.chrome:id/negative_button')))

    def accept_sync(self):
        self.accept_sync_button.click()

    def deny_sync(self):
        self.deny_sync_button.click()

