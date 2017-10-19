from selenium import webdriver
import time

driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                #'app': '[app]'
                'browserName': 'chrome',
                'platformName': 'Android',
                'platformVersion': '7.1.1',
                'deviceName': 'Android Emulator',
                'orientation': 'LANDSCAPE'
            })

def test_pulse_login():
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

def test_home():
    """Test homepage attributes"""


def teardown_class(self):
        driver.quit()