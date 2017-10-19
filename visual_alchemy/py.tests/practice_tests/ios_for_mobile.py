"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
import time

class IOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('../../visual_alchemy/apps/QuickBright/QuickBright.app')
        #app = os.path.abspath('../../visual_alchemy/apps/Payload/OnSite_Shire.app')
        #app = os.path.abspath('../../visual_alchemy/apps/Chess_iOS/HOXChess.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.2',
                'deviceName': 'iPhone 6'
            })
##
        self.driver.implicitly_wait(60)
##
    def tearDown(self):
        self.driver.quit()

    def test_open_close(self):
        """open/close"""
        time.sleep(5)