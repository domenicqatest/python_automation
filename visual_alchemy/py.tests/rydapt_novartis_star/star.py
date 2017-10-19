# -*- coding: utf-8 -*-

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from selenium.webdriver.support.select import Select
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.common.exceptions import NoAlertPresentException
import requests
import time

base_url = "http://kcentra.reg-portal.va-dev.net/"

def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the full page
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    driver.set_window_size(898, 800)
    driver.get(base_url)
    driver.implicitly_wait(1)

def teardown_module(module):
    driver.quit()

class Header(object):

    # Row 1
    def test_presence_row1(self):
        """The top row is present"""

    # Row 2
    def test_presence_row2(self):
        """The middle row is present"""

    # Row 3
    def test_presence_row3(self):
        """The bottom row is present"""

    def test_row1_attributes(self):
        """Test Row 1 attributes"""
        # left side color

        # right side color

        # size

        # location

    def test_row2_left(self):
        """Test the attributes of the left side of row 2"""
        # image

        # size

        # location

    def test_row2_right(self):
        """Test the attributes of the right side of row 2"""
        # size of right side

        # location of ride side

        # background color

        # territory wrapper name

        # territory code

        # territory code options

        # login wrapper

        # greeting

        # user name

        # logout button

        # size of logout button

        # location of logout button

        # logout button image

        # button functionality

    def test_row2_combined(self):
        """Test the attributes of both sides of row 2"""
        # size

        # location

    def test_row3_left(self):
        """Test the attributes of the left side of row 3"""
        # size

        # location

        # background color

    def teardown_class(self):
        driver.quit()
