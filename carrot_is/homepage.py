#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from utils.exceptions import FunctionalError
#from utils.log import logger
import urllib2
import requests
import time
import unittest

base_url = "http://carrot.is/"

def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the full page
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    driver.set_window_size(1080, 800)
    driver.get(base_url)

def teardown_module(module):
    driver.quit()

class TestTopNav_CarrotLogo(object):
    def test_carrot_logo(self):
        """Test correct logo present"""
        print('\n' * 2)  # adds line break
        logo = driver.find_element_by_id("logo").value_of_css_property("background-image")
        background = 'url("http://carrot.is/img/desktop_nav/carrot_logo.svg")'

        # Is the logo present? Missing? Broken?  (REPLACE WITH TRY, IF, EXCEPT)
        if assertEqual(logo, background):
            print "image missing or broken"
        else:
            print "image is present"

    def test_correct_carrot_logo(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        logo_file = open('utils/logo.txt', 'r').read()
        # this requests the data from the URL
        svg_url = requests.get("http://carrot.is/img/desktop_nav/carrot_logo.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(logo_file, svg_url):
            print "image does not match file"
        else:
            print "image matches file"


    def test_logo_size(self):
        logo = driver.find_element_by_id("logo")
        size = logo.size
        print('\n')  # adds line break
        print "size of the image is:"
        print (size)

        assertEqual(logo.size["width"], 110)
        assertEqual(logo.size["height"], 24)

    def test_logo_placement(self):

        logo = driver.find_element_by_id("logo")
        print('\n')  # adds line break
        print "location of image is at:"
        print (logo.location)

        assertEqual(logo.location, {"y": 28.0, "x": 60.0})

    def test_carrot_logo_menu(self):
        """Test logo menu parts, fonts, colors"""

        logo = driver.find_element_by_id("logo")

        # logo dropdown
        logo_dropdown = driver.find_element_by_id("contextmenu")

        # drop down the menu - right click = content_click
        ActionChains(driver).move_to_element(logo).context_click(logo).perform()
        ActionChains(driver).move_to_element(logo_dropdown).click().perform()
        time.sleep(1)

        ## Use 'len' to verify items in dropdown? ##

        # little arrow present?
        assert driver.find_element_by_id("arrow")

        #little arrow color
        arrow = driver.find_element_by_id("arrow")
        assertEqual(arrow.value_of_css_property("border-bottom"), '8px solid rgb(140, 198, 63)')

        # menu background present?
        assert driver.find_element_by_id("contextmenu")

        # menu background color
        menu = driver.find_element_by_id("contextmenu")
        assertEqual(menu.value_of_css_property("background-color"), 'rgba(140, 198, 63, 1)')


        # menus items text font
        menu_font = driver.find_elements_by_tag_name("a")[9 - 11]
        menu_font2 = driver.find_elements_by_tag_name("h4")[0]
        assertEqual(menu_font.value_of_css_property("font-family"),
                    'proxima-nova, "Helvetica Neue", HelveticaNeue, Helvetica, Arial, sans-serif')
        assertEqual(menu_font2.value_of_css_property("font-family"),
                    'proxima-nova, "Helvetica Neue", HelveticaNeue, Helvetica, Arial, sans-serif')

        # logo dropdown
        logo_dropdown = driver.find_element_by_id("contextmenu")

        # drop down the menu
        ActionChains(driver).move_to_element(logo).context_click(logo).perform()
        ActionChains(driver).move_to_element(logo_dropdown).click().perform()
        time.sleep(1)

        # menu items text color
        menu_items = driver.find_element_by_tag_name("h4")
        menu_items2 = driver.find_elements_by_tag_name("a")[9 - 11]
        assertEqual(menu_items.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')
        assertEqual(menu_items2.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')

    def test_carrot_logo_files(self):
        """Test logo menu file types"""

        # EPS (9)

        logo = driver.find_element_by_id("logo")

        # logo dropdown
        logo_dropdown = driver.find_element_by_id("contextmenu")

        # download text
        assert driver.find_element_by_tag_name("h4")

        #eps = driver.find_elements_by_tag_name("a")[9]

        #ActionChains(driver).move_to_element(logo).context_click(logo).perform()
        #ActionChains(driver).move_to_element(logo_dropdown).click(eps).perform()
        #time.sleep(2)

        # PNG (10)

        logo = driver.find_element_by_id("logo")

        # logo dropdown
        logo_dropdown = driver.find_element_by_id("contextmenu")

        # download text
        assert driver.find_element_by_tag_name("h4")

        png = driver.find_elements_by_tag_name("a")[10]

        ActionChains(driver).move_to_element(logo).context_click(logo).perform()
        ActionChains(driver).move_to_element(logo_dropdown).click(png).perform()
        driver.get(base_url)
        time.sleep(2)

        # JPEG (11)

        logo = driver.find_element_by_id("logo")

        # logo dropdown
        logo_dropdown = driver.find_element_by_id("contextmenu")

        # download text
        assert driver.find_element_by_tag_name("h4")

        jpeg = driver.find_elements_by_tag_name("a")[11]

        ActionChains(driver).move_to_element(logo).context_click(logo).perform()
        ActionChains(driver).move_to_element(logo_dropdown).click(jpeg).perform()
        driver.get(base_url)
        time.sleep(2)

    def test_navigation_links(self):
        """Work, About, Careers, Blog clickouts"""

        # nav links colors
        nav_colors = driver.find_elements_by_tag_name("a")[12 - 15]
        assertEqual(nav_colors.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')

        # nav links clickthroughs
        driver.find_element_by_link_text("WORK").click()
        assert driver.find_element_by_id("case-studies")
        driver.get(base_url)
        time.sleep(1)
        driver.find_element_by_link_text("ABOUT").click()
        assert driver.find_element_by_id("about")
        driver.get(base_url)
        time.sleep(1)
        driver.find_element_by_link_text("CAREERS").click()
        assert driver.find_element_by_id("hiring")
        driver.get(base_url)
        time.sleep(1)
        driver.find_element_by_link_text("BLOG").click()
        time.sleep(1)
        driver.find_element_by_id("blog")
        driver.get(base_url)
        time.sleep(1)

    def test_navigation_attributes(self):
        """Work, About, Careers, Blog font attributes"""

        # nav text size
        text_size1 = driver.find_element_by_link_text("WORK")
        text_size2 = driver.find_element_by_link_text("ABOUT")
        text_size3 = driver.find_element_by_link_text("CAREERS")
        text_size4 = driver.find_element_by_link_text("BLOG")
        assertEqual(text_size1.value_of_css_property("font-size"), '16.5px')
        assertEqual(text_size2.value_of_css_property("font-size"), '16.5px')
        assertEqual(text_size3.value_of_css_property("font-size"), '16.5px')
        assertEqual(text_size4.value_of_css_property("font-size"), '16.5px')

        # nav links font
        nav_font = driver.find_elements_by_tag_name("a")[12 - 15]
        assertEqual(nav_font.value_of_css_property("font-family"),
                    'proxima-nova, "Helvetica Neue", HelveticaNeue, Helvetica, Arial, sans-serif')

class TestGetInTouch(object):
    def test_contact_button(self):
        """This will test all the functionality of the 'Get In Touch' button"""

        assert driver.find_elements_by_tag_name("g")[10]
        get_in = driver.find_elements_by_tag_name("g")[10]
        assertEqual(get_in.value_of_css_property("color"), 'rgba(140, 198, 63, 1)')

        # Get In Touch open
        driver.find_elements_by_tag_name("a")[16].click()
        time.sleep(1)

        # orange 'x' color
        orange_x = driver.find_elements_by_tag_name("g")[11]
        assertEqual(orange_x.value_of_css_property("color"), 'rgba(140, 198, 63, 1)')


    def test_active(self):
        """This will test all the Map active element functionality"""
        # make sure gmaps is present and actively selected
        try:
            gmaps_active = driver.find_element_by_class_name("active").find_element_by_class_name("gmaps")  # this element should be visible
            if gmaps_active.is_enabled():
                print('\n')  # adds line break
                print "Google Maps Active"
        except NoSuchElementException:
            print('\n')  # adds line break
            print "Google Maps NOT Active"
            time.sleep(3)
            raise

        driver.find_element_by_class_name("car").click()

        # make sure car is present and actively selected
        try:
            car_active = driver.find_element_by_class_name("active").find_element_by_class_name(
                "car")  # this element should be visible
            if car_active.is_enabled():
                print('\n')  # adds line break
                print "Car Active"
        except NoSuchElementException:
            print('\n')  # adds line break
            print "Car NOT Active"
            time.sleep(3)
            raise

        driver.find_element_by_class_name("train").click()

        # make sure train is present and actively selected
        try:
            train_active = driver.find_element_by_class_name("active").find_element_by_class_name(
                "train")  # this element should be visible
            if train_active.is_enabled():
                print('\n')  # adds line break
                print "Train Active"
        except NoSuchElementException:
            print('\n')  # adds line break
            print "Train NOT Active"
            time.sleep(3)
            raise

        driver.find_element_by_class_name("dino").click()

        # make sure dino is present and actively selected
        try:
            dino_active = driver.find_element_by_class_name("active").find_element_by_class_name(
                "dino")  # this element should be visible
            if dino_active.is_enabled():
                print('\n')  # adds line break
                print "Dino Active"
        except NoSuchElementException:
            print('\n')  # adds line break
            print "Dino NOT Active"
            time.sleep(3)
            raise


    def test_address_attributes(self):
        """This will test all the address container attributes"""

        # address font family
        address_font = driver.find_elements_by_tag_name("a")[12 - 15]
        assertEqual(address_font.value_of_css_property("font-family"),
                    'proxima-nova, "Helvetica Neue", HelveticaNeue, Helvetica, Arial, sans-serif')

        # address font color
        address_color = driver.find_elements_by_tag_name("a")[12 - 15]
        assertEqual(address_color.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')

        #address font size
        address_text = driver.find_element_by_link_text("BLOG")
        assertEqual(address_text.value_of_css_property("font-size"), '16.5px')

        # PIN icon - DO THE SAME AS LOGO (SAVE INFO)
        pin = 'url("http://carrot.is/img/contact/address_pin.svg")'
        address = driver.find_element_by_class_name("address").value_of_css_property("background-image")

        # Is the pin present? Missing? Broken? (REPLACE WITH TRY, IF, EXCEPT)
        if assertEqual(address, pin):
            print('\n') # adds line break
            print "Pin missing or broken"
        else:
            print('\n') # adds line break
            print "Pin is present"

        # see if the SVG matches

        # this pulls data from the text file
        pin_file = open('utils/pin.txt', 'r').read()
        # this requests the data from the URL
        pin_svg_url = requests.get("http://carrot.is/img/contact/address_pin.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(pin_file, pin_svg_url):
            print "Pin does not match file"
        else:
            print "Pin matches file"

        # Mobile icon
        mobile_icon = 'url("http://carrot.is/img/contact/mobile_icon.svg")'
        call = driver.find_element_by_class_name("call").value_of_css_property("background-image")

        # Is the pin present? Missing? Broken? (REPLACE WITH TRY, IF, EXCEPT)
        if assertEqual(mobile_icon, call):
            print('\n')  # adds line break
            print "Mobile icon missing or broken"
        else:
            print('\n')  # adds line break
            print "Mobile icon is present"

        # see if the SVG matches

        # this pulls data from the text file
        mobile_icon_file = open('utils/mobile_icon.txt', 'r').read()
        # this requests the data from the URL
        mobile_icon_url = requests.get("http://carrot.is/img/contact/mobile_icon.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(mobile_icon_file, mobile_icon_url):
            print "Mobile icon does not match file"
        else:
            print "Mobile icon matches file"

        # EMAIL icon
        email_icon = 'url("http://carrot.is/img/contact/email_icon.svg")'
        email = driver.find_element_by_class_name("email").value_of_css_property("background-image")

        # Is the pin present? Missing? Broken? (REPLACE WITH TRY, IF, EXCEPT)
        if assertEqual(email_icon, email):
            print('\n')  # adds line break
            print "Email icon missing or broken"
        else:
            print('\n')  # adds line break
            print "Email icon is present"

        # see if the SVG matches

        # this pulls data from the text file
        email_icon_file = open('utils/email_icon.txt', 'r').read()
        # this requests the data from the URL
        email_icon_url = requests.get("http://carrot.is/img/contact/email_icon.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(email_icon_file, email_icon_url):
            print "Email icon does not match file"
        else:
            print "Email icon matches file"

        # WORK icon
        work_icon = 'url("http://carrot.is/img/contact/email_icon.svg")'
        work = driver.find_element_by_class_name("work").value_of_css_property("background-image")

        # Is the pin present? Missing? Broken? (REPLACE WITH TRY, IF, EXCEPT)
        if assertEqual(work_icon, work):
            print('\n')  # adds line break
            print "Work icon missing or broken"
        else:
            print('\n')  # adds line break
            print "Work icon is present"

        # see if the SVG matches

        # this pulls data from the text file
        work_icon_file = open('utils/email_icon.txt', 'r').read()
        # this requests the data from the URL
        work_icon_url = requests.get("http://carrot.is/img/contact/email_icon.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(work_icon_file, work_icon_url):
            print "Work icon does not matches the EMAIL file"
        else:
            print "Work icon matches the EMAIL file"

        # GRAY TEXT FONT - span [0 - 4]
        gray_font = driver.find_elements_by_tag_name("span")[0 - 4]
        assertEqual(gray_font.value_of_css_property("font-family"),
                    'proxima-nova, "Helvetica Neue", HelveticaNeue, Helvetica, Arial, sans-serif')

        # GRAY TEXT COLOR - span [0 - 4]
        gray_color = driver.find_elements_by_tag_name("span")[0 - 4]
        assertEqual(gray_color.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')

        # BLACK TEXT FONT - p [0 - 3]
        black_font = driver.find_elements_by_tag_name("p")[0 - 3]
        assertEqual(black_font.value_of_css_property("font-family"),
                    'proxima-nova, "Helvetica Neue", HelveticaNeue, Helvetica, Arial, sans-serif')

        # BLACK TEXT COLOR - p [0 - 3]
        black_color = driver.find_elements_by_tag_name("p")[0 - 3]
        assertEqual(black_color.value_of_css_property("color"), 'rgba(85, 85, 85, 1)')

        driver.find_elements_by_tag_name("a")[4].click()
        time.sleep(3)

        # put focus on newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        # close the tab
        driver.close()
        # switch to the main window
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

        # orange 'x' close functionality
        orange_x = driver.find_elements_by_tag_name("g")[11]
        orange_x.click()
        time.sleep(1)

class TestGITContainers(object):
    def test_containers(self):
        """This will test the color and size of the 'switch-map' 'map-container' and 'info' container"""
        #container = driver.find_element_by_id("map-container")
        #container_size = container.size
        #print('\n')  # adds line break
        #print "size of the container is:"
        #print (container_size)

        #assertEqual(container.size["width"], 110)
        #assertEqual(container.size["height"], 24)

        ####

        map_container_file = open('utils/map_container.txt', 'r').read()
        # this requests the data from the URL
        map_container_url = requests.get\
            ("http://d33wubrfki0l68.cloudfront.net/a4c322c6439d0816b64a6afed20488ac6e55719e/e0497/img/contact/direction_maps/map.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(map_container_file, map_container_url):
            print "Mobile icon does not match file"
        else:
            print "Mobile icon matches file"

    def test_map_click_functionality(self):
        """This will test all the Map info click functionality"""

        # map click functionality

        # phone click out functionality

        # email and email functionality


class TestHomepageBody(object):
    def test_video_functionality(self):
        """This will test the video"""

    def test_sizzle_text_and_button(self):
        """This will make sure the text is rendering correctly
        and the button renders and functions correctly"""

    def test_callouts_text_button(self):
        """This will make sure the text is rendering correctly
        and the button renders and functions correctly for the
        'Come work with us' section"""

class TestHomepageFooter(object):
    def test_vice_logos(self):
        """This will test that all logos are rendering properly"""

    def test_footer_video_functionality(self):
        """This will test the video"""

    def test_social_and_links(self):
        """This will test all the footer links, including social"""

    def test_newsletter_signup(self):
        """This will test newsletter signup"""

    #
    def teardown_class(self):
        driver.quit()

        ### Multiple screen resolutions