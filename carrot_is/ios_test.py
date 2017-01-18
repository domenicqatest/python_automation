#"""Be sure to connect to the Selendroid server!"""
#java -jar jars/ios-server-standalone-0.6.6-SNAPSHOT.jar

from selenium import webdriver
import time

# iphone
driver = webdriver.Remote("http://localhost:5555/wd/hub", webdriver.DesiredCapabilities.IPHONE)
# ipad
#driver = webdriver.Remote("http://localhost:5555/wd/hub", webdriver.DesiredCapabilities.IPAD)

def test_carrot_site(self):
    """Test site opens"""

    driver.get("http://carrot.is/")
    time.sleep(3)

def teardown_class(self):
        driver.quit()

