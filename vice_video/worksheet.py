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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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

    #def teardown_class(cls):
        #"""This is what you put if you're moving on to something different in another class"""
        #driver.find_element_by_class_name("TEST TEST").click()

## AD COUNT DOWN

    def time_left(self):
        """Return the amount of time left"""
        try:
            t = int(self.driver.find_element_by_class_name("vp-ad-countdown-time").text.split(' ')[0])
            print "were in try, value is %s" % t
        except Exception:
            t = False
            print "were in exception, value is %s" % t
        return t

    def test_waiting_for_ad(self):
        while not self.time_left():
            try:
                time_left = self.time_left()
            except Exception:
                pass
        else:
            time.sleep(time_left + 1)

###

    def initial_hover_(self):
            """Pair this anytime you initiate the video controls"""
            # wait til ad is done playing (30 second ad is the max.)
            control_menu = self.driver.find_element_by_class_name("jw-media")
            # hover over control menu
            hover = ActionChains(self.driver).move_to_element(control_menu)
            hover.perform()
###
### BEGIN WORKSHEET ###

    def _playlist_column2(self):
        """Test playlist 2 column"""

        # switch to tab 2
        self.driver.find_element_by_xpath("//ul[@id='playlists']/li[2]/label/span").click()

        # playlists-panel, is the panel present?
        assert self.driver.find_element_by_id("playlists-panel")
        # Are the playlists present?
        assert self.driver.find_element_by_id("playlists")

        # collapse / expand theatre-toggler
        self.driver.find_element_by_class_name("icon-collapse").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("icon-expand").click()

        # tab2 label
        assert self.driver.find_element_by_id("tab2")

        # tab2 content container
        assert self.driver.find_element_by_id("tab-content2")

        # tab2 scroll track
        assert self.driver.find_element_by_class_name("scroll-track")

        # tab2 list items
        items = self.driver.find_elements_by_class_name("list-item")
        for item in items:
            list = item
            print(list).text

        #parentElement = self.driver.find_element_by_class_name("scroll-track")
        #elementList = parentElement.find_elements_by_class_name("list-item")
        #list = elementList
        #print(list).text

        #parentElement = self.driver.find_element_by_class_name("scroll-track")
        #all_children_by_class_name = parentElement.find_element_by_class_name("list-item")
        #print '(all_children_by_class_name): ' + str(all_children_by_class_name)

        time.sleep(3)

    def playlist_column1(self):
        """Test playlist 2 column"""

        # switch to tab1
        self.driver.find_element_by_xpath("//ul[@id='playlists']/li[1]/label/span").click()

        # playlists-panel, is the panel present?
        assert self.driver.find_element_by_id("playlists-panel")
        # Are the playlists still present?
        assert self.driver.find_element_by_id("playlists")

        # collapse / expand theatre-toggler
        self.driver.find_element_by_class_name("icon-collapse").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("icon-expand").click()

        # tab1 label
        assert self.driver.find_element_by_id("tab1")

        #tab1 content container
        assert self.driver.find_element_by_id("tab-content1")

        # tab1 scroll track
        assert self.driver.find_element_by_class_name("scroll-track")

        # tab1 list items
        items = self.driver.find_elements_by_class_name("list-item")
        for item in items:
            list = item
            print(list).text

    def teardown_class(self):
            self.driver.quit()





### Examples for if/then ads

#TRY THIS KEEPING THE RESOLUTION MENU OPEN AND NAV BAR:

#def resolution_setup_method(self):
    """Ensures that the resolution menu is open before testing."""
    # We need to make sure the menu is open for all tests in this class.
    try:
        # what do you want to achieve?
        self.driver.find_element_by_class_name("navbar--open")
    except NoSuchElementException:
        # what do you need to do to achieve it?
        self.driver.find_element_by_class_name("jw-menu").click()


#def teardown_method(self):
    try:
        self.driver.find_element_by_class_name("navbar--open")
    except NoSuchElementException:
        self.driver.find_element_by_class_name("nav-toggle").click()

#

#def nav_bar_setup_method(self):
     """Ensures that the navigation bar is raised before testing."""
    # We need to make sure the nav is open for all tests in this class.
    try:
        # hover
        control_menu = self.driver.find_element_by_class_name("jw-media")
        hover = ActionChains(self.driver).move_to_element(control_menu)
        hover.perform()
    except NoSuchElementException:
        control_menu = self.driver.find_element_by_class_name("jw-media")
        hover = ActionChains(self.driver).move_to_element(control_menu)
        hover.perform()

#def teardown_method(self):
    try:
        # hover
        control_menu = self.driver.find_element_by_class_name("jw-media")
        hover = ActionChains(self.driver).move_to_element(control_menu)
        hover.perform()
    except NoSuchElementException:
        control_menu = self.driver.find_element_by_class_name("jw-media")
        hover = ActionChains(self.driver).move_to_element(control_menu)
        hover.perform()

###










### OLD SCRIPTING AND EXAMPLES ###

















    def close_tab(self):
        """KEEP THIS HERE - close tab"""
        self.driver.find_element_by_class_name("foo").click()
        # new tabs will be the last object in the window_handles list
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # < do stuff >
        # close the tab
        self.driver.close()
        # switch to the main window
        self.driver.switch_to.window(self.driver.window_handles[0])

#Old Scripting for no ad video.

    def video_player(self):
        """plays video (no ad)"""
        self.driver.find_element_by_class_name("jw-icon-playback").click()
        #or#
        #self.driver.find_element_by_class_name("vice-player").click()
        #"jw-playback" is the play/pause button.  You need the controlbar to be visible for this to toggle#
        time.sleep(32)
        #If you simply want to toggle play/pause you can do the 2 commands below:"
        self.driver.find_element_by_class_name("jw-state-playing").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("jw-state-paused").click()
        time.sleep(1)

#Old scripting for ad skipping.

        def ad_clickthrough_part1(self):
            """this clicks through the ad"""
            ## ADD DURATION TESTS!##
            time.sleep(2)
            advertisement = self.driver.find_element_by_class_name("vp-player-clicks")
            if advertisement.is_displayed():
                time.sleep(1)
                # click out (pauses video)
                self.driver.find_element_by_class_name("vp-player-clicks").click()
                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # close the tab
                self.driver.close()
                # switch to the main window
                self.driver.switch_to.window(self.driver.window_handles[0])
                # click play when you return from ad
                self.driver.find_element_by_class_name("jw-icon-playback").click()
                time.sleep(1)
                # test mute
                self.driver.find_element_by_class_name("jw-slider-volume").click()
                # wait rest of the ad out
                time.sleep(35)
                #
            else:
                advertisement.not_displayed()
                # proceed with test
                pass

        time.sleep(0)

#### Next to screen sizes



        def waiting_for_ad(self):
            advertisement = self.driver.find_element_by_class_name("vp-player-clicks")

            try:
                self.driver.implicitly_wait(1)
                self.driver.find_element_by_class_name("vp-player-clicks")
            except NoSuchElementException:
                pass
            else:
                raise FunctionalError("No ad present... moving on.")

##########

