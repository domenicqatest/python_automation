"""USE THIS AS AN ADD CLASS WORKSHEET"""

"""Load Python Console"""
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("http://google.com")

# search dev tools console for element:
# ex. - document.getElementsByTagName('h6') and also document.getElementsByClassName('media')

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from assertlib import assertEqual, assertAtleast
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from ..utils.exceptions import FunctionalError
import time
import unittest

base_url = "https://vice:welcome@staging-video.viceops.net"
# base_url = "https://video.vice.com/en_us"

def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the full page
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    driver.get(base_url)
    element = driver.find_element_by_tag_name("body")
    element.send_keys(Keys.ESCAPE)
    driver.implicitly_wait(1)

def teardown_module(module):
    driver.quit()

class TestLedeTopNav(object):
    def test_escape_ad(self):
        """This Escapes out of the ad"""
        driver.get(base_url)
        element = driver.find_element_by_tag_name("body")
        element.send_keys(Keys.ESCAPE)
        driver.implicitly_wait(5)

    def test_logo_present(self):
        """Make sure Video logo and entire nav menue is present"""
        assert driver.find_element_by_id("Ebene_1")
        driver.find_element_by_id("Ebene_1").click()
        time.sleep(1)
        assert driver.find_element_by_class_name("site-menu")
        assert driver.find_element_by_class_name("network-bar")

    def test_vice_home(self):
        """Click Vice.com Home CTA and come back"""
        driver.find_element_by_class_name("cta").click()
        driver.get(base_url)

    def test_lede_video(self):
        """"Test the lede video playback"""
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div[1]/div/div/a[2]/div[2]/div/i").click()
        driver.get(base_url)

    def test_search(self):
        """Test search"""
        term = "Action Bronson"
        driver.find_element_by_class_name("desktop-search").click()
        time.sleep(1)
        driver.find_element_by_class_name("search-query").send_keys(term)
        driver.find_element_by_class_name("search-query").send_keys(Keys.RETURN)
        time.sleep(1)

    def test_accurate_search_results(self):
        driver.find_elements_by_xpath("//*[contains(text(), 'action bronson')]")
        driver.get(base_url)
        time.sleep(1)

    def test_navigation_bar_right(self):
        """Test all parts of The Vice Network dropdown"""
        assert driver.find_element_by_class_name("the-vice-network")
        assert driver.find_element_by_class_name("arr")
        assert driver.find_element_by_class_name("close")
        time.sleep(1)

    def dropdown_items(self):
        """Test all items in The Vice Network dropdown are present"""

    def test_lede_image_present(self):
        """Test that the lede image or player is present and clicks through"""
        assert driver.find_element_by_class_name("fmv-container")
        driver.find_element_by_class_name("fmv-container").click()
        driver.get(base_url)
        time.sleep(3)

    def test_lede_slider(self):
        """Test that the slider works on both sides"""
        driver.find_elements_by_class_name("icon-carousel-arrow")[0].click()
        driver.find_elements_by_class_name("icon-carousel-arrow")[0].click()
        driver.find_elements_by_class_name("icon-carousel-arrow")[0].click()
        driver.find_elements_by_class_name("icon-carousel-arrow")[1].click()
        driver.find_elements_by_class_name("icon-carousel-arrow")[1].click()
        driver.find_elements_by_class_name("icon-carousel-arrow")[1].click()

    def test_lede_player_elements_present(self):
        """Test that the label, title, and play button are present"""
        assert driver.find_element_by_class_name("slide-label")
        assert driver.find_element_by_class_name("slide-title")
        assert driver.find_element_by_class_name("slide-cta")

class TestCategoryAreas(object):
    def test_slider_title_1(self):
        """Make sure the category 3 slider titles are present"""
        assert driver.find_elements_by_class_name("slider-title")[0 - 2]

    def test_entry_title_1(self):
        """Make sure the 78 entry titles (including the 12 visible ones) are present"""
        assert driver.find_elements_by_class_name("entry-title")[0 - 77]

    def test_entry_subtitle_1(self):
        """Make sure the 78 entry subtitles (including the 12 visible ones) are present"""
        assert driver.find_elements_by_class_name("entry-subtitle")[0 - 52]
        time.sleep(1)

    def test_media_videos(self):
        """Make sure the 104 'media' items (including video thumbs) are present"""
        assert driver.find_elements_by_class_name("media")[0 - 24]
        time.sleep(1)

    def test_video_click_throughs(self):
        """Test Latest, Trending, and Recommended video click-throughs"""
        driver.find_element_by_xpath("//div[@id='app']/div[3]/div/div/div/article[5]/a/div/div[1]/img").click()
        driver.get(base_url)
        driver.find_element_by_xpath("//div[@id='app']/div[4]/div/div/div/article[5]/a/div/div[1]/img").click()
        driver.get(base_url)
        driver.find_element_by_xpath("//div[@id='app']/div[5]/div/div/div/article[5]/a/div/div/img").click()
        driver.get(base_url)

    def teardown_class(self):
        driver.quit()

#   def setup_method(method):
#   def teardown_method(method):

#   def setup_class(cls):
#   def teardown_class(cls):