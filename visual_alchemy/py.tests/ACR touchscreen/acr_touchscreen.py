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

#base_url = "http://mod-touchscreen.beta.visual-a.com/"
base_url = "http://localhost:8888/mod_touchscreen/"

def setup_module(module):
    """The setup_module runs only one time."""

    # NOTE:
    # YOU MUST CLEAR THE JSON FILE ('/Applications/MAMP/htdocs/mod_touchscreen/analytics.json') AND ADD '[]' TO IT BEFORE RUNNING

    global driver
    driver = webdriver.Chrome()
    driver.set_window_size(1850, 1000)
    driver.get(base_url)
    # zoom in
    driver.execute_script("document.body.style.zoom='75%'")
    driver.implicitly_wait(10)

class TestModTouchscreen(object):

    def test_clicking_before(self):
        """Test randomly tapping the touchscreen video with the footer, BUT avoid the play button"""
        time.sleep(1)
        video = driver.find_element_by_id("video")

        ac = ActionChains(driver)

        for x in range(1):

            x = random.randint(0,1810)
            if 1189 <= x <= 1329:
                continue

            y = random.randint(0,780)
            if 767 <= y <= 907:
                continue

            coordinates = x, y

            el = driver.execute_script("arguments[0].click();", video)
            ac.move_to_element_with_offset(el, x, y)
            time.sleep(1)
            print "Coordinate checked:", coordinates

    def test_click_button1(self):
        """Click the button to restart the video and hide the footer"""

        # verify button group location before clicking
        button_group1 = driver.find_element_by_class_name("button-group")
        print button_group1.location

        # click the button - #1
        arrow = driver.find_element_by_class_name("arrow")
        driver.execute_script("arguments[0].click();", arrow)
        time.sleep(3)

        # click the button 10 times to try and break it in this state - #2
        for x in range(10):
            arrow = driver.find_element_by_class_name("arrow")
            driver.execute_script("arguments[0].click();", arrow)
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
        footer = driver.find_element_by_class_name("footer")

        # FOOTER IMAGE
        footer_file = open('utils/footer.txt', 'r').read()
        # this requests the data from the URL again
        footer_url = requests.get(
            "http://mod-touchscreen.beta.visual-a.com/img/footer.png").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(footer_file, footer_url):
            print "footer does not match file"
        else:
            print "footer matches file"

        if footer.is_displayed():
            print('\n')  # adds line break
            print "Footer is present"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("Footer is NOT present")

        # click the button and proceed - #3
        arrow = driver.find_element_by_class_name("arrow")
        driver.execute_script("arguments[0].click();", arrow)
        time.sleep(1)

        # verify footer is gone for 5 minutes
        if footer.is_displayed():
            print('\n')  # adds line break
            raise NoSuchElementException("Footer should NOT be present")

        else:
            print('\n')  # adds line break
            print "Footer is NOT present, proceeding with clicks..."

        # verify button group location after clicking
        button_group2 = driver.find_element_by_class_name("button-group")
        print button_group2.location

        # verify they are not the same
        if ({'y': 782.0, 'x': 1171.0}, button_group2.location): #bg1 = {'y': 782.0, 'x': 1171.0} / bg2 = {'y': 1128.0, 'x': 1171.0}
            print "Locations are different... proceeding"
            pass
        else:
            raise NoSuchElementException("The locations should NOT be the same")

    def test_clicking_after(self):
        """Test randomly tapping the touchscreen video now that the footer is gone, BUT avoid the play button"""
        time.sleep(5)
        video = driver.find_element_by_id("video")
        ac = ActionChains(driver)

        for x in range(1):

            x = random.randint(0,1810)##### Does this need updated???
            if 1779 <= x <= 1919:
                continue

            y = random.randint(0,780)
            if 943 <= y <= 1083:
                continue

            coordinates = x,y

            el = driver.execute_script("arguments[0].click();", video)
            ac.move_to_element_with_offset(el, x, y)
            time.sleep(1)
            print "Coordinate checked:", coordinates

    def test_footer_visible(self):
        """After 4:30 minutes, is the footer visible again?"""
        print "Waiting 4:30 minutes for footer to reappear..."

        time_left = 270 #seconds = 4 minutes
        while time_left > 0:
            print(time_left)
            time.sleep(1)
            time_left = time_left - 1

        footer =  driver.find_element_by_class_name("footer")
        if footer.is_displayed():
            print('\n')  # adds line break
            print "Is the footer visible? : ", (footer.is_enabled())

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("Footer is NOT present")

        # now verify button group location after footer comes back
        button_group1 = driver.find_element_by_class_name("button-group")
        print button_group1.location

        # verify they are not the same
        if (button_group1.location, {'y': 1128.0, 'x': 1171.0}):  # bg1 = {'y': 782.0, 'x': 1171.0} / bg2 = {'y': 1128.0, 'x': 1171.0}
            print "Locations are different... proceeding"
            pass
        else:
            raise NoSuchElementException("The locations should NOT be the same")

    def test_footer_attributes(self):
        """Test the footer attributes"""

        # size
        footer =  driver.find_element_by_class_name("footer")
        size = footer.size
        print('\n')  # adds line break
        print "size of the footer is:"
        print (size)

        assertEqual(footer.size["width"], 1920)
        assertEqual(footer.size["height"], 303)

        # location
        print('\n')  # adds line break
        print "location of footer is at:"
        print (footer.location)

        assertEqual(footer.location, {"y": 782.0, "x": 0.0})

        # footer image
        footer_file = open('utils/footer_image.txt', 'r').read()
        # this requests the data from the URL again
        footer_url = requests.get("http://mod-touchscreen.beta.visual-a.com/img/footer.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(footer_file, footer_url):
            pass
        print "Footer matches what's on file"

    def test_button_group_attributes(self):
        """Test the button group attributes"""

        # restart image file
        restart_file = open('utils/restart.txt', 'r').read()
        # this requests the data from the URL again
        restart_url = requests.get(
            "http://mod-touchscreen.beta.visual-a.com//img/restart-bg.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(restart_file, restart_url):
            pass
        print "Restart image matches what's on file"

        # size - restart image
        restart = driver.find_element_by_class_name("button-group")
        size = restart.size
        print('\n')  # adds line break
        print "size of the restart image is:"
        print (size)

        assertEqual(restart.size["width"], 749)
        assertEqual(restart.size["height"], 121)

        # location - restart image
        print('\n')  # adds line break
        print "location of restart image is at:"
        print (restart.location)

        assertEqual(restart.location, {"y": 782.0, "x": 1171.0})

        # size - white area
        white_area = driver.find_element_by_class_name("restart")
        size = white_area.size
        print('\n')  # adds line break
        print "size of the white area is:"
        print (size)

        assertEqual(white_area.size["width"], 99)
        assertEqual(white_area.size["height"], 100)

        # location - white area
        print('\n')  # adds line break
        print "location of white area is at:"
        print (white_area.location)

        assertEqual(white_area.location, {"y": 789.0, "x": 1212.0})

        # image - white area
        white_area_file = open('utils/white_area_image.txt', 'r').read()
        # this requests the data from the URL again
        white_area_url = requests.get("http://mod-touchscreen.beta.visual-a.com/img/white-circle.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(white_area_file, white_area_url):
            pass
        print "White area matches what's on file"

        # size - gps ring
        ring = driver.find_element_by_class_name("gps_ring")
        print('\n')  # adds line break
        print ring.size

        width = ring.size["width"]
        if 87 <= width <= 108:
            print('\n')  # adds line break
            print "GPS Ring is in animation SIZE range"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of SIZE range")

        height = ring.size["height"]
        if 87 <= height <= 108:
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
        if 700 <= y <= 1003:
            print('\n')  # adds line break
            print "GPS Ring is in animation LOCATION range"
            pass

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of LOCATION range")

        x = ring.location['x']
        if 1194 <= x <= 1300:
            print('\n')  # adds line break
            print "GPS Ring is in animation LOCATION range"
            pass

        else:
            print('\n')  # adds line break
            raise NoSuchElementException("GPS Ring animation is out of LOCATION range")

        # size - round circle
        round_circle = driver.find_element_by_class_name("round-circle")
        size = round_circle.size
        print('\n')  # adds line break
        print "size of the round circle is:"
        print (size)

        assertEqual(round_circle.size["width"], 73)
        assertEqual(round_circle.size["height"], 68)

        # location - round circle
        print('\n')  # adds line break
        print "location of round circle is at:"
        print (round_circle.location)

        assertEqual(round_circle.location, {"y": 801.0, "x": 1223.0})

        # round circle image
        round_circle_file = open('utils/round_circle_image.txt', 'r').read()
        # this requests the data from the URL again
        round_circle_url = requests.get("http://mod-touchscreen.beta.visual-a.com/img/round-circle.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(round_circle_file, round_circle_url):
            pass
        print "Round circle matches what's on file"

        # size - arrow
        arrow = driver.find_element_by_class_name("arrow")
        size = arrow.size
        print('\n')  # adds line break
        print "size of the arrow is:"
        print (size)

        assertEqual(arrow.size["width"], 19)
        assertEqual(arrow.size["height"], 27)

        # location - arrow
        print('\n')  # adds line break
        print "location of arrow is at:"
        print (arrow.location)

        assertEqual(arrow.location, {"y": 822.0, "x": 1251.0})

        # arrow image
        arrow_file = open('utils/arrow_image.txt', 'r').read()
        # this requests the data from the URL again
        arrow_url = requests.get("http://mod-touchscreen.beta.visual-a.com/img/arrow.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(arrow_file, arrow_url):
            pass
        print "Arrow matches what's on file"

    def test_break_button(self):
        """Try to break the play button and hotspot by clicking multiple times"""

        # click triangle multiple times to try and break - #4
        for x in range(10):
        # click arrow multiple times to try and break
            arrow = driver.find_element_by_class_name("arrow")
            driver.execute_script("arguments[0].click();", arrow)
            time.sleep(1)

        for x in range(10):
        # click arrow multiple times to try and break - #5
            round_circle = driver.find_element_by_class_name("round-circle")
            driver.execute_script("arguments[0].click();", round_circle)
            time.sleep(1)

        for x in range(10):
        # click white area multiple times to try and break - #6
            white_area = driver.find_element_by_class_name("restart")
            driver.execute_script("arguments[0].click();", white_area)
            time.sleep(1)

        for x in range(10):
        # click gps ring multiple times to try and break - #7
            ring = driver.find_element_by_class_name("gps_ring")
            driver.execute_script("arguments[0].click();", ring)
            time.sleep(1)

        # gps ring attributes
            assertEqual(ring.value_of_css_property("border-bottom-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring.value_of_css_property("border-left-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring.value_of_css_property("border-right-color"), 'rgba(255, 255, 255, 1)')
            assertEqual(ring.value_of_css_property("border-top-color"), 'rgba(255, 255, 255, 1)')

        for x in range(1):
        # click hotspot multiple times to try and break - won't count towards analytics
            hotspot = driver.find_element_by_class_name("hotspot")
            driver.execute_script("arguments[0].click();", hotspot)
            time.sleep(1)

    def test_pull_analytics(self):
        """This will pull the analytics from the file(s)"""
        # read text file
        analytics_json_file = open('/Applications/MAMP/htdocs/mod_touchscreen/analytics.json', 'r').read()

        print('\n')  # adds line break
        print "Analytics JSON:"
        # compare the number of restarts in the file with the number is should be
        restart = "restart-time"
        # the total number of analytics calls should match the number of button clicks = 51

        pattern = re.compile(format(restart), re.I)  # case insensitive
        num = len(pattern.findall(analytics_json_file))

        if assertEqual(num, 52):
            print('\n')  # adds line break
            print "Restart analytic entries in JSON file match number of clicks"
            pass

            # compare the number of fullVideoWatched in the file with the number is should be
            fullVideoWatched = "fullVideoWatched"
            # the total number of analytics calls should match the number of button clicks = 1

            pattern2 = re.compile(format(fullVideoWatched), re.I)  # case insensitive
            num2 = len(pattern2.findall(analytics_json_file))
            print num2

            if assertEqual(num2, 1):
                print('\n')  # adds line break
                print "fullVideoWatched analytic entries in JSON file match number of clicks"
                pass

    def teardown_class(self):
        driver.quit()