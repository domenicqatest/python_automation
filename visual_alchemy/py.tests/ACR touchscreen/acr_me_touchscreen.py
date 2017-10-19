# -*- coding: utf-8 -*-

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from assertlib import assertEqual, assertAtleast, assertTrue, assertFalse
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import requests
import random
import time
import re

#base_url = "http://me-touchscreen.beta.visual-a.com/"
base_url = "http://localhost:8888/me-touchscreen/"

def setup_module(module):
    """The setup_module runs only one time."""

    # NOTE:
    # YOU MUST CLEAR THE JSON FILE ('/Applications/MAMP/htdocs/mod_touchscreen/analytics.json') AND ADD '[]' TO IT BEFORE RUNNING

    global driver
    driver = webdriver.Chrome()
    driver.set_window_size(1850, 1000)
    driver.get(base_url)
    # zoom in
    driver.execute_script("document.body.style.zoom='65%'")
    driver.implicitly_wait(10)

class TestModTouchscreen(object):

    def test_clicking_before(self):
        """Test randomly tapping the touchscreen video with the footer, BUT avoid the play button"""
        time.sleep(1)
        video = driver.find_element_by_id("bg-video")

        ac = ActionChains(driver)

        for x in range(100):

            x = random.randint(0,1810)
            if 210 <= x <= 1920:
                continue

            y = random.randint(0,684)
            if 680 <= y <= 910:
                continue

            coordinates = x, y

            el = driver.execute_script("arguments[0].click();", video)
            ac.move_to_element_with_offset(el, x, y)
            time.sleep(1)
            print "Coordinate checked:", coordinates

    def test_click_button(self):
        """Click the button to restart the video and hide the footer"""

        # verify button group location before clicking
        button_group1 = driver.find_element_by_class_name("buttons")
        assert driver.find_element_by_class_name("mi-wrapper")
        assert driver.find_element_by_class_name("cv-wrapper")

        print button_group1.location

        # click the MI button
        arrow = driver.find_element_by_class_name("mi")
        driver.execute_script("arguments[0].click();", arrow)
        assert driver.find_element_by_class_name("cv-text")
        time.sleep(3)

        # CV-TEXT IMAGE
        cv_text_file = open('utils/cv.txt', 'r').read()
        # this requests the data from the URL again
        cv_text_url = requests.get(
            "http://me-touchscreen.beta.visual-a.com/img/learn-about.png").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(cv_text_file, cv_text_url):
            print "cv-text does not match file"
        else:
            print "cv-text matches file"

        # size - cv-text
        cv_text = driver.find_element_by_class_name("cv-text")
        size = cv_text.size
        print('\n')  # adds line break
        print "size of the cv-text is:"
        print (size)

        assertEqual(cv_text.size["width"], 831)
        assertEqual(cv_text.size["height"], 215)

        # location - cv-text
        print('\n')  # adds line break
        print "location of the cv-text is at:"
        print (cv_text.location)

        assertEqual(cv_text.location, {"y": 689.0, "x": 3010.0})

        # click the CV button 10 times to try and break it in this state - #2
        for x in range(10):
            cv = driver.find_element_by_class_name("cv")
            mi = driver.find_element_by_class_name("mi")
            driver.execute_script("arguments[0].click();", cv)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", mi)
            time.sleep(1)

        # verify hotspot works and you can see the footer again
        hotspot = driver.find_element_by_class_name("hotspot")

        # size - hotspot
        size = hotspot.size
        print('\n')  # adds line break
        print "size of the hotspot is:"
        print (size)

        assertEqual(hotspot.size["width"], 100)
        assertEqual(hotspot.size["height"], 100)

        # location - hotspot
        print('\n')  # adds line break
        print "location of the hotspot is at:"
        print (hotspot.location)

        assertEqual(hotspot.location, {"y": 0.0, "x": 1820.0})

        driver.execute_script("arguments[0].click();", hotspot)
        time.sleep(3)

        # verify footer is back
        footer =  driver.find_element_by_xpath("/html/body/div[2]/div[2]/div")
        assert footer
        if footer.is_displayed():
            print('\n')  # adds line break
            print "Footer is present"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("Footer is NOT present")

        # click the CV_button - #1
        arrow = driver.find_element_by_class_name("cv")
        driver.execute_script("arguments[0].click();", arrow)
        time.sleep(3)
        assert driver.find_element_by_class_name("mi-text")

        # CV-TEXT IMAGE
        mi_text_file = open('utils/mi.txt', 'r').read()
        # this requests the data from the URL again
        mi_text_url = requests.get(
            "http://me-touchscreen.beta.visual-a.com/img/explore-the-rounded.png").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(mi_text_file, mi_text_url):
            print "mi-text does not match file"
        else:
            print "mi-text matches file"

        # size - mi-text
        mi_text = driver.find_element_by_class_name("mi-text")
        size = mi_text.size
        print('\n')  # adds line break
        print "size of the mi-text is:"
        print (size)

        assertEqual(mi_text.size["width"], 1155)
        assertEqual(mi_text.size["height"], 215)

        # location - mi-text
        print('\n')  # adds line break
        print "location of the mi-text is at:"
        print (mi_text.location)

        assertEqual(mi_text.location, {"y": 689.0, "x": 2144.0})

        # click the MI button 10 times to try and break it in this state - #2
        for x in range(10):
            cv = driver.find_element_by_class_name("cv")
            mi = driver.find_element_by_class_name("mi")
            driver.execute_script("arguments[0].click();", mi)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", cv)
            time.sleep(1)

        # verify hotspot works and you can see the footer again
        hotspot = driver.find_element_by_class_name("hotspot")

        # location - hotspot
        size = hotspot.size
        print('\n')  # adds line break
        print "size of the hotspot is:"
        print (size)

        assertEqual(hotspot.size["width"], 100)
        assertEqual(hotspot.size["height"], 100)

        # size - hotspot
        print('\n')  # adds line break
        print "location of the hotspot is at:"
        print (hotspot.location)

        assertEqual(hotspot.location, {"y": 0.0, "x": 1820.0})

        driver.execute_script("arguments[0].click();", hotspot)
        time.sleep(3)

        # verify footer is back
        footer =  driver.find_element_by_xpath("/html/body/div[2]/div[2]/div")
        if footer.is_displayed():
            print('\n')  # adds line break
            print "Footer is present"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("Footer is NOT present")

    def test_clicking_mi_after(self):
        """Test randomly tapping the touchscreen video now that the footer is gone, BUT avoid the play button"""
        mi = driver.find_element_by_class_name("mi")
        driver.execute_script("arguments[0].click();", mi)
        # we're now on the mi video... so we're going to focus on the not clicking the cv play button
        time.sleep(5)
        video = driver.find_element_by_id("video")
        ac = ActionChains(driver)

        for x in range(10):

            x = random.randint(0,1810)
            if 1412 <= x <= 1926:
                continue

            y = random.randint(0,780)
            if 943 <= y <= 1083:
                continue

            coordinates = x,y

            el = driver.execute_script("arguments[0].click();", video)
            ac.move_to_element_with_offset(el, x, y)
            time.sleep(1)
            print "Coordinate checked:", coordinates

    def test_clicking_cv_after(self):
        """Test randomly tapping the touchscreen video now that the footer is gone, BUT avoid the play button"""
        cv = driver.find_element_by_class_name("cv")
        driver.execute_script("arguments[0].click();", cv)
        # we're now on the cv video... so we're going to focus on the not clicking the mi play button
        time.sleep(5)
        video = driver.find_element_by_id("video")
        ac = ActionChains(driver)

        for x in range(10):

            x = random.randint(0, 1810)
            if 1310 <= x <= 1926:
                continue

            y = random.randint(0, 780)
            if 943 <= y <= 1083:
                continue

            coordinates = x, y

            el = driver.execute_script("arguments[0].click();", video)
            ac.move_to_element_with_offset(el, x, y)
            time.sleep(1)
            print "Coordinate checked:", coordinates

    def test_footer_visible1(self):
        """After 3:30 minutes of the CV, is the footer visible again?"""
        print "Waiting 3:15 minutes for footer to reappear..."
        # we're now on the cv video waiting for the footer
        time_left = 195 #seconds = # minutes
        while time_left > 0:
            print(time_left)
            time.sleep(1)
            time_left = time_left - 1

        footer =  driver.find_element_by_xpath("/html/body/div[2]/div[2]/div")
        if footer.is_displayed():
            print('\n')  # adds line break
            print "Is the footer visible? : ", (footer.is_enabled())

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("Footer is NOT present")


    def test_footer_visible2(self):
        """After 3:30 minutes if the MI, is the footer visible again?"""
        # click the MI button
        mi = driver.find_element_by_class_name("mi")
        driver.execute_script("arguments[0].click();", mi)
        # we're now on the mi video waiting for the footer
        print "Waiting 3:25 minutes for footer to reappear..."

        time_left = 205 #seconds = # minutes
        while time_left > 0:
            print(time_left)
            time.sleep(1)
            time_left = time_left - 1

        footer =  driver.find_element_by_xpath("/html/body/div[2]/div[2]/div")
        if footer.is_displayed():
            print('\n')  # adds line break
            print "Is the footer visible? : ", (footer.is_enabled())

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("Footer is NOT present")

    def test_footer_attributes(self):
        """Test the footer attributes"""

        footer =  driver.find_element_by_xpath("/html/body/div[2]/div[2]/div")
        # size
        size = footer.size
        print('\n')  # adds line break
        print "size of the footer is:"
        print (size)

        assertEqual(footer.size["width"], 1920)
        assertEqual(footer.size["height"], 215)

        # location
        print('\n')  # adds line break
        print "location of footer is at:"
        print (footer.location)

        assertEqual(footer.location, {"y": 689.0, "x": 0.0})

        # footer image
        footer_file = open('utils/footer_image.txt', 'r').read()
        # this requests the data from the URL again
        footer_url = requests.get("http://me-touchscreen.beta.visual-a.com/img/footer.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(footer_file, footer_url):
            pass
        print "Footer matches what's on file"

    def test_button_group_attributes(self):
        """Test the button group attributes"""

        # size - mi white area
        white_area = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/img[1]")
        size = white_area.size
        print('\n')  # adds line break
        print "size of the white area is:"
        print (size)

        assertEqual(white_area.size["width"], 178)
        assertEqual(white_area.size["height"], 177)

        # location - mi white area
        print('\n')  # adds line break
        print "location of white area is at:"
        print (white_area.location)

        assertEqual(white_area.location, {"y": 715.0, "x": 314.0})

        # mi white area image
        white_area_file = open('utils/white-circle-big.txt', 'r').read()
        # this requests the data from the URL again
        white_area_url = requests.get("http://me-touchscreen.beta.visual-a.com/img/white-circle-big.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(white_area_file, white_area_url):
            pass
        print "White area matches what's on file"

        # size - cv white area
        white_area2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/img[1]")
        size = white_area2.size
        print('\n')  # adds line break
        print "size of the white area is:"
        print (size)

        assertEqual(white_area2.size["width"], 178)
        assertEqual(white_area2.size["height"], 177)

        # location - cv white area
        print('\n')  # adds line break
        print "location of white area is at:"
        print (white_area2.location)

        assertEqual(white_area2.location, {"y": 715.0, "x": 1180.0})

        # size - mi gps ring
        ring = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div")
        print('\n')  # adds line break
        print ring.size

        width = ring.size["width"]
        if 15 <= width <= 210:
            print('\n')  # adds line break
            print "GPS Ring is in animation SIZE range"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of SIZE range")

        height = ring.size["height"]
        if 15 <= height <= 210:
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of SIZE range")

        # is the animation running correctly?
        assertEqual(ring.value_of_css_property("animation-play-state"), 'running')
        assertEqual(ring.value_of_css_property("animation-duration"), '4s')
        assertEqual(ring.value_of_css_property("animation-direction"), 'normal')
        assertEqual(ring.value_of_css_property("animation-delay"), '0s')
        assertEqual(ring.value_of_css_property("animation-iteration-count"), 'infinite')
        assertEqual(ring.value_of_css_property("animation-timing-function"), 'ease-out')

        # location - gps ring
        print('\n')  # adds line break
        print "location of GPS Ring is at:"
        print (ring.location)

        y = ring.location['y']
        if 695 <= y <= 1003:
            print('\n')  # adds line break
            print "GPS Ring is in animation LOCATION range"
            pass

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of LOCATION range")

        x = ring.location['x']
        if 290 <= x <= 2295:
            print('\n')  # adds line break
            print "GPS Ring is in animation LOCATION range"
            pass

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of LOCATION range")

        # size - cv gps ring
        ring2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div")
        print('\n')  # adds line break
        print ring2.size

        width = ring2.size["width"]
        if 87 <= width <= 210:
            print('\n')  # adds line break
            print "GPS Ring is in animation SIZE range"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of SIZE range")

        height = ring2.size["height"]
        if 87 <= height <= 210:
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of SIZE range")

        # is the animation running correctly?
        assertEqual(ring2.value_of_css_property("animation-play-state"), 'running')
        assertEqual(ring2.value_of_css_property("animation-duration"), '4s')
        assertEqual(ring2.value_of_css_property("animation-direction"), 'normal')
        assertEqual(ring2.value_of_css_property("animation-delay"), '0s')
        assertEqual(ring2.value_of_css_property("animation-iteration-count"), 'infinite')
        assertEqual(ring2.value_of_css_property("animation-timing-function"), 'ease-out')

        # location - gps ring
        print('\n')  # adds line break
        print "location of GPS Ring2 is at:"
        print (ring2.location)

        y = ring2.location['y']
        if 700 <= y <= 1003:
            print('\n')  # adds line break
            print "GPS Ring2 is in animation LOCATION range"
            pass

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of LOCATION range")

        x = ring2.location['x']
        if 335 <= x <= 3100:
            print('\n')  # adds line break
            print "GPS Ring is in animation LOCATION range"
            pass

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of LOCATION range")

        # size - mi round circle
        round_circle = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/img[3]")
        size = round_circle.size
        print('\n')  # adds line break
        print "size of the round circle is:"
        print (size)

        assertEqual(round_circle.size["width"], 129)
        assertEqual(round_circle.size["height"], 120)

        # location - mi round circle
        print('\n')  # adds line break
        print "location of round circle is at:"
        print (round_circle.location)

        assertEqual(round_circle.location, {"y": 736.0, "x": 333.0})

        round_file = open('utils/round-circle-big.txt', 'r').read()
        # this requests the data from the URL again
        round_url = requests.get("http://me-touchscreen.beta.visual-a.com/img/round-circle-big.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(round_file, round_url):
            pass
        print "Round arrow matches what's on file"

        # size - cv round circle
        round_circle2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/img[2]")
        size = round_circle2.size
        print('\n')  # adds line break
        print "size of the round circle is:"
        print (size)

        assertEqual(round_circle2.size["width"], 129)
        assertEqual(round_circle2.size["height"], 120)

        # location - cv round circle
        print('\n')  # adds line break
        print "location of round circle is at:"
        print (round_circle2.location)

        assertEqual(round_circle2.location, {"y": 736.0, "x": 1199.0})

        # size - mi arrow
        arrow = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/img[2]")
        size = arrow.size
        print('\n')  # adds line break
        print "size of the arrow is:"
        print (size)

        assertEqual(arrow.size["width"], 32)
        assertEqual(arrow.size["height"], 45)

        # location - mi arrow
        print('\n')  # adds line break
        print "location of arrow is at:"
        print (arrow.location)

        assertEqual(arrow.location, {"y": 770.0, "x": 378.0})

        # arrow mi image
        arrow_file = open('utils/me_arrow_image.txt', 'r').read()
        # this requests the data from the URL again
        arrow_url = requests.get("http://me-touchscreen.beta.visual-a.com/img/arrow-big.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(arrow_file, arrow_url):
            pass
        print "Arrow matches what's on file"

        # size - cv arrow
        arrow2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/img[3]")
        size = arrow2.size
        print('\n')  # adds line break
        print "size of the arrow is:"
        print (size)

        assertEqual(arrow2.size["width"], 32)
        assertEqual(arrow2.size["height"], 45)

        # location - cv arrow
        print('\n')  # adds line break
        print "location of arrow is at:"
        print (arrow2.location)

        assertEqual(arrow2.location, {"y": 770.0, "x": 1244.0})

    def test_break_button(self):
        """Try to break the play button and hotspot by clicking multiple times"""

        # click triangle multiple times to try and break - #4
        for x in range(10):
            cv = driver.find_element_by_class_name("cv")
            mi = driver.find_element_by_class_name("mi")
            driver.execute_script("arguments[0].click();", mi)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", cv)
            time.sleep(1)

        for x in range(10):
        # click gps ring multiple times to try and break - #7
            ring = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div")
            driver.execute_script("arguments[0].click();", ring)
            time.sleep(1)

        # gps ring attributes
            assertEqual(ring.value_of_css_property("border-bottom-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring.value_of_css_property("border-left-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring.value_of_css_property("border-right-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring.value_of_css_property("border-top-color"), 'rgba(255, 255, 255, 1)')

        # gps ring2 attributes
        for x in range(10):
        # click gps ring multiple times to try and break - #7
            ring2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div")
            driver.execute_script("arguments[0].click();", ring2)
            time.sleep(1)

        # gps ring attributes
            assertEqual(ring2.value_of_css_property("border-bottom-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring2.value_of_css_property("border-left-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring2.value_of_css_property("border-right-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring2.value_of_css_property("border-top-color"), 'rgba(255, 255, 255, 1)')

        for x in range(10):
        # click hotspot multiple
        # times to try and break - won't count towards analytics
            hotspot = driver.find_element_by_class_name("hotspot")
            driver.execute_script("arguments[0].click();", hotspot)
            time.sleep(1)

    def test_pull_analytics(self):
        """This will pull the analytics from the file(s)"""
        # read text file
        analytics_json_file = open('/Applications/MAMP/htdocs/me-touchscreen/analytics.json', 'r').read()

        print('\n')  # adds line break
        print "Analytics JSON:"
        # compare the number of restarts in the file with the number is should be
        restart = "start"
        # the total number of analytics calls should match the number of button clicks = 65

        pattern = re.compile(format(restart), re.I)  # case insensitive
        num = len(pattern.findall(analytics_json_file))

        if assertEqual(num, 65):
            print('\n')  # adds line break
            print "Restart analytic entries in JSON file match number of clicks"
            pass

        # compare the number of fullVideoWatched in the file with the number is should be
        completed = "completed"
        # the total number of analytics calls should match the number of button clicks = 2

        pattern2 = re.compile(format(completed), re.I)  # case insensitive
        num2 = len(pattern2.findall(analytics_json_file))

        if assertEqual(num2, 2):
            print('\n')  # adds line break
            print "fullVideoWatched analytic entries in JSON file match number of clicks"
            pass

    def teardown_class(self):
        driver.quit()