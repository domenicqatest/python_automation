### The commented out info below is ALL OUTDATED! ###

#"""Be sure to connect to the iOS server!"""
#java -jar jars/ios-server-standalone-0.6.6-SNAPSHOT.jar

#Try this:
#http://ios-driver.github.io/ios-driver/?page=safari


from selenium import webdriver
import time

# iphone
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                #'app': '[app]'
                'browserName': 'safari',
                'platformName': 'iOS',
                'platformVersion': '10.3',
                'deviceName': 'iPhone 6',
                'orientation': 'LANDSCAPE'
            })
# ipad
#driver = webdriver.Remote("http://localhost:5555/wd/hub", webdriver.DesiredCapabilities.IPAD)

def test_carrot_site():
    """Test site opens"""
    driver.get("http://beta.aml.star-application.com/")
    time.sleep(3)

def teardown_class(self):
        driver.quit()