import unittest
import os
from appium import webdriver
import time

class IOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('../../app_files/Chess_iOS/HOXChess.app')
        #app = os.path.abspath('../../app_files/Kcentra_Onsite/OnSiteKcentra.app')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.3',
                'deviceName': 'iPhone 6'
            })
        self.driver.implicitly_wait(60)
##
    def tearDown(self):
        self.driver.quit()

    def test_open_close(self):
        """Click Practice and Home icon"""
        time.sleep(10)
        self.driver.find_element_by_name(" Practice").click()
        self.driver.find_element_by_name("go home").click()
        self.driver.find_element_by_name(" Practice").click()
        time.sleep(2)
        self.driver.find_element_by_name("computer").click()
        time.sleep(1)