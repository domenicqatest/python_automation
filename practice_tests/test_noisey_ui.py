#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Front-end tests for Noisey.

Usage::
    py.test -s -v --tb=line test_noisey_ui.py

-s: No capture. Don't suppress output.

-v: Verbose. Gimme all the info.

--tb=line: Shorten the tracebacks should an error occur.
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from ..utils.exceptions import FunctionalError
from ..utils.log import logger
from assertlib import assertEqual, assertAtleast
base_url = "https://staging-noisey.viceops.net"


def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the fullpage
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    log = logger()
    driver.get(base_url)
    element = driver.find_element_by_tag_name("body")
    element.send_keys(Keys.ESCAPE)
    driver.implicitly_wait(1)

def teardown_module(module):
    driver.quit()

class TestVideoPlayer(object):
    def test_video_present(self):
        """Navigate to a video and make sure a Video is present"""
        self.driver.find_element_by_class_name("watch-button").click()
        assert self.driver.find_element_by_class_name("vice-player")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_class_name("")



class TestLocaleMenu(object):
    """Test's that elements appear in the locale menu."""
    def setup_class(cls):
        """Open the locale menu before starting the tests."""
        driver.find_element_by_class_name("current-locale").click()

