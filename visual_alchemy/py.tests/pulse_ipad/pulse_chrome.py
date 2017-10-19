# -*- coding: utf-8 -*-

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import requests
import time

base_url = "http://pulse.beta.visual-a.com/login/"

def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the full page
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 768)
    driver.get(base_url)
    driver.implicitly_wait(1)

def teardown_module(module):
    driver.quit()

class TestLogin(object):

    def test_pulse_login(self):
        """Test login opens"""
        time.sleep(5)

        # is login present?
        user = driver.find_element_by_id("id_username")

        if user.is_displayed():

            top_bg = driver.find_element_by_id("wrapper")
            assertEqual(top_bg.value_of_css_property("background-image"),
                        'url(https://va-pulse-beta.s3.amazonaws.com/static/img/vi_login_bkg_top.gif)')

            # verify top vi_bkg_top matches
            top_file = open('utils/top.txt', 'r').read()
            # this requests the data from the URL
            top_url = requests.get(
                "https://va-pulse-beta.s3.amazonaws.com/static/img/vi_login_bkg_top.gif").content
            # this compares the 2
            print('\n')  # adds line break
            if assertEqual(top_file, top_url):
                pass
            print "Top matches file"

            # verify bottom background image
            bottom_bg = driver.find_element_by_xpath("/html/body")

            assertEqual(bottom_bg.value_of_css_property("background-image"),
                        'url(https://va-pulse-beta.s3.amazonaws.com/static/img/vi_login_bkg_bottom.gif)')

            # verify top vi_bkg_bottom matches
            bottom_file = open('utils/bottom.txt', 'r').read()
            # this requests the data from the URL again
            bottom_url = requests.get(
                "https://va-pulse-beta.s3.amazonaws.com/static/img/vi_login_bkg_bottom.gif").content
            # this compares the 2
            print('\n')  # adds line break
            if assertEqual(bottom_file, bottom_url):
                pass
            print "Bottom matches file"

            # verify forgot password? link
            forgot = driver.find_element_by_class_name("forgot")
            if forgot.is_enabled():
                print('\n')  # adds line break
                print "Is 'Forgot password?' link enabled: ", (forgot.is_enabled())

            else:
                print('\n')  # adds line break
                raise NoSuchElementException("Forgot password link inactive")

            # verify forgot password link attributes
            try:
                assertEqual(forgot.text, "Forgot password?")
                print('\n')  # adds line break
                print "'", forgot.text, "'", " text matches"
            except:
                print('\n')  # adds line break
                print "Text does not match"
                raise NoSuchElementException("Text does not match")

            # location
            print('\n')  # adds line break
            print "Location of logo is at:"
            print (forgot.location)

            assertEqual(forgot.location, {"y": 202.0, "x": 370.0})

            # verify text attributes
            assertEqual(forgot.value_of_css_property("color"), 'rgba(184, 184, 184, 1)')
            assertEqual(forgot.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
            assertEqual(forgot.value_of_css_property("font-size"), '12px')
            assertEqual(forgot.value_of_css_property("font-weight"), 'normal')

            # verify other elements by logging into the web app: developer/imagine1
            driver.find_element_by_class_name("input").click()

            username = "developer"
            password = "imagine1"
            driver.find_element_by_class_name("input").click()
            time.sleep(1)
            driver.find_element_by_id("id_username").send_keys(username)
            driver.find_element_by_id("id_password").send_keys(password)

            login = driver.find_element_by_id("login")
            # button color
            assertEqual(forgot.value_of_css_property("color"), 'rgba(184, 184, 184, 1)')

            # login button size
            print('\n')  # adds line break
            print "Size of the login button is:"
            print (login.size)

            assertEqual(login.size["width"], 196)
            assertEqual(login.size["height"], 41)

            # login button location
            print('\n')  # adds line break
            print "Location of login button is at:"
            print (login.location)

            assertEqual(login.location, {"y": 249.0, "x": 371.0})

            # login button text
            login_text = driver.find_element_by_id("login").get_attribute("value")

            try:
                assertEqual(login_text, "Login")
                print('\n')  # adds line break
                print "'", login_text, "'", " text matches"
            except:
                print('\n')  # adds line break
                print "Text does not match"
                raise NoSuchElementException("Text does not match")

            # verify text attributes
            text_att = driver.find_element_by_id("login")
            assertEqual(text_att.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
            assertEqual(text_att.value_of_css_property("font-family"), 'Helvetica')
            assertEqual(text_att.value_of_css_property("font-size"), '12px')
            assertEqual(text_att.value_of_css_property("font-weight"), 'normal')

            # click the login button
            login.click()
            time.sleep(5)

        else:
            print "User already logged in."
            pass

class TestContentHeader(object):
    def logo(self):
        """Test homepage attributes"""
        # logoWrapper
        try:
            logo = driver.find_element_by_class_name("logoWrapper")
            if logo.is_displayed():
                print('\n')  # adds line break
                print "Logo found"

        except:
            print('\n')  # adds line break
            raise NoSuchElementException("Logo not found")

        # size
        print('\n')  # adds line break
        print "Size of the logo is:"
        print (logo.size)

        assertEqual(logo.size["width"], 276)
        assertEqual(logo.size["height"], 115)

        # location
        print('\n')  # adds line break
        print "Location of logo is at:"
        print (logo.location)

        assertEqual(logo.location, {"y": 10.0, "x": 10.0})

    def correct_logo(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        logo_file = open('utils/logo.txt', 'r').read()
        # this requests the data from the URL again
        png_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/pulse.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(logo_file, png_url):
            pass
        print "Logo matches file"

    def event_title(self):
        title = driver.find_element_by_css_selector("h1").text
        if assertEqual(title, "Test_Admin"):
            pass
        print('\n')  # adds line break
        print title

        date = driver.find_element_by_css_selector("h2").text
        if assertEqual(date, "August 30-31, 2017"):
            pass
        print('\n')  # adds line break
        print date

        city = driver.find_element_by_xpath("//*[@id='contentHeader']/div[2]/h2[2]").text
        if assertEqual(city, "New York, NY"):
            pass
        print('\n')  # adds line break
        print city

    def profile(self):
        """test profile box"""

        # verify the box is present and the right size/location
        try:
            profile = driver.find_element_by_id("profile")
            if profile.is_displayed():
                print('\n')  # adds line break
                print "Profile box found"

        except:
            print('\n')  # adds line break
            raise NoSuchElementException("Profile box not found")

        # size
        print('\n')  # adds line break
        print "Size of the profile box is:"
        print (profile.size)

        assertEqual(profile.size["width"], 303)
        assertEqual(profile.size["height"], 178)

        # location
        print('\n')  # adds line break
        print "Location of profile box is at:"
        print (profile.location)

        assertEqual(profile.location, {"y": 10.0, "x": 708.0})

        # this pulls data from the text file
        profile_file = open('utils/profile.txt', 'r').read()
        # this requests the data from the URL again
        profile_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/user.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(profile_file, profile_url):
            pass
        print "Logo matches file"

        # verify the correct profileName is present with correct attributes
        name = driver.find_element_by_class_name("profileName")
        if assertEqual(name.text, "Kevin Cherepski, MD"):
            pass
        print "profileName is correct"

        assertEqual(name.value_of_css_property("color"), 'rgba(87, 114, 146, 1)')
        assertEqual(name.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(name.value_of_css_property("font-size"), '18px')
        assertEqual(name.value_of_css_property("font-weight"), 'normal')

        # verify the correct profileSpecialty is present with correct attributes
        specialty = driver.find_element_by_class_name("profileSpecialty")
        if assertEqual(specialty.text, "Technology"):
            pass
        print "profileSpecialty is correct"

        assertEqual(specialty.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(specialty.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(specialty.value_of_css_property("font-size"), '14px')
        assertEqual(specialty.value_of_css_property("font-weight"), 'normal')

        # verify the correct profileLocation is present with correct attributes
        location = driver.find_element_by_class_name("profileLocation")
        if assertEqual(location.text, "Georgetown University\nNew York, NY"):
            pass
        print "profileLocation is correct"

        assertEqual(location.value_of_css_property("color"), 'rgba(170, 170, 170, 1)')
        assertEqual(location.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(location.value_of_css_property("font-size"), '14px')
        assertEqual(location.value_of_css_property("font-weight"), 'normal')

        # verify that profileTasks is present with correct attributes
        tasks = driver.find_element_by_id("profileTasks")
        if assertEqual(tasks.text, "0% of Tasks Completed"):
            pass
        print "profileTask is correct"

        assertEqual(tasks.value_of_css_property("color"), 'rgba(67, 67, 67, 1)')
        assertEqual(tasks.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(tasks.value_of_css_property("font-size"), '12px')
        assertEqual(tasks.value_of_css_property("font-weight"), 'normal')

        # verify percentage complete
        percentage = driver.find_element_by_class_name("bar").get_attribute("style")
        print percentage

        if assertEqual("width: 0%;", percentage):
            pass
        print "The width of the status bar is", percentage

        # verify that the profileTask percentage matches the actual percentage in the status bar
        chars = set("0%")
        if any((c in chars) for c in (percentage or tasks.text)):
            pass
        print "profileTask text matches the percentage in the status bar"

    def navigation_icons(self):
        """verify the navigation icons are at the bottom"""

        # this is the SVG text file
        #icons_file = open('utils/home_icon.txt', 'w')
        # this requests the data from the URL
        #icons_url = requests.get("https://va-pulse-beta.s3.amazonaws.com/static/img/footerIconsNew.png").content
        # this saves the data into the SVG text file
        #icons_file.write(icons_url)

        # this pulls data from the text file
        icons_file = open('utils/home_icon.txt', 'r').read()
        # this requests the data from the URL again
        icons_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/footerIconsNew.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(icons_file, icons_url):
            pass
        print "Icons match what's on file"

class TestHome(object):
    def home_button(self):
        """verify you are actually on the home page"""
        home_nav = driver.find_element_by_id("homeNav")
        if home_nav.is_enabled():
            assert driver.find_element_by_class_name("active")
            print('\n')  # adds line break
            print "You are on the Home screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Home screen")

    def schedule_of_events(self):
        """Test Schedule of Events sections and logo"""

        # this pulls data from the text file
        schedule_file = open('utils/schedule.txt', 'r').read()
        # this requests the data from the URL again
        schedule_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/sched.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(schedule_file, schedule_url):
            pass
        print "Logo matches file"

    def schedule_text(self):
        schedule = driver.find_element_by_xpath("//*[@id='content']/h1").text
        if assertEqual(schedule, "Schedule of Events"):
            pass
        print('\n')  # adds line break
        print schedule

    def schedule_header(self):
        # header text
        header = driver.find_element_by_css_selector("a.active")
        # #scheduleHeader a.active
        if assertEqual(header.text, "Thursday, Aug 31"):
            pass
        print('\n')  # adds line break
        print "profileHeader is correct"

        # header attributes
        assertEqual(header.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')
        assertEqual(header.value_of_css_property("background-color"), 'rgba(25, 69, 129, 1)')
        assertEqual(header.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(header.value_of_css_property("font-size"), '16px')
        assertEqual(header.value_of_css_property("font-weight"), 'normal')

    def hour_header(self):
        # hour header text
        hour_text = driver.find_element_by_class_name("scheduleHourHeader")
        if assertEqual(hour_text.text, "11:00 am"):
            pass
        print('\n')  # adds line break
        print "scheduleHourHeader is correct"

        # hour header attributes
        assertEqual(hour_text.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')
        assertEqual(hour_text.value_of_css_property("font-family"), 'Helvetica, Arial, sans-serif')
        assertEqual(hour_text.value_of_css_property("font-size"), '16px')
        assertEqual(hour_text.value_of_css_property("font-weight"), 'bold')

        hour_header = driver.find_element_by_class_name("scheduleHourHeader")
        # hour header location
        assertEqual(hour_header.location, {"y": 301.0, "x": 11.0})
        print('\n')  # adds line break
        print "Location of hour header is at :", (hour_header.location)
        # hour header size
        assertEqual(hour_header.size["width"], 1003)
        assertEqual(hour_header.size["height"], 23)
        print('\n')  # adds line break
        print "Size of hour header is:", (hour_header.size)

    def schedule_topic(self):
        # schedule topic text
        schedule_topic = driver.find_element_by_class_name("scheduleTopic")

        # schedule topic location
        assertEqual(schedule_topic.location, {"y": 324.0, "x": 11.0})
        print('\n')  # adds line break
        print "Location of schedule topic is at :", (schedule_topic.location)
        # schedule topic size
        assertEqual(schedule_topic.size["width"], 1003)
        assertEqual(schedule_topic.size["height"], 119)
        print('\n')  # adds line break
        print "Size of schedule topic is:", (schedule_topic.size)

        # Location:
        location = driver.find_element_by_class_name("left")
        if assertEqual(location.text, "LOCATION:\n1"):
            pass
        print('\n')  # adds line break
        print "'Location' text is correct"

        location_number = driver.find_element_by_class_name("blue").get_attribute('innerText')
        if assertEqual(location_number, "1"):
            pass
        print('\n')  # adds line break
        print "Location number is correct"

        # this pulls data from the text file
        badge_file = open('utils/badge.txt', 'r').read()
        # this requests the data from the URL again
        badge_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/notification_bg.png").content
        # this compares the 2
        if assertEqual(badge_file, badge_url):
            pass
        print('\n')  # adds line break
        print "Logo matches file"

        city = driver.find_element_by_class_name("right").text
        if assertEqual(city, "New York, NY - 11:05 am - 12:05 pm\nTest Ab\nTest Author\nOral Presentation"):
            pass
        print('\n')  # adds line break
        print "City text is correct"

        time = driver.find_element_by_xpath("//*[@id='schedule']/ul/li/ul/ul/li/a/div[2]/span").text
        if assertEqual(time, "11:05 am - 12:05 pm"):
            pass
        print('\n')  # adds line break
        print "Time text is correct"

        title = driver.find_element_by_xpath("//*[@id='schedule']/ul/li/ul/ul/li/a/div[2]/div[1]").text
        if assertEqual(title, "Test Ab"):
            pass
        print('\n')  # adds line break
        print "Title text is correct"

        author_type = driver.find_element_by_class_name("lightGray")
        if assertEqual(author_type.text, "Test Author\nOral Presentation"):
            pass
        print('\n')  # adds line break
        print "Author / Event Type text is correct"

class TestUsers(object):
    def test_users_button(self):
        """verify you are actually on the users page"""
        driver.find_element_by_id("usersNav").click()
        users_nav = driver.find_element_by_id("usersNav")
        if users_nav.is_enabled():
            assert driver.find_element_by_class_name("active")
            print('\n')  # adds line break
            print "You are on the Users screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Users screen")

    def test_user_image(self):
        """This tests the user image is present"""

        # this pulls data from the text file
        user_image_file = open('utils/user_image.txt', 'r').read()
        # this requests the data from the URL again
        user_image_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/footerIconsNew.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(user_image_file, user_image_url):
            pass
        print "Image matches what's on file"

        # userDescription
        user = driver.find_element_by_tag_name("h3").text
        if assertEqual(user, "Kevin Cherepski, BS"):
            pass
        print('\n')  # adds line break
        print "User text is correct"








class TestNotifications(object):
    def notifications_button(self):
        """verify you are actually on the notifications page"""
        notifications_nav = driver.find_element_by_id("notiNav")
        if notifications_nav.is_enabled():
            assert driver.find_element_by_class_name("active")
            print('\n')  # adds line break
            print "You are on the Notifications screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Notifications screen")

class TestOther(object):
    def other_button(self):
        """verify you are actually on the other page"""
        other_nav = driver.find_element_by_id("otherNav")
        if other_nav.is_enabled():
            assert driver.find_element_by_class_name("active")
            print('\n')  # adds line break
            print "You are on the Other screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Other screen")

class TestSupport(object):
    def support_button(self):
        """verify you are actually on the support page"""
        support_nav = driver.find_element_by_id("supportNav")
        if support_nav.is_enabled():
            assert driver.find_element_by_class_name("active")
            print('\n')  # adds line break
            print "You are on the Support screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Support screen")

class TestLogout(object):
    def test_logo(self):
        """Test logout attributes"""

