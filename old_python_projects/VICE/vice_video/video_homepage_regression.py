from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from assertlib import assertEqual, assertAtleast
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from ..utils.log import logger
import time
import unittest

base_url = "https://vice:welcome@staging-video.viceops.net"
#base_url = "https://video.vice.com/en_us"

def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the full page
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    driver.set_window_size(1280, 800)
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
        driver.find_element_by_class_name("carousel").click()
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

class TestPlaylists(object):
    def test_playlist_click_throughs(self):
        """Make sure all thumbs are present / Test 1 video in the 4 playlist sections"""
        assert driver.find_element_by_class_name("entry-thumb")
        driver.find_element_by_xpath("//div[@id='app']/div[3]/div/div/div/article[5]/a/div/div[3]/div[1]").click()
        driver.get(base_url)
        driver.find_element_by_xpath("//div[@id='app']/div[4]/div/div/div/article[5]/a/div/div[3]/div[1]").click()
        driver.get(base_url)
        driver.find_element_by_xpath("//div[@id='app']/div[5]/div/div/div/article[5]/a/div/div").click()
        driver.get(base_url)
        driver.find_element_by_xpath("//div[@id='collection-']/div/a[1]/div").click()
        driver.get(base_url)
        assert driver.find_elements_by_class_name("playlist-item")[0 - 2]
        driver.find_element_by_xpath("//div[@id='collection-']/div/a[1]").click()
        driver.get(base_url)
        driver.find_element_by_css_selector("div.collection-cta > i.icon-arrow-right").click()
        driver.get(base_url)
        driver.find_element_by_css_selector("div.collection-watch > span").click()
        driver.get(base_url)
        driver.find_element_by_css_selector("div.collection-cta-container").click()
        driver.get(base_url)
        #driver.find_element_by_link_text("9 Videos in Playlist").click()
        driver.get(base_url)
        driver.find_element_by_xpath("(//div[@id='collection-']/a/div[2]/div/div/i)[2]").click()
        driver.get(base_url)
        driver.find_element_by_xpath("(//div[@id='collection-']/a/div[2]/div/div[2])[3]").click()
        driver.get(base_url)
        # driver.find_element_by_xpath("(//div[@id='collection-']/a/div)[3]").click()
        driver.get(base_url)
        # driver.find_element_by_link_text("11 Videos in Playlist").click()
        driver.get(base_url)
        driver.find_element_by_xpath("(//div[@id='collection-']/a/div[2]/div/div/i)[3]").click()
        driver.get(base_url)
        driver.find_element_by_xpath("(//div[@id='collection-']/a/div[2]/div/div[2])[3]").click()
        driver.get(base_url)
        # driver.find_element_by_xpath("(//div[@id='collection-']/a/div)[5]").click()
        driver.get(base_url)
        # driver.find_element_by_link_text("24 Videos in Playlist").click()
        driver.get(base_url)

    def test_playlist_title_elements(self):
        """Test playlist title elements - h4/11, h6/39"""
        assert driver.find_elements_by_tag_name('h4')[0 - 11]
        assert driver.find_elements_by_tag_name('h6')[0 - 39]

class TestCategorySliders(object):
    def test_category_slider(self):
        """Test that the slider works for Latest, Trending, and Recommended"""
        time.sleep(3)
        driver.find_elements_by_class_name("slick-next")[0].click()
        #assert self.driver.find_elements_by_class_name("slick-active")
        #time.sleep(3)  Figure out how to verify that a a slide is active.
        driver.find_elements_by_class_name("slick-next")[0].click()
        time.sleep(1)
        driver.find_elements_by_class_name("slick-prev")[0].click()
        driver.find_elements_by_class_name("slick-prev")[0].click()
        driver.find_elements_by_class_name("slick-next")[1].click()
        driver.find_elements_by_class_name("slick-next")[1].click()
        time.sleep(1)
        driver.find_elements_by_class_name("slick-prev")[1].click()
        driver.find_elements_by_class_name("slick-prev")[1].click()
        driver.find_elements_by_class_name("slick-next")[2].click()
        driver.find_elements_by_class_name("slick-next")[2].click()
        time.sleep(1)
        driver.find_elements_by_class_name("slick-prev")[2].click()
        driver.find_elements_by_class_name("slick-prev")[2].click()

class TestTopNavDropdowns(object):
    def test_browse_dropdown(self):
        """Test all parts of the Browse dropdown"""
        assert driver.find_elements_by_class_name("icon-arrow-right")[0 - 1]
        driver.find_element_by_class_name("browse").click()
        assert driver.find_elements_by_class_name("dropdown-menu")[0 - 1]
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[1]/li[1]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[1]/li[2]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[1]/li[4]/a").click()
        time.sleep(3)
        driver.get(base_url)
        time.sleep(3)
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[1]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[2]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[3]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[4]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[5]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[6]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[7]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[8]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[9]/a").click()
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[2]/li[10]/a").click()

    def test_channels_dropdown(self):
        """Test all parts of the Channels dropdown"""
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[1]/li[1]/a").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[1]/li[2]/a").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[1]/li[3]/a").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[1]/li[4]/a").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[1]/li[5]/a").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[1]/li[6]/a").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[2]/li[1]/a/i").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[2]/li[2]/a/i").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[2]/li[3]/a/i").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[2]/li[4]/a/i").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[2]/li[5]/a").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[2]/div/div/ul[2]/li[6]/a").click()

class TestFooterLinks(object):
    def test_footer_links(self):
        """Test the elements and links in the footer"""
        driver.get(base_url)
        assert driver.find_element_by_class_name("main-footer")
        assert driver.find_element_by_class_name("footer-internal")
        assert driver.find_element_by_class_name("footer-left")
        assert driver.find_element_by_class_name("footer-right")
        assert driver.find_element_by_class_name("footer-corp")
        assert driver.find_element_by_class_name("footer-heading")
        assert driver.find_element_by_class_name("footer-video-topics")

class TestClickOutLinks(object):
    def test_hbo_clickout(self):
        """This will test the clickout until we figure out how to close tab properly"""
        driver.find_element_by_class_name("browse").click()
        assert driver.find_element_by_class_name("dropdown-menu")
        driver.find_element_by_xpath("//div[@id='app']/nav/ul[2]/li[1]/div/div/ul[1]/li[3]/a").click()
        driver.switch_to_default_content()

    def test_footer_watch_social(self):
        """Test the footer, watch random, and social"""
        driver.find_element_by_class_name("watch-button").click()
        driver.get(base_url)
        driver.find_element_by_css_selector("i.icon-facebook").click()
        driver.find_element_by_css_selector("i.icon-twitter").click()
        driver.find_element_by_css_selector("i.icon-email").click()

    def teardown_class(self):
        driver.quit()

#   def setup_method(method):
#   def teardown_method(method):

#   def setup_class(cls):
#   def teardown_class(cls):