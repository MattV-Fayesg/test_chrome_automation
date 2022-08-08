import unittest
import HtmlTestRunner
import sys
try:
    from wd_connect import Driver
    from objects.chrome_home_screen import ChromeHome
    from objects.initial_screen import (ChromeBTN_Acceptance,
                                        ChromeSyncAccount)
except ModuleNotFoundError:
    sys.path.insert(0, '/home/fayesg/Documents/Coding/Projects/AndroidAuto/auto_chrome')
    from wd_connect import Driver
    from objects.chrome_home_screen import ChromeHome
    from objects.initial_screen import (ChromeBTN_Acceptance,
                                        ChromeSyncAccount)


class TestingChromeHomeSearchingString(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        launchAcceptBTN = ChromeBTN_Acceptance(self.driver)
        launchAcceptBTN.accept_terms()
        launchSyncAccount = ChromeSyncAccount(self.driver)
        launchSyncAccount.deny_sync()

    def tearDown(self):
        self.driver.instance.quit()

    def test_searching_string_True(self):
        launch = ChromeHome(self.driver)
        launch.search('Teste')


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='tests_report',
            report_title='TestReport')
    )
