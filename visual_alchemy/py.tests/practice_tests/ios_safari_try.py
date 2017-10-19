### The commented out info below is ALL OUTDATED! ###

#"""Be sure to connect to the iOS server!"""
#java -jar jars/ios-server-standalone-0.6.6-SNAPSHOT.jar

#Try this:
#http://ios-driver.github.io/ios-driver/?page=safari


from selenium import webdriver
from assertlib import assertEqual, assertAtleast, assertTrue
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

class TestLogin(object):

    def test_pulse_login(self):
        """Test login opens"""
        driver.get("http://pulse.beta.visual-a.com/")
        time.sleep(3)

        # Is login present?

        user = driver.find_element_by_id("id_username")

        if user.is_displayed():

            # Log into the web app: developer/imagine1
            driver.find_element_by_class_name("input").click()

            username = "developer"
            password = "imagine1"
            driver.find_element_by_class_name("input").click()
            time.sleep(1)
            driver.find_element_by_id("id_username").send_keys(username)
            driver.find_element_by_id("id_password").send_keys(password)

            driver.find_element_by_id("login").click()
            time.sleep(1)

        else:
            print "User already logged in."

class TestHome(object):
    def test_logo(self):
        """Test homepage attributes"""
        # logoWrapper
        logo = driver.find_element_by_class_name("logoWrapper")
        print('\n')  # adds line break
        print "size of the header is:"
        print (logo.size)

        assertEqual(logo.size["width"], 276)
        assertEqual(logo.size["height"], 115)

        print('\n')  # adds line break
        print "location of background is at:"
        print (logo.location)

        assertEqual(logo.location, {"y": 10.0, "x": 10.0})

    def test_event_title(self):
        title = driver.find_element_by_css_selector("h1").text
        if assertEqual(title, "ASH 2016"):
            pass
        print('\n')  # adds line break
        print title

        date = driver.find_element_by_css_selector("h2").text
        #date = driver.find_element_by_xpath("//*[@id='contentHeader']/div[2]/h2[1]").text
        if assertEqual(date, "December 03-06, 2016"):
            pass
        print('\n')  # adds line break
        print date

        city = driver.find_element_by_xpath("//*[@id='contentHeader']/div[2]/h2[2]").text
        if assertEqual(city, "San Diego, CA"):
            pass
        print('\n')  # adds line break
        print city

def teardown_class(self):
        driver.quit()