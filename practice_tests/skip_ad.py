"""Update Homebrew once a week"""

#Console Usage::
    # py.test -s -v --tb=line test_noisey_ui.py

# -s: No capture. Don't suppress output.

# -v: Verbose. Gimme all the info.

# --tb=line: Shorten the tracebacks should an error occur.

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

#search dev tools console for element:
#ex. - document.getElementsByTagName('h6') and also document.getElementsByClassName('media')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from assertlib import assertEqual, assertAtleast
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from ..utils.exceptions import FunctionalError
#from ..utils.log import logger
import time
import unittest

base_url = "https://vice:welcome@staging-video.viceops.net/en_us"


class TestVideoFeatures(object):
    """This is what you're accomplishing with this group"""
    def setup_class(self):
        """This is what the setup needs to be"""
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        self.driver.get("https://vice:welcome@staging-video.viceops.net/en_us/video/guardian-angels-1/576c539277a2a2485d814464")

        # test
        def ad_countdown(self):
            """This is the precise ad countdown without skipping"""
            # add mute???
            self.driver.find_element_by_class_name("jw-slider-volume").click()
        # define
        def time_left(self):
            """Return the amount of time left"""
            try:
                t = int(self.driver.find_element_by_class_name("vp-ad-countdown-time").text.split(' ')[0])
                print "were in try, value is %s" % t
            except Exception:
                t = False
                print "were in exception, value is %s" % t
            return t
        # test
        def waiting_for_ad(self):
            while not self.time_left():
                try:
                    time_left = self.time_left()
                except Exception:
                    pass
            else:
                time.sleep(time_left + 1)

## TWO ADS IN A ROW??

    def test_video_controls(self):
            """Testing the video control panel"""
            # wait til ad is done playing (30 second ad is the max.)
            #time.sleep(5)
            control_menu = self.driver.find_element_by_class_name("jw-media")
            # hover over control menu
            hover = ActionChains(self.driver).move_to_element(control_menu)
            hover.perform()
            # click 30 second replay button
            thirty_seconds_back = self.driver.find_element_by_class_name("jw-icon-replay")
            # click pause
            pause = self.driver.find_element_by_class_name("jw-icon-playback")
            # click play
            play = self.driver.find_element_by_class_name("jw-icon-playback")
            # click CC
            cc = self.driver.find_element_by_class_name("jw-icon-cc").click()
            ActionChains(self.driver).move_to_element(control_menu).click(thirty_seconds_back).perform()
            time.sleep(1)
            ActionChains(self.driver).move_to_element(control_menu).click(cc).perform()
            time.sleep(1)
            ActionChains(self.driver).move_to_element(control_menu).click(pause).perform()
            time.sleep(1)
            ActionChains(self.driver).move_to_element(control_menu).click(play).perform()
            time.sleep(1)

    def teardown_class(self):
        self.driver.quit()