from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from assertlib import assertEqual, assertAtleast
import time
import unittest

base_url = "https://staging-noisey.viceops.net/en_us/topic/features"

class TestNoiseyFeatures(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://vice:welcome@staging-noisey.viceops.net")

    def test_escape_ad(self):
        """This Escapes out of the ad"""
        self.driver.get(base_url)
        element = self.driver.find_element_by_tag_name("body")
        element.send_keys(Keys.ESCAPE)
        self.driver.implicitly_wait(10)

    def test_logo_present_1(self):
        """Make sure Noisey logo is present"""
        assert self.driver.find_element_by_class_name("site-header__logo")

    def test_header_1(self):
        """Make sure a correct header is present"""
        assert self.driver.find_element_by_class_name("site-header")
        assertEqual("Latest features", self.driver.find_element_by_css_selector("div.section-header__wrapper__title").text)
        time.sleep(1)

    def test_locale_present_1(self):
        """Is the current locale name present?"""
        assert self.driver.find_element_by_class_name("current-locale__locale")
        time.sleep(1)

    def test_locale_dropdown_triangle_present_1(self):
        """Is the locale dropdown triangle present?"""
        assert self.driver.find_element_by_class_name("current-locale")
        self.driver.find_element_by_class_name("current-locale").click()
        time.sleep(1)

    def test_verify_topic_count_on_page(self):
        """Verifies there are 12 elements (topics) on first page."""
        assert len(self.driver.find_elements_by_class_name("grid__wrapper__card__topic")) == 12

    def test_verify_article_count_on_page(self):
        """Verifies there are 12 elements (articles) on first page."""
        assert len(self.driver.find_elements_by_class_name("grid__wrapper__card__thumbnail")) == 12

    def test_paginator_1(self):
        """Make sure paginator works (> : page 1->2), THREE statement options"""
        self.driver.find_elements_by_class_name("paginator__arrow")[2].click()

        #self.driver.find_element_by_xpath("//div[@id='V1C3']/div/div[4]/div/div/div/span[4]/p").click()

        # x = self.driver.find_elements_by_class_name("paginator-arrow")
        # x[2].click()
        time.sleep(1)

    def test_logo_present_2(self):
        """Noisey logo still present?"""
        assert self.driver.find_element_by_class_name("site-header__logo")
        time.sleep(1)

    def test_header_2(self):
        """Make sure a correct header is still present"""
        assert self.driver.find_element_by_class_name("site-header")
        assertEqual("Latest features", self.driver.find_element_by_css_selector("div.section-header__wrapper__title").text)
        time.sleep(1)

    def test_paginator_2(self):
        """Make sure paginator works (>> : page 2->607), THREE statement options"""
        self.driver.find_elements_by_class_name("paginator__arrow")[3].click()

        #self.driver.find_element_by_xpath("//div[@id='V1C3']/div/div[4]/div/div/div/span[4]/p").click()

        # x = self.driver.find_elements_by_class_name("paginator-arrow")
        # x[2].click()
        time.sleep(1)

    def test_logo_present_3(self):
        """Noisey logo still present?"""
        assert self.driver.find_element_by_class_name("site-header__logo")
        time.sleep(1)

    def test_header_3(self):
        """Make sure a correct header is still present"""
        assert self.driver.find_element_by_class_name("site-header")
        assertEqual("Latest features", self.driver.find_element_by_css_selector("div.section-header__wrapper__title").text)
        time.sleep(1)

    def test_paginator_3(self):
        """Make sure paginator works (< : page 607->606), THREE statement options"""
        self.driver.find_elements_by_class_name("paginator__arrow")[1].click()

        #self.driver.find_element_by_xpath("//div[@id='V1C3']/div/div[4]/div/div/div/span[4]/p").click()

        # x = self.driver.find_elements_by_class_name("paginator-arrow")
        # x[2].click()
        time.sleep(1)

    def test_logo_present_4(self):
        """Noisey logo still present?"""
        assert self.driver.find_element_by_class_name("site-header__logo")
        time.sleep(1)

    def test_header_4(self):
        """Make sure a correct header is still present"""
        assert self.driver.find_element_by_class_name("site-header")
        assertEqual("Latest features", self.driver.find_element_by_css_selector("div.section-header__wrapper__title").text)
        time.sleep(1)

    def test_paginator_4(self):
        """Make sure paginator works (<< : page 606->1), THREE statement options"""
        self.driver.find_elements_by_class_name("paginator__arrow")[0].click()

        #self.driver.find_element_by_xpath("//div[@id='V1C3']/div/div[4]/div/div/div/span[4]/p").click()

        # x = self.driver.find_elements_by_class_name("paginator-arrow")
        # x[2].click()
        time.sleep(1)

    def teardown_class(self):
        self.driver.quit()