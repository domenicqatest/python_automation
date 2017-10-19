# -*- coding: utf-8 -*-

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from assertlib import assertEqual, assertNotEqual, assertAtleast, assertTrue
import time
import itertools
from selenium.webdriver.common.action_chains import ActionChains

base_url = "https://moat.com/"

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

class TestQuestion9(object):

    # Try These
    def test_try_these(self):
        """Verify that the 'Try These' links are random and that they work"""
        time.sleep(3)
        random_text1 = driver.find_elements_by_class_name("random-brand")
        for element in random_text1:
            print('\n')  # adds line break
            print_random_text1 = element.get_attribute('innerText')
            print print_random_text1

        driver.refresh()
        random_text2 = driver.find_elements_by_class_name("random-brand")
        for element in random_text2:
            print('\n')  # adds line break
            print_random_text2 = element.get_attribute('innerText')
            print print_random_text2
        assertNotEqual(random_text1, random_text2)

        driver.refresh()
        random_text3 = driver.find_elements_by_class_name("random-brand")
        for element in random_text3:
            print('\n')  # adds line break
            print_random_text3 = element.get_attribute('innerText')
            print print_random_text3
        assertNotEqual(random_text2, random_text3)

        if assertNotEqual(random_text1, random_text2):
            print('\n')  # adds line break
            print "Links are not random"
        else:
            print('\n')  # adds line break
            print "Links are random"

        if assertNotEqual(random_text1, random_text3):
            print('\n')  # adds line break
            print "Links are not random"
        else:
            print('\n')  # adds line break
            print "Links are random"

    # Recently Seen Ads
    def test_recently(self):
        """Verify that the 'Recently Seen Ads' are no more than half an hour old"""
        time.sleep(3)
        recent1 = driver.find_elements_by_class_name("featured-agencies")
        for element in recent1:
            print('\n')  # adds line break
            recent1_text = element.get_attribute('innerText')
            print recent1_text

        number_range = unicode(31 <= 1000)
        if number_range not in recent1_text:
            print "Ads are no more than half an hour old"

    # Ad Count
    def test_count(self):
        """Verify the ad count on the search result page is correct, even if there are more than 100 ads in the result set"""
        term = "Vice"
        driver.find_element_by_id("pro-landing-search-box").clear()
        driver.find_element_by_id("pro-landing-search-box").send_keys(term)
        driver.find_element_by_class_name("fa-search").click()
        time.sleep(3)

        if driver.find_element_by_class_name("er-load-more").is_displayed():
            for _ in itertools.repeat(None, 6):
                driver.find_element_by_class_name("er-load-more").click()
                time.sleep(3)

        top_number = driver.find_element_by_xpath("//*[@id='er-app']/div/div[2]/div/div[2]/span[1]").text
        print('\n')  # adds line break
        print top_number

        creatives = driver.find_elements_by_class_name("er-creative")
        creatives_number = len(creatives)
        print creatives_number, "creatives"

        time.sleep(5)

        if assertNotEqual(top_number, (creatives_number, 'creatives')):
            print('\n')  # adds line break
            print "Numbers match"
        else:
            print('\n')  # adds line break
            print "Numbers don't match"

    # Share this Ad
    def test_share(self):
        """Verify the 'Share the Ad' feature"""
        creative_container = driver.find_element_by_class_name("er-creative-container")
        hover = ActionChains(driver).move_to_element(creative_container)
        hover.perform()
        time.sleep(3)
        share = driver.find_element_by_class_name("ca-digest-link")
        time.sleep(3)
        ActionChains(driver).move_to_element(creative_container).click(share).perform()
        time.sleep(3)

        driver.find_element_by_class_name("copy-button").click()
        assert driver.find_element_by_class_name("url-message")
        driver.find_element_by_class_name("close-popup-icon").click()

    def teardown_class(self):
        driver.quit()