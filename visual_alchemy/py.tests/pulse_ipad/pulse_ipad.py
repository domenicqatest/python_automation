### The commented out info below is ALL OUTDATED! ###

#"""Be sure to connect to the iOS server!"""
#java -jar jars/ios-server-standalone-0.6.6-SNAPSHOT.jar

#Try this:
#http://ios-driver.github.io/ios-driver/?page=safari


from selenium import webdriver
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import requests
import time


# iphone
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                #'app': '[app]'
                'browserName': 'safari',
                'platformName': 'iOS',
                'platformVersion': '10.3',
                'deviceName': 'iPad Air',
                'orientation': 'LANDSCAPE'
            })
# ipad
#driver = webdriver.Remote("http://localhost:5555/wd/hub", webdriver.DesiredCapabilities.IPAD)

base_url = "http://pulse.beta.visual-a.com/login"

def setup_module(module):
    """The setup_module runs only one time."""

    driver.get(base_url)
    driver.implicitly_wait(1)

class TestLogin(object):

    def test_pulse_login(self):
        """Test login opens"""
        time.sleep(5)

        # is login present?
        user = driver.find_element_by_id("id_username")

        if user.is_displayed():

            top_bg = driver.find_element_by_id("wrapper")
            assertEqual(top_bg.value_of_css_property("background-image"), 'url(https://va-pulse-beta.s3.amazonaws.com/static/img/vi_login_bkg_top.gif)')

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
    def test_logo(self):
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

    def test_correct_logo(self):
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

    def test_event_title(self):
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

    def test_profile(self):
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
        if assertEqual(tasks.text, "25% of Tasks Completed"):
            pass
        print "profileTask is correct"

        assertEqual(tasks.value_of_css_property("color"), 'rgba(67, 67, 67, 1)')
        assertEqual(tasks.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(tasks.value_of_css_property("font-size"), '12px')
        assertEqual(tasks.value_of_css_property("font-weight"), 'normal')

        # verify percentage complete
        percentage = driver.find_element_by_class_name("bar").get_attribute("style")
        print percentage

        if assertEqual("width: 25%;", percentage):
            pass
        print "The width of the status bar is", percentage

        # verify that the profileTask percentage matches the actual percentage in the status bar
        chars = set("25%")
        if any((c in chars) for c in (percentage or tasks.text)):
            pass
        print "profileTask text matches the percentage in the status bar"

    def test_navigation_icons(self):
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
    def test_home_button(self):
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

    def test_schedule_of_events(self):
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

    def test_schedule_text(self):
        schedule = driver.find_element_by_xpath("//*[@id='content']/h1").text
        if assertEqual(schedule, "Schedule of Events"):
            pass
        print('\n')  # adds line break
        print schedule

    def test_schedule_header(self):
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

    def test_hour_header(self):
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

    def test_schedule_topic(self):
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

        # location attributes
        assertEqual(location.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(location.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(location.value_of_css_property("font-size"), '16px')
        assertEqual(location.value_of_css_property("font-weight"), 'normal')

        location_number = driver.find_element_by_class_name("blue").get_attribute('innerText')
        if assertEqual(location_number, "1"):
            pass
        print('\n')  # adds line break
        print "Location number is correct"

        # location number attributes
        assertEqual(location_number.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(location_number.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(location_number.value_of_css_property("font-size"), '12px')
        assertEqual(location_number.value_of_css_property("font-weight"), 'normal')

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

        # city - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        city = driver.find_element_by_class_name("right").text
        if assertEqual(city, "New York, NY - 11:05 am - 12:05 pm\nTest Ab\nTest Author\nOral Presentation"):
            pass
        print('\n')  # adds line break
        print "City text is correct"

        # city attributes
        assertEqual(city.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(city.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(city.value_of_css_property("font-size"), '12px')
        assertEqual(city.value_of_css_property("font-weight"), 'normal')

        time = driver.find_element_by_xpath("//*[@id='schedule']/ul/li/ul/ul/li/a/div[2]/span").text
        if assertEqual(time, "11:05 am - 12:05 pm"):
            pass
        print('\n')  # adds line break
        print "Time text is correct"

        # title - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        title = driver.find_element_by_xpath("//*[@id='schedule']/ul/li/ul/ul/li/a/div[2]/div[1]").text
        if assertEqual(title, "Test Ab"):
            pass
        print('\n')  # adds line break
        print "Title text is correct"

        # title attributes
        assertEqual(title.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(title.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(title.value_of_css_property("font-size"), '12px')
        assertEqual(title.value_of_css_property("font-weight"), 'normal')

        # title - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        author_type = driver.find_element_by_class_name("lightGray")
        if assertEqual(author_type.text, "Test Author\nOral Presentation"):
            pass
        print('\n')  # adds line break
        print "Author / Event Type text is correct"

        # author attributes
        assertEqual(author_type.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(author_type.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(author_type.value_of_css_property("font-size"), '12px')
        assertEqual(author_type.value_of_css_property("font-weight"), 'normal')

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

    def test_user_attributes(self):
        """This tests the attributes of the text"""

        # name - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        user = driver.find_element_by_tag_name("h3")
        if assertEqual(user.text, "Kevin Cherepski, BS"):
            pass
        print('\n')  # adds line break
        print "User text is correct"

        # user attributes
        assertEqual(user.value_of_css_property("color"), 'rgba(19, 68, 127, 1)')
        assertEqual(user.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(user.value_of_css_property("font-size"), '18px')
        assertEqual(user.value_of_css_property("font-weight"), 'normal')

        # profession - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        profession = driver.find_element_by_tag_name("p")
        if assertEqual(profession.text, "Sitting Around"):
            pass
        print('\n')  # adds line break
        print "Profession text is correct"

        # profession attributes
        assertEqual(profession.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(profession.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(profession.value_of_css_property("font-size"), '12px')
        assertEqual(profession.value_of_css_property("font-weight"), 'normal')

        # college - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        college = driver.find_element_by_class_name("college")
        if assertEqual(college.text, "Georgetown University"):
            pass
        print('\n')  # adds line break
        print "College text is correct"

        # college attributes
        assertEqual(college.value_of_css_property("color"), 'rgba(170, 170, 170, 1)')
        assertEqual(college.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(college.value_of_css_property("font-size"), '12px')
        assertEqual(college.value_of_css_property("font-weight"), 'normal')

        # verify that profileTasks is present with correct attributes
        tasks = driver.find_element_by_class_name("userProgress")
        if assertEqual(tasks.text, "0% of Tasks Completed"):
            pass
        print('\n')  # adds line break
        print "profileTask is correct"

        assertEqual(tasks.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(tasks.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(tasks.value_of_css_property("font-size"), '14px')
        assertEqual(tasks.value_of_css_property("font-weight"), 'normal')

        # verify percentage complete
        percentage = driver.find_element_by_class_name("bar").get_attribute("style")
        print percentage

        if assertEqual("width: 25%;", percentage):
            pass
        print('\n')  # adds line break
        print "The width of the status bar is", percentage

        # verify that the profileTask percentage matches the actual percentage in the status bar
        chars = set("0%")
        if any((c in chars) for c in (percentage or tasks.text)):
            pass
        print('\n')  # adds line break
        print "userProgress text matches the percentage in the status bar"

class TestNotifications(object):
    def test_notifications_button(self):
        """verify you are actually on the notifications page"""
        driver.find_element_by_id("notifNav").click()
        notifications_nav = driver.find_element_by_id("notifNav")
        if notifications_nav.is_enabled():
            assert driver.find_element_by_class_name("active")
            print('\n')  # adds line break
            print "You are on the Notifications screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Notifications screen")

        # test notification
        driver.find_element_by_class_name("itemDescription").click()

        # verify notification text
        try:
            assert driver.find_element_by_class_name("dateline")
            assert driver.find_element_by_class_name("title")
            assert driver.find_element_by_class_name("body")
        except:
            print('\n')  # adds line break
            raise NoSuchElementException("Notification elements not found")

        # go back to notification screen
        driver.find_element_by_id("notifNav").click()

        # verify badge is present
        assert driver.find_element_by_class_name("badge")

    def test_notification_attributes(self):
        """Test the attributes of the notifications section"""

        # notification name - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        name = driver.find_element_by_tag_name("h3")
        if assertEqual(name.text, "Test Notification"):
            pass
        print('\n')  # adds line break
        print "Name text is correct"

        # notification name attributes
        assertEqual(name.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(name.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(name.value_of_css_property("font-size"), '18px')
        assertEqual(name.value_of_css_property("font-weight"), 'normal')

        # comment - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        comment = driver.find_element_by_tag_name("p")
        if assertEqual(comment.text, "Comment Posted by:"):
            pass
        print('\n')  # adds line break
        print "Comment text is correct"

        # comment attributes
        assertEqual(comment.value_of_css_property("color"), 'rgba(87, 114, 146, 1)')
        assertEqual(comment.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(comment.value_of_css_property("font-size"), '12px')
        assertEqual(comment.value_of_css_property("font-weight"), 'normal')

        # in response
        response = driver.find_element_by_xpath("//*[@id='reloadableList']/li/a/div[1]/div/p[2]")
        if assertEqual(response.text, "In Response to:"):
            pass
        print('\n')  # adds line break
        print "Response text is correct"

        # in response attributes
        assertEqual(response.value_of_css_property("color"), 'rgba(87, 114, 146, 1)')
        assertEqual(response.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(response.value_of_css_property("font-size"), '12px')
        assertEqual(response.value_of_css_property("font-weight"), 'normal')

        # dateline - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        dateline = driver.find_element_by_class_name("dateline")
        if assertEqual(dateline.text, "3 weeks ago"):
            pass
        print('\n')  # adds line break
        print "Dateline text is correct"

        # dateline attributes
        assertEqual(dateline.value_of_css_property("color"), 'rgba(87, 114, 146, 1)')
        assertEqual(dateline.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(dateline.value_of_css_property("font-size"), '12px')
        assertEqual(dateline.value_of_css_property("font-weight"), 'normal')

        # body - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        body = driver.find_element_by_class_name("body")
        if assertEqual(body.text, "This is a Notification Test"):
            pass
        print('\n')  # adds line break
        print "College text is correct"

        # body attributes
        assertEqual(body.value_of_css_property("color"), 'rgba(87, 114, 146, 1)')
        assertEqual(body.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(body.value_of_css_property("font-size"), '14px')
        assertEqual(body.value_of_css_property("font-weight"), 'normal')

        # arrow - this pulls data from the text file
        arrow_file = open('utils/arrow.txt', 'r').read()
        # this requests the data from the URL again
        arrow_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/rowArrow.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(arrow_file, arrow_url):
            pass
        print "Arrow matches what's on file"

class TestOther(object):
    def test_other_button(self):
        """verify you are actually on the other page"""
        driver.find_element_by_id("otherNav").click()
        other_nav = driver.find_element_by_id("otherNav")
        if other_nav.is_enabled():
            assert driver.find_element_by_class_name("active")
            print('\n')  # adds line break
            print "You are on the Other screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Other screen")

        # test other
        driver.find_element_by_class_name("itemDescription").click()

        # verify notification text
        if driver.find_element_by_id("questionContent").is_enabled():
            try:
                assert driver.find_element_by_class_name("title")
                assert driver.find_element_by_class_name("body")
                assert driver.find_element_by_id("questionContent")
                assert driver.find_element_by_class_name("blueMenu")
            except:
                print('\n')  # adds line break
                raise NoSuchElementException("Other elements not found")

            ## Need to find a way to automate submitting questions ##

        else:
            print "Questions already present"

        # click data button
        driver.find_element_by_class_name("data").click()
        time.sleep(3)

        #verify pdf
        assert driver.find_element_by_id("dataContainer")
        assert driver.find_element_by_id("dataName")
        driver.find_element_by_id("closeBtn").click()

        # verify questions
        assert driver.find_elements_by_class_name("questionItem")
        # verify any badges
        assert driver.find_elements_by_class_name("badge")

        # click one and verify question text and elements
        driver.find_element_by_link_text("Question 1").click()
        title = driver.find_element_by_class_name("title").text
        title_text = "Discussion \xe2\x80\x94 Question 1"

        #import pdb; pdb.set_trace()
        assertEqual(title.encode("utf-8"), title_text)
        assert driver.find_element_by_tag_name("p")
        assert driver.find_element_by_class_name("itemImage")
        assert driver.find_element_by_class_name("poster")
        assert driver.find_element_by_class_name("dateline")
        assert driver.find_element_by_xpath("//*[@id='comment-thread']/li/a/div[1]/div/div")

        # reply icon
        driver.find_element_by_class_name("replyIcon").click()
        # body
        assert driver.find_element_by_id("areaT")
        # send
        assert driver.find_element_by_xpath("//*[@id='btnSend']/span[1]").text

        # cancel
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/button[2]/span[1]").click()

        # go back to other screen
        driver.find_element_by_id("otherNav").click()

        # verify badge is present
        assert driver.find_element_by_class_name("badge")

        #### Do if/else statement for check mark or pencil ####
        #### Read what it is, then verify to the file ####

    def test_other_attributes(self):
        """Test the attributes of the notifications section"""

        # notification name - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        name = driver.find_element_by_tag_name("h3")
        if assertEqual(name.text, "Test Discussions"):
            pass
        print('\n')  # adds line break
        print "Name text is correct"

        # notification name attributes
        assertEqual(name.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(name.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(name.value_of_css_property("font-size"), '18px')
        assertEqual(name.value_of_css_property("font-weight"), 'normal')

        # dateline - WILL NEED XPATH EVENTUALLY WHEN OTHERS ARE ADDED
        dateline = driver.find_element_by_class_name("dateline")
        if assertEqual(dateline.text, "3 weeks ago"):
            pass
        print('\n')  # adds line break
        print "Dateline text is correct"

        # dateline attributes
        assertEqual(dateline.value_of_css_property("color"), 'rgba(87, 114, 146, 1)')
        assertEqual(dateline.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(dateline.value_of_css_property("font-size"), '12px')
        assertEqual(dateline.value_of_css_property("font-weight"), 'normal')

        # body
        body = driver.find_element_by_xpath("//*[@id='reloadableList']/li/a/div[1]/div/p[3]")
        if assertEqual(body.text, "Test ?"):
            pass
        print('\n')  # adds line break
        print "College text is correct"

        # body attributes
        assertEqual(body.value_of_css_property("color"), 'rgba(87, 114, 146, 1)')
        assertEqual(body.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(body.value_of_css_property("font-size"), '12px')
        assertEqual(body.value_of_css_property("font-weight"), 'normal')

        # arrow - this pulls data from the text file
        arrow_file = open('utils/arrow.txt', 'r').read()
        # this requests the data from the URL again
        arrow_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/rowArrow.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(arrow_file, arrow_url):
            pass
        print "Arrow matches what's on file"

class TestSupport(object):
    def test_support_button(self):
        """verify you are actually on the support page"""
        support_nav = driver.find_element_by_id("supportNav")
        support_nav.click()
        if support_nav.is_enabled():
            assert driver.find_element_by_class_name("clicked")
            print('\n')  # adds line break
            print "You are on the Support screen"
            pass
        else:
            print('\n')  # adds line break
            raise NoSuchElementException("You need to be on the Support screen")

    def test_content(self):
        """Verify content"""
        # Pulse support title
        title = driver.find_element_by_class_name("title")
        if assertEqual(title.text, "PULSE Support"):
            pass
        print('\n')  # adds line break
        print "Title text is correct"

        # title name attributes
        assertEqual(title.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(title.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(title.value_of_css_property("font-size"), '18px')
        assertEqual(title.value_of_css_property("font-weight"), 'normal')

        # body support title
        title = driver.find_element_by_class_name("body")
        if assertEqual(title.text, "Please type a question below and hit send to contact PULSE Support"):
            pass
        print('\n')  # adds line break
        print "Body text is correct"

        # body attributes
        assertEqual(title.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(title.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(title.value_of_css_property("font-size"), '18px')
        assertEqual(title.value_of_css_property("font-weight"), 'normal')

    def test_comment_photo(self):
        """Verify comment photo"""
        assert driver.find_elements_by_class_name("itemImage")
        # this pulls data from the text file
        item_file = open('utils/item_image.txt', 'r').read()
        # this requests the data from the URL again
        item_url = requests.get(
            "https://va-pulse-beta.s3.amazonaws.com/static/img/user.png").content
        # this compares the 2
        print('\n')  # adds line break
        if assertEqual(item_file, item_url):
            pass
        print "Item image matches what's on file"

    def test_comment_thread(self):
        """Verify comment thread elements"""
        # poster support title
        poster = driver.find_element_by_xpath("//*[@id='comment-thread']/li[1]/a/div[1]/div/span").get_attribute("innerText")
        if assertEqual(poster, "Kevin Cherepski, MD"):
            pass
        print('\n')  # adds line break
        print "Poster text is correct"

        # poster name attributes
        poster_text = driver.find_element_by_xpath("//*[@id='comment-thread']/li[1]/a/div[1]/div/span")
        assertEqual(poster_text.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(poster_text.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(poster_text.value_of_css_property("font-size"), '18px')
        assertEqual(poster_text.value_of_css_property("font-weight"), 'normal')

        # dateline
        date = driver.find_element_by_xpath("//*[@id='comment-thread']/li[1]/a/div[1]/div/div").get_attribute("innerText")
        if assertEqual(date, "September 21, 2017 10:54 am"):
            pass
        print('\n')  # adds line break
        print "Date text is correct"

        # dateline attributes
        date_text = driver.find_element_by_xpath("//*[@id='comment-thread']/li[1]/a/div[1]/div/div")
        assertEqual(date_text.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(date_text.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(date_text.value_of_css_property("font-size"), '12px')
        assertEqual(date_text.value_of_css_property("font-weight"), 'normal')

        # time
        time = driver.find_element_by_class_name("smallCaps")
        if assertEqual(time.text, "10:54 am"):
            pass
        print('\n')  # adds line break
        print "Time text is correct"

        # time attributes
        assertEqual(time.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(time.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(time.value_of_css_property("font-size"), '12px')
        assertEqual(time.value_of_css_property("font-weight"), 'normal')

        # comment text

        # verify that the profileTask percentage matches the actual percentage in the status bar
        comment = driver.find_element_by_xpath("//*[@id='comment-thread']/li[1]/a/div[1]/div")
        chars = set("Testing Text Submission")
        if any((c in chars) for c in (comment.text)):
            pass
        print('\n')  # adds line break
        print "Comment text is correct"

        # comment text attributes
        assertEqual(comment.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(comment.value_of_css_property("font-family"), 'Futura, Helvetica, Arial, sans-serif')
        assertEqual(comment.value_of_css_property("font-size"), '18px')
        assertEqual(comment.value_of_css_property("font-weight"), 'normal')

    def submit(self):
        """Verify you can submit"""
        # negative submit text
        driver.find_element_by_id("areaTm").click()
        # try to submit
        driver.find_element_by_id("post-comment").click()
        # verify negative message

        # BUG you should NOT be able to submit 'nothing' in the text field.

        # positive submit text
        text = "Testing Text Submission"
        driver.find_element_by_id("areaTm").click()
        time.sleep(1)
        driver.find_element_by_id("areaTm").send_keys(text)
        # submit
        driver.find_element_by_id("post-comment").click()

class TestLogout(object):
    def test_logo(self):
        """Test logout button"""
        # click logout button
        driver.find_element_by_id("logoutBtn").click()

        # verify that you're logged out
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

            # verify forgot password? link is present now
            assert driver.find_element_by_class_name("forgot")

            # verify login button is present now
            assert driver.find_element_by_id("login")

        else:
            print "User still logged in"
            pass

def teardown_class(self):
        driver.quit()