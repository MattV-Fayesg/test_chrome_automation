import unittest
import HtmlTestRunner
import sys
try:
    from wd_connect import Driver
    from objects.initial_screen import (ChromeBTN_Acceptance,
                                        ChromeSyncAccount)
except ModuleNotFoundError:
    sys.path.insert(0, '/home/fayesg/Documents/Coding/Projects/AndroidAuto/auto_chrome')
    from wd_connect import Driver
    from objects.initial_screen import (ChromeBTN_Acceptance,
                                        ChromeSyncAccount)


class TestChromeBTN_Acceptance(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.close_app()

    def test_accept_btn(self):
        launch = ChromeBTN_Acceptance(self.driver)
        launch.accept_terms()


class TestChromeSyncAccount(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        launch = ChromeBTN_Acceptance(self.driver)
        launch.accept_terms()

    def tearDown(self):
        self.driver.instance.close_app()

    def test_deny_sync(self):
        launch = ChromeSyncAccount(self.driver)
        launch.deny_sync()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='tests_report', report_title='TestReport')
    )
