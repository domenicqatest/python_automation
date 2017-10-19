import os
import time

import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../../visual_alchemy/apps/Payload/selendroid-test-app.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_open_close(self):
        """open and close"""
        time.sleep(5)


#if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    #unittest.TextTestRunner(verbosity=2).run(suite)