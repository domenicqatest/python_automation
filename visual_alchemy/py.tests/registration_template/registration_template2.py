# -*- coding: utf-8 -*-

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from selenium.webdriver.support.select import Select
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
import requests
import time

base_url = "http://registration.agios.va-dev.net/23/"

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

class TestFillingPage1Form(object):

    def page_1_form(self):
        """Filling out the form"""

        # are you on page 1?
        assertEqual(driver.title, 'Program Registration')
        time.sleep(1)
        Select(driver.find_element_by_id("id_month")).select_by_visible_text("2017 April")
        time.sleep(1)
        Select(driver.find_element_by_id("id_event")).select_by_visible_text("Venue Program: #23")
        driver.find_element_by_css_selector("button.button").click()

        try:
            driver.switch_to_alert().accept()
        except NoAlertPresentException as e:
            print('\n')  # adds line break
            print("no alert")
            print('\n')  # adds line break

        time.sleep(1)
        driver.get(base_url)
        time.sleep(3)

class TestPage2Elements(object):

    # Background
    def test_background(self):
        """Test correct background is present"""

        # are you on page 2?
        assertEqual(driver.title, 'Program Registration')
        print('\n' * 2)  # adds line break
        bg = driver.find_element_by_class_name("container")

        if bg.is_displayed():
            print "background found"
        else:
            print "background not found"

    def test_correct_background(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        bg_file = open('utils/background.txt', 'r').read()
        # this requests the data from the URL again
        bg_url = requests.get("https://va-mosaic-agios-beta.s3.amazonaws.com/images/main-bg.jpg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(bg_file, bg_url):
            print "background does not match file"
        else:
            print "background matches file"

    def test_bg_size(self):
        """Is the size correct?"""

        bg = driver.find_element_by_class_name("container")
        size = bg.size
        print('\n')  # adds line break
        print "size of the background is:"
        print (size)

        assertEqual(bg.size["width"], 750)
        assertEqual(bg.size["height"], 1527)

    def test_bg_placement(self):
        """Is the placement correct"""

        bg = driver.find_element_by_class_name("container")
        print('\n')  # adds line break
        print "location of background is at:"
        print (bg.location)

        assertEqual(bg.location, {"y": 50.0, "x": 74.0})

    # Header
    def test_header(self):
        """Test correct container present"""

        print('\n' * 2)  # adds line break
        header = driver.find_element_by_id("header")

        if header.is_displayed():
            print "header found"
        else:
            print "header not found"

    def test_correct_header_size(self):
        """Is the size correct?"""

        header = driver.find_element_by_id("header")
        size = header.size
        print('\n')  # adds line break
        print "size of the header is:"
        print (size)

        assertEqual(header.size["width"], 746)
        assertEqual(header.size["height"], 146)

    def test_header_placement(self):
        """Is the placement correct"""

        header = driver.find_element_by_id("header")
        print('\n')  # adds line break
        print "location of header is at:"
        print (header.location)

        assertEqual(header.location, {"y": 52.0, "x": 76.0})

        # header background color
        header = driver.find_element_by_id("header")
        assertEqual(header.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')

    # Container
    def test_container(self):
        """Test correct container present"""
        print('\n' * 2)  # adds line break
        container = driver.find_element_by_class_name("container")

        if container.is_displayed():
            print "container found"
        else:
            print "container not found"

    def test_correct_container_size(self):
        """Is the size correct?"""

        container = driver.find_element_by_class_name("container")
        size = container.size
        print('\n')  # adds line break
        print "size of the container is:"
        print (size)

        assertEqual(container.size["width"], 750)
        assertEqual(container.size["height"], 1527)

    def test_container_placement(self):
        """Is the placement correct"""

        container = driver.find_element_by_class_name("container")
        print('\n')  # adds line break
        print "location of container is at:"
        print (container.location)

        assertEqual(container.location, {"y": 50.0, "x": 74.0})

        # Container colors and attributes
        container = driver.find_element_by_class_name("container")
        assertEqual(container.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(container.value_of_css_property("background-color"), 'rgba(255, 255, 255, 1)')
        assertEqual(container.value_of_css_property("border-bottom-color"), 'rgba(0, 0, 0, 1)')
        assertEqual(container.value_of_css_property("border-left-color"), 'rgba(0, 0, 0, 1)')
        assertEqual(container.value_of_css_property("border-right-color"), 'rgba(0, 0, 0, 1)')
        assertEqual(container.value_of_css_property("border-top-color"), 'rgba(0, 0, 0, 1)')

        assertEqual(container.value_of_css_property("line-height"), '20px')
        assertEqual(container.value_of_css_property("margin-bottom"), '50px')
        assertEqual(container.value_of_css_property("margin-left"), '74px')
        assertEqual(container.value_of_css_property("margin-right"), '74px')
        assertEqual(container.value_of_css_property("margin-top"), '0px')
        assertEqual(container.value_of_css_property("max-width"), '817px')

    # Content
    def test_content(self):
        """This tests the attributes of the content section"""

        # location
        content = driver.find_element_by_id("content")
        print('\n')  # adds line break
        print "location of content cell is at:"
        print (content.location)

        # size
        content = driver.find_element_by_id("content")
        size = content.size
        print('\n')  # adds line break
        print "size of the content cell is:"
        print (size)

        assertEqual(content.size["width"], 630)
        assertEqual(content.size["height"], 960)

        # Register here...
        font_large = driver.find_element_by_css_selector("h2.font-large").text
        if assertEqual(font_large, "Register here to participate in an upcoming program on Characterizing the Molecular Heterogeneity of Acute Myeloid Leukemia (AML)."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'",font_large,"'"," text is present"

        register = driver.find_element_by_class_name("font-large")
        assertEqual(register.value_of_css_property("color"), 'rgba(3, 78, 128, 1)')
        assertEqual(register.value_of_css_property("font-family"), '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(register.value_of_css_property("font-size"), '25px')
        assertEqual(register.value_of_css_property("font-weight"), '500')

        # Title
        title = driver.find_element_by_css_selector("h3.title").text
        if assertEqual(title, "Program Information"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", title, "'", " text is present"

class TestProgramDetails(object):
    def test_program_details(self):
        """This focuses on the program details' attributes"""
        print('\n')  # adds line break
        print "Program Information is:"
        print('\n')  # adds line break

        date = driver.find_element_by_css_selector("b")
        assertEqual(date.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(date.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(date.value_of_css_property("font-size"), '14px')
        assertEqual(date.value_of_css_property("font-weight"), 'bold')
        print date.text

        time = driver.find_element_by_xpath("//*[@id='program-details']/div/div[2]")
        assertEqual(time.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(time.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(time.value_of_css_property("font-size"), '14px')
        assertEqual(time.value_of_css_property("font-weight"), 'normal')
        print time.text

        presenter1 = driver.find_element_by_xpath("//div[@id='program-details']/div/div[3]")
        assertEqual(presenter1.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(presenter1.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(presenter1.value_of_css_property("font-size"), '14px')
        assertEqual(presenter1.value_of_css_property("font-weight"), 'normal')
        print presenter1.text

        presenter2 = driver.find_element_by_xpath("//div[@id='program-details']/div/div[3]/b")
        assertEqual(presenter2.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(presenter2.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(presenter2.value_of_css_property("font-size"), '14px')
        assertEqual(presenter2.value_of_css_property("font-weight"), 'bold')

        venue = driver.find_element_by_xpath("//div[@id='program-details']/div/div[4]")
        assertEqual(venue.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(venue.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(venue.value_of_css_property("font-size"), '14px')
        assertEqual(venue.value_of_css_property("font-weight"), 'normal')
        print venue.text

        host1 = driver.find_element_by_xpath("//div[@id='program-details']/div/div[5]")
        assertEqual(host1.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(host1.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(host1.value_of_css_property("font-size"), '14px')
        assertEqual(host1.value_of_css_property("font-weight"), 'normal')
        print host1.text

        host2 = driver.find_element_by_xpath("//div[@id='program-details']/div/div[5]/b")
        assertEqual(host2.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(host2.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(host2.value_of_css_property("font-size"), '14px')
        assertEqual(host2.value_of_css_property("font-weight"), 'bold')

class TestProfessionalInformation(object):
    """This tests the professional information section"""

    def test_correct_professional_text1(self):
        """See if the text matches and send keys"""

        # this pulls data from the text file
        professional_file = open('utils/professional.txt', 'r').read()
        # this requests the data from the URL again
        professional_text = driver.find_element_by_xpath("//*[@id='program-details']/p[1]").text

        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(professional_file, professional_text):
            print "text does not match file"
        else:
            print "text matches file"
            print('\n')  # adds line break
            print professional_text

        # please complete the following information...
        please_text = driver.find_element_by_xpath("//*[@id='program-details']/p[1]")
        assertEqual(please_text.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(please_text.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(please_text.value_of_css_property("font-size"), '14px')
        assertEqual(please_text.value_of_css_property("font-weight"), 'normal')

        # email
        email = driver.find_element_by_xpath("//*[@id='program-details']/p/a")
        assertEqual(email.value_of_css_property("color"), 'rgba(51, 122, 183, 1)')
        assertEqual(email.value_of_css_property("font-family"), '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(email.value_of_css_property("font-size"), '14px')
        assertEqual(email.value_of_css_property("font-weight"), 'normal')

        # phone number...
        phone_text = driver.find_element_by_xpath("//*[@id='program-details']/p/b")
        assertEqual(phone_text.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(phone_text.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(phone_text.value_of_css_property("font-size"), '14px')
        assertEqual(phone_text.value_of_css_property("font-weight"), 'bold')

        # this is the required field text.
        required_text1 = driver.find_element_by_xpath("//*[@id='register-form']/div/p").text

        if assertEqual(required_text1, "*This is a required field."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'",required_text1,"'"," text is present"

        # attributes
        required_text = driver.find_element_by_xpath("//*[@id='register-form']/div/p")
        assertEqual(required_text.value_of_css_property("color"), 'rgba(255, 0, 0, 1)')
        assertEqual(required_text.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(required_text.value_of_css_property("font-size"), '18px')
        assertEqual(required_text.value_of_css_property("font-weight"), 'normal')

    def test_form_titles(self):
        """This will test the drop down form titles"""

        first_text = driver.find_element_by_css_selector("label").text
        if assertEqual(first_text, "First name:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", first_text, "'", " text is present"

        first = driver.find_element_by_css_selector("label")
        assertEqual(first.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(first.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(first.value_of_css_property("font-size"), '14px')
        assertEqual(first.value_of_css_property("font-weight"), 'bold')

        first_term = "First"
        driver.find_element_by_id("id_registrants-0-first_name").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-first_name").send_keys(first_term)
        time.sleep(1)

        middle_text = driver.find_element_by_xpath("//label[@for='id_registrants-0-middle_name']").text
        if assertEqual(middle_text, "Middle name:"):
             print('\n')  # adds line break
             print "text not found"
        else:
             print('\n')  # adds line break
             print "'", middle_text, "'", " text is present"

        middle = driver.find_element_by_xpath("//label[@for='id_registrants-0-middle_name']")
        assertEqual(middle.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(middle.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(middle.value_of_css_property("font-size"), '14px')
        assertEqual(middle.value_of_css_property("font-weight"), 'bold')

        middle_term = "Middle"
        driver.find_element_by_id("id_registrants-0-middle_name").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-middle_name").send_keys(middle_term)
        time.sleep(1)

        last_text = driver.find_element_by_xpath("//label[@for='id_registrants-0-last_name']").text
        if assertEqual(last_text, "Last name:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", last_text, "'", " text is present"

        last = driver.find_element_by_xpath("//label[@for='id_registrants-0-last_name']")
        assertEqual(last.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(last.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(last.value_of_css_property("font-size"), '14px')
        assertEqual(last.value_of_css_property("font-weight"), 'bold')

        last_term = "Last"
        driver.find_element_by_id("id_registrants-0-last_name").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-last_name").send_keys(last_term)
        time.sleep(1)

        state_text = driver.find_element_by_xpath("//label[@for='id_registrants-0-state']").text
        if assertEqual(state_text, "State:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", state_text, "'", " text is present"

        state = driver.find_element_by_xpath("//label[@for='id_registrants-0-state']")
        assertEqual(state.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(state.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(state.value_of_css_property("font-size"), '14px')
        assertEqual(state.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-state")).select_by_visible_text("AK")

        # BEGIN WITH TESTING ALL THE PROFESSIONAL DROPDOWN OPTIONS AND VERIFYING THOSE REQUIRED FIELDS.
        # THEN LASTLY, SELECT THE 'I AM A PROFESSIONAL LICENSED TO PRESCRIBE' OPTION
        # BECAUSE IT FULFILLS ALL OF THE DROPDOWN REQUIREMENTS. #####

class TestHealthcareNoPrescribe(object):
    """This tests the professional information section if 'I am a healthcare professional, NOT licensed to prescribe' is chosen"""

    def test_stars_section1(self):
        """All that needs checked is the 'required fields'since it's almost the same as the previous option"""

        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am a healthcare professional, NOT licensed to prescribe")
        time.sleep(1)

        # required field stars
        stars = driver.find_elements_by_class_name("star")[0 - 15]
        print('\n')  # adds line break

        if stars.is_displayed():
            print "Relevant fields NOT all marked as required"
        else:
            print "Relevant fields marked as required"

class TestNotHealthcareProfessional(object):
    """This tests the professional information section if 'I am not a healthcare professional' is chosen"""

    def test_stars_section2(self):
        """All that needs checked is the 'required fields'since it's almost the same as the first option"""

        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am not a healthcare professional")
        time.sleep(1)

        # required field stars
        stars = driver.find_elements_by_class_name("star")[0 - 12]
        print('\n')  # adds line break

        if stars.is_displayed():
            print "Relevant fields NOT all marked as required"
        else:
            print "Relevant fields marked as required"

class TestCelgeneAgiosProfessional(object):
    """This tests the professional information section if 'I am not a healthcare professional' is chosen"""

    def test_stars_section2(self):
        """All that needs checked is the 'required fields'since it's almost the same as the first option"""

        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am a Celgene or Agios professional")
        time.sleep(1)

        # required field stars
        stars = driver.find_elements_by_class_name("star")[0 - 11]
        print('\n')  # adds line break

        if stars.is_displayed():
            print "Relevant fields NOT all marked as required"
        else:
            print "Relevant fields marked as required"

class TestHealthcarePrescribe(object):
    """This tests the professional information section if 'I am a healthcare professional, licensed to prescribe' is chosen... This satisfies all dropdown requirements"""

    def test_correct_professional_text1(self):
        """This tests the form scenario when 'I am a healthcare profession, licensed to prescribe' option is chosen"""

        # choose 'I am a healthcare professional, licensed to prescribe'
        healthcare_text = driver.find_element_by_xpath("//label[@for='id_registrants-0-ecp']").text
        if assertEqual(healthcare_text, "Are you a healthcare professional?:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", healthcare_text, "'", " text is present"

        healthcare = driver.find_element_by_xpath("//label[@for='id_registrants-0-ecp']")
        assertEqual(healthcare.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(healthcare.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(healthcare.value_of_css_property("font-size"), '14px')
        assertEqual(healthcare.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am a healthcare professional, licensed to prescribe")
        time.sleep(1)

    def test_record_pop_up(self):
        """This tests the form scenario when 'I am a healthcare profession, licensed to prescribe' option is chosen"""

        choices_text = driver.find_element_by_xpath("//*[@id='npi_picker_container']/div/div/div[1]/h3").text
        if assertEqual(choices_text, "Please select from the choices below."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", choices_text, "'", " text is present"

        choices = driver.find_element_by_xpath("//*[@id='npi_picker_container']/div/div/div[1]/h3")
        assertEqual(choices.value_of_css_property("color"), 'rgba(4, 75, 123, 1)')
        assertEqual(choices.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(choices.value_of_css_property("font-size"), '24px')
        assertEqual(choices.value_of_css_property("font-weight"), '500')

        sorry_text = driver.find_element_by_xpath("//*[@id='npi_picker_table']/p").text
        if assertEqual(sorry_text, "Sorry, no results were returned."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", sorry_text, "'", " text is present"

        sorry = driver.find_element_by_xpath("//*[@id='npi_picker_table']/p")
        assertEqual(sorry.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(sorry.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(sorry.value_of_css_property("font-size"), '14px')
        assertEqual(sorry.value_of_css_property("font-weight"), 'normal')

        pop_text = driver.find_element_by_xpath("//*[@id='btn_click_to_continue']").text
        if assertEqual(pop_text, "Not seeing your record? Click here to continue."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", pop_text, "'", " text is present"

        pop = driver.find_element_by_xpath("//*[@id='btn_click_to_continue']")
        assertEqual(pop.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(pop.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(pop.value_of_css_property("font-size"), '14px')
        assertEqual(pop.value_of_css_property("font-weight"), 'normal')
        assertEqual(pop.value_of_css_property("background-color"), 'rgba(204, 204, 204, 1)')

        # make sure 'X' is there
        assert driver.find_elements_by_class_name("close")

        # click the text close button
        driver.find_element_by_xpath("//*[@id='npi_picker_container']/div/div/div[1]/button").click()
        time.sleep(1)

    def test_title_section(self):
        """See if the title section is correct"""

        title_text = driver.find_element_by_xpath("//label[@for='id_registrants-0-salutation']").text
        if assertEqual(title_text, "Title:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", title_text, "'", " text is present"

        title = driver.find_element_by_xpath("//label[@for='id_registrants-0-salutation']")
        assertEqual(title.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(title.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(title.value_of_css_property("font-size"), '14px')
        assertEqual(title.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-salutation")).select_by_visible_text("Sir")

        # suffix
        #suffix_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[2]/label[1]").text
        #if assertEqual(suffix_text, "Suffix:"):
            #print('\n')  # adds line break
            #print "text not found"
        #else:
            #print('\n')  # adds line break
            #print "'", suffix_text, "'", " text is present"

        #suffix = driver.find_element_by_xpath("//*[@id='main_content_container']/div[2]/label[1]")
        #assertEqual(suffix.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        #assertEqual(suffix.value_of_css_property("font-family"),
                    #'"Helvetica Neue", Helvetica, Arial, sans-serif')
        #assertEqual(suffix.value_of_css_property("font-size"), '14px')
        #assertEqual(suffix.value_of_css_property("font-weight"), 'bold')

        # professional designation
        designation_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[3]/label[1]").text
        if assertEqual(designation_text, "Professional designation:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", designation_text, "'", " text is present"

        designation = driver.find_element_by_xpath("//*[@id='main_content_container']/div[3]/label[1]")
        assertEqual(designation.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(designation.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(designation.value_of_css_property("font-size"), '14px')
        assertEqual(designation.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-primary_degree")).select_by_visible_text("RPh")

        # primary degree other
        #degree_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[4]/label[1]").text
        #if assertEqual(degree_text, "Primary degree other:"):
            #print('\n')  # adds line break
            #print "text not found"
        #else:
            #print('\n')  # adds line break
            #print "'", degree_text, "'", " text is present"

        #degree = driver.find_element_by_xpath("//*[@id='main_content_container']/div[4]/label[1]")
        #assertEqual(degree.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        #assertEqual(degree.value_of_css_property("font-family"),
                    #'"Helvetica Neue", Helvetica, Arial, sans-serif')
        #assertEqual(degree.value_of_css_property("font-size"), '14px')
        #assertEqual(degree.value_of_css_property("font-weight"), 'bold')

        # affiliation/practice
        affiliation_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[5]/label[1]").text
        if assertEqual(affiliation_text, "Affiliation/Practice:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", affiliation_text, "'", " text is present"

        affiliation = driver.find_element_by_xpath("//*[@id='main_content_container']/div[5]/label[1]")
        assertEqual(affiliation.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(affiliation.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(affiliation.value_of_css_property("font-size"), '14px')
        assertEqual(affiliation.value_of_css_property("font-weight"), 'bold')

        affiliation_term = "Affiliation/Practice"
        driver.find_element_by_id("id_registrants-0-affiliation").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-affiliation").send_keys(affiliation_term)
        time.sleep(1)

        # specialty
        specialty_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[6]/label[1]").text
        if assertEqual(specialty_text, "Specialty:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", specialty_text, "'", " text is present"

        specialty = driver.find_element_by_xpath("//*[@id='main_content_container']/div[6]/label[1]")
        assertEqual(specialty.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(specialty.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(specialty.value_of_css_property("font-size"), '14px')
        assertEqual(specialty.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-specialty")).select_by_visible_text("Trauma & Acute Care Surgery")

        # specialty other
        #specialty_text2 = driver.find_element_by_xpath("//*[@id='main_content_container']/div[7]/label[1]").text
        #if assertEqual(specialty_text2, "Specialty other:"):
            #print('\n')  # adds line break
            #print "text not found"
        #else:
            #print('\n')  # adds line break
            #print "'", specialty_text2, "'", " text is present"

        #specialty2 = driver.find_element_by_xpath("//*[@id='main_content_container']/div[7]/label[1]")
        #assertEqual(specialty2.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        #assertEqual(specialty2.value_of_css_property("font-family"),
                    #'"Helvetica Neue", Helvetica, Arial, sans-serif')
        #assertEqual(specialty2.value_of_css_property("font-size"), '14px')
        #assertEqual(specialty2.value_of_css_property("font-weight"), 'bold')

        # NPI number
        npi_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[9]/label[1]").text
        if assertEqual(npi_text, "NPI number:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", npi_text, "'", " text is present"

        npi = driver.find_element_by_xpath("//*[@id='main_content_container']/div[9]/label[1]")
        assertEqual(npi.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(npi.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(npi.value_of_css_property("font-size"), '14px')
        assertEqual(npi.value_of_css_property("font-weight"), 'bold')

        NPI_term = "0123456789"
        driver.find_element_by_id("id_registrants-0-certification_npi_number").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-certification_npi_number").send_keys(NPI_term)
        time.sleep(1)

        # NPI checkbox
        npi_text2 = driver.find_element_by_xpath("//*[@id='main_content_container']/div[10]/label[1]").text
        if assertEqual(npi_text2, "I don't have an NPI number:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", npi_text2, "'", " text is present"

        npi2 = driver.find_element_by_xpath("//*[@id='main_content_container']/div[10]/label[1]")
        assertEqual(npi2.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(npi2.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(npi2.value_of_css_property("font-size"), '14px')
        assertEqual(npi2.value_of_css_property("font-weight"), 'bold')

        # check checkbox
        checkbox = driver.find_element_by_name("registrants-0-no_npi_number")
        checkbox.click()
        time.sleep(1)
        checkbox.click()
        time.sleep(1)

        # click here link - exit out of tab
        click_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/span/a").text
        if assertEqual(click_text, "Click here to search for your NPI number"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", click_text, "'", " text is present"

        click = driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/span/a")
        assertEqual(click.value_of_css_property("color"), 'rgba(51, 122, 183, 1)')
        assertEqual(click.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(click.value_of_css_property("font-size"), '14px')
        assertEqual(click.value_of_css_property("font-weight"), 'normal')

        driver.find_element_by_link_text("Click here to search for your NPI number").click()
        time.sleep(1)
        # put focus on newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        # close the tab
        driver.close()
        # switch to the main tab
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        # state license number
        license_text = driver.find_element_by_xpath("//*[@id='state-license-form']/div[2]/label[1]").text
        if assertEqual(license_text, "State license number:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", license_text, "'", " text is present"

        license = driver.find_element_by_xpath("//*[@id='state-license-form']/div[2]/label[1]")
        assertEqual(license.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(license.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(license.value_of_css_property("font-size"), '14px')
        assertEqual(license.value_of_css_property("font-weight"), 'bold')

        license_term = "0123456789"
        driver.find_element_by_id("id_registrants-0-state_licenses-0-license_number").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-state_licenses-0-license_number").send_keys(license_term)
        time.sleep(1)

        # add additional license number - THIS DOES NOT FUNCTION
        additional_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[13]/a").text
        if assertEqual(additional_text, "Add additional license |"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", additional_text, "'", " text is present"

        additional = driver.find_element_by_xpath("//*[@id='main_content_container']/div[13]/a")
        assertEqual(additional.value_of_css_property("color"), 'rgba(51, 122, 183, 1)')
        assertEqual(additional.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(additional.value_of_css_property("font-size"), '14px')
        assertEqual(additional.value_of_css_property("font-weight"), 'normal')

        # click additional
        # driver.find_element_by_xpath("//*[@id='main_content_container']/div[13]/a").click()

        # click to search license - exit out of tab
        search_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[13]/span/a").text
        if assertEqual(search_text, "Click here to search for your state license number"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", search_text, "'", " text is present"

        search = driver.find_element_by_xpath("//*[@id='main_content_container']/div[13]/span/a")
        assertEqual(search.value_of_css_property("color"), 'rgba(51, 122, 183, 1)')
        assertEqual(search.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(search.value_of_css_property("font-size"), '14px')
        assertEqual(search.value_of_css_property("font-weight"), 'normal')

        driver.find_element_by_link_text("Click here to search for your state license number").click()
        time.sleep(1)
        # put focus on newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        # close the tab
        driver.close()
        # switch to the main tab
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        # primary place of business name
        #business_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[14]/label[1]").text
        #if assertEqual(business_text, "Primary place of business name:"):
            #print('\n')  # adds line break
            #print "text not found"
        #else:
            #print('\n')  # adds line break
            #print "'", business_text, "'", " text is present"

        #business = driver.find_element_by_xpath("//*[@id='main_content_container']/div[14]/label[1]")
        #assertEqual(business.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        #assertEqual(business.value_of_css_property("font-family"),
                    #'"Helvetica Neue", Helvetica, Arial, sans-serif')
        #assertEqual(business.value_of_css_property("font-size"), '14px')
        #assertEqual(business.value_of_css_property("font-weight"), 'bold')

        # address 1
        address_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[15]/label[1]").text
        if assertEqual(address_text, "Address 1:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", address_text, "'", " text is present"

        address = driver.find_element_by_xpath("//*[@id='main_content_container']/div[15]/label[1]")
        assertEqual(address.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(address.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(address.value_of_css_property("font-size"), '14px')
        assertEqual(address.value_of_css_property("font-weight"), 'bold')

        address1_term = "123 Test Place"
        driver.find_element_by_id("id_address1").click()
        time.sleep(1)
        driver.find_element_by_id("id_address1").send_keys(address1_term)
        time.sleep(1)

        # address 2
        address2_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[16]/label[1]").text
        if assertEqual(address2_text, "Address 2:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", address2_text, "'", " text is present"

        address2 = driver.find_element_by_xpath("//*[@id='main_content_container']/div[16]/label[1]")
        assertEqual(address2.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(address2.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(address2.value_of_css_property("font-size"), '14px')
        assertEqual(address2.value_of_css_property("font-weight"), 'bold')

        address2_term = "Suite Test"
        driver.find_element_by_id("id_address2").click()
        time.sleep(1)
        driver.find_element_by_id("id_address2").send_keys(address2_term)
        time.sleep(1)

        # city
        city_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[17]/label[1]").text
        if assertEqual(city_text, "City:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", city_text, "'", " text is present"

        city = driver.find_element_by_xpath("//*[@id='main_content_container']/div[17]/label[1]")
        assertEqual(city.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(city.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(city.value_of_css_property("font-size"), '14px')
        assertEqual(city.value_of_css_property("font-weight"), 'bold')

        city_term = "City Test"
        driver.find_element_by_id("id_city").click()
        time.sleep(1)
        driver.find_element_by_id("id_city").send_keys(city_term)
        time.sleep(1)

        # state
        state_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[18]/label[1]").text
        if assertEqual(state_text, "State:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", state_text, "'", " text is present"

        state = driver.find_element_by_xpath("//*[@id='main_content_container']/div[18]/label[1]")
        assertEqual(state.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(state.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(state.value_of_css_property("font-size"), '14px')
        assertEqual(state.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_state")).select_by_visible_text("NY")

        # zip
        zip_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[20]/label[1]").text
        if assertEqual(zip_text, "Zip:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", zip_text, "'", " text is present"

        zip = driver.find_element_by_xpath("//*[@id='main_content_container']/div[20]/label[1]")
        assertEqual(zip.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(zip.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(zip.value_of_css_property("font-size"), '14px')
        assertEqual(zip.value_of_css_property("font-weight"), 'bold')

        zip_term = "10001"
        driver.find_element_by_id("id_zipcode").click()
        time.sleep(1)
        driver.find_element_by_id("id_zipcode").send_keys(zip_term)
        time.sleep(1)

        # phone number
        phone_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[22]/label[1]").text
        if assertEqual(phone_text, "Phone number:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", phone_text, "'", " text is present"

        phone = driver.find_element_by_xpath("//*[@id='main_content_container']/div[22]/label[1]")
        assertEqual(phone.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(phone.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(phone.value_of_css_property("font-size"), '14px')
        assertEqual(phone.value_of_css_property("font-weight"), 'bold')

        phone_term = "2125555555"
        driver.find_element_by_id("id_registrants-0-mobile_phone").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-mobile_phone").send_keys(phone_term)
        time.sleep(1)

        # email address
        email_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[24]/label[1]").text
        if assertEqual(email_text, "Email address:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", email_text, "'", " text is present"

        email = driver.find_element_by_xpath("//*[@id='main_content_container']/div[24]/label[1]")
        assertEqual(email.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(email.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(email.value_of_css_property("font-size"), '14px')
        assertEqual(email.value_of_css_property("font-weight"), 'bold')

        email_term = "test@example.com"
        driver.find_element_by_id("id_registrants-0-email").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-email").send_keys(email_term)
        time.sleep(1)

        # Before continuing, try to submit and test the "Please fill out all fields marked with an *." text.

        # button
        button = driver.find_element_by_class_name("button")
        # hover over the button
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()

    def test_correct_error(self):
        """See if the asterisks text matches"""

        # this pulls data from the text file
        asterisks_file = open('utils/register.txt', 'r').read()
        # this requests the data from the URL again
        asterisks = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div").text
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(asterisks_file, asterisks):
            print "Asterisks text does not match file"
        else:
            print "Asterisks text matches file"


        # confirm email
        confirm_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[25]/label[1]").text
        if assertEqual(confirm_text, "Confirm email:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", confirm_text, "'", " text is present"

        confirm = driver.find_element_by_xpath("//*[@id='main_content_container']/div[25]/label[1]")
        assertEqual(confirm.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(confirm.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(confirm.value_of_css_property("font-size"), '14px')
        assertEqual(confirm.value_of_css_property("font-weight"), 'bold')

        confirm_term = "test@example.com"
        driver.find_element_by_id("id_registrants-0-confirm_email").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-confirm_email").send_keys(confirm_term)
        time.sleep(1)

        # dietary restrictions
        dietary_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[26]/label[1]").text
        if assertEqual(dietary_text, "Dietary restrictions:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", dietary_text, "'", " text is present"

        dietary = driver.find_element_by_xpath("//*[@id='main_content_container']/div[26]/label[1]")
        assertEqual(dietary.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(dietary.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(dietary.value_of_css_property("font-size"), '14px')
        assertEqual(dietary.value_of_css_property("font-weight"), 'bold')

        dietary_term = "test test test"
        driver.find_element_by_id("id_registrants-0-dietary_restrictions").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-dietary_restrictions").send_keys(dietary_term)
        time.sleep(1)

        # opt out of meal / checkbox
        opt_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[27]/label[1]").text
        if assertEqual(opt_text, "Opt out of meal:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", opt_text, "'", " text is present"

        opt = driver.find_element_by_xpath("//*[@id='main_content_container']/div[27]/label[1]")
        assertEqual(opt.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(opt.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(opt.value_of_css_property("font-size"), '14px')
        assertEqual(opt.value_of_css_property("font-weight"), 'bold')

        # check checkbox2
        checkbox2 = driver.find_element_by_name("registrants-0-opt_out_of_meal")
        checkbox2.click()
        time.sleep(1)
        checkbox2.click()
        time.sleep(1)

        # required field stars
        stars = driver.find_elements_by_class_name("star")[0 - 16]
        print('\n')  # adds line break

        if stars.is_displayed():
            print "Relevant fields NOT all marked as required"
        else:
            print "Relevant fields marked as required"

class TestDropdownContents(object):

    def test_state_dropdown(self):
        """verifies the contents of the 1st state drop down"""

        state_dropdown = driver.find_elements_by_xpath("//*[@id='id_registrants-0-state']/option")
        state_list = [state_dropdown[i].text for i in xrange(51)]
        assertEqual(state_list,
                    [u'---------', u'AK', u'AL', u'AR', u'AZ', u'CA', u'CO', u'CT', u'DC', u'DE', u'FL', u'GA', u'HI',
                     u'IA', u'ID', u'IL', u'IN', u'KS', u'KY', u'LA', u'MA', u'MD', u'ME', u'MI', u'MN', u'MO', u'MS',
                     u'MT', u'NC', u'ND', u'NE', u'NH', u'NJ', u'NM', u'NV', u'NY', u'OH', u'OK', u'OR', u'PA', u'PR',
                     u'RI', u'SC', u'SD', u'TN', u'TX', u'UT', u'VA', u'VT', u'WA', u'WI']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-state']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    def test_state_dropdown2(self):
        """verifies the contents of the 2nd state dropdown"""

        state_dropdown2 = driver.find_elements_by_xpath("//*[@id='id_state']/option")
        state_list2 = [state_dropdown2[i].text for i in xrange(51)]
        print state_list2,

        assertEqual(state_list2,
                    [u'------', u'AK', u'AL', u'AR', u'AZ', u'CA', u'CO', u'CT', u'DC', u'DE', u'FL', u'GA', u'HI',
                     u'IA', u'ID', u'IL', u'IN', u'KS', u'KY', u'LA', u'MA', u'MD', u'ME', u'MI', u'MN', u'MO', u'MS',
                     u'MT', u'NC', u'ND', u'NE', u'NH', u'NJ', u'NM', u'NV', u'NY', u'OH', u'OK', u'OR', u'PA', u'PR',
                     u'RI', u'SC', u'SD', u'TN', u'TX', u'UT', u'VA', u'VT', u'WA', u'WI']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_state']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    def test_hp_dropdown2(self):
        """verifies the contents of the healthcare professional dropdown"""

        hp_dropdown = driver.find_elements_by_xpath("//*[@id='id_registrants-0-ecp']/option")
        hp_list = [hp_dropdown[i].text for i in xrange(5)]
        print hp_list,

        assertEqual(hp_list,
                    [u'---------',
                     u'I am a healthcare professional, licensed to prescribe',
                     u'I am a healthcare professional, NOT licensed to prescribe',
                     u'I am not a healthcare professional',
                     u'I am a Celgene or Agios professional']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-ecp']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    def test_title_dropdown2(self):
        """verifies the contents of the title dropdown"""

        title_dropdown = driver.find_elements_by_xpath("//*[@id='id_registrants-0-salutation']/option")
        title_list = [title_dropdown[i].text for i in xrange(9)]
        print title_list,

        assertEqual(title_list,
                    [u'---------', u'Dr.', u'Madam', u'Miss', u'Mr.', u'Mrs.', u'Ms.', u'Professor', u'Sir']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-salutation']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    def test_pd_dropdown2(self):
        """verifies the contents of the professional designation dropdown"""

        pd_dropdown = driver.find_elements_by_xpath("//*[@id='id_registrants-0-primary_degree']/option")
        pd_list = [pd_dropdown[i].text for i in xrange(29)]
        print pd_list,

        assertEqual(pd_list,
                    [u'---------',
                     u'APNP',
                     u'APRN',
                     u'ARNP',
                     u'BS',
                     u'CRNP',
                     u'DNP',
                     u'DO',
                     u'DO, MSc, FACP, FHM',
                     u'EdD',
                     u'JD',
                     u'LCSW',
                     u'LPN',
                     u'MBBCh',
                     u'MBBS',
                     u'MD',
                     u'MSN',
                     u'MSW',
                     u'N/A',
                     u'NP',
                     u'OD',
                     u'PA',
                     u'PharmD',
                     u'PhD',
                     u'PMHCNS-BC',
                     u'PMHNP-BC',
                     u'PsyD',
                     u'RN',
                     u'RPh']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-primary_degree']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    def test_specialty_dropdown(self):
        """verifies the contents of the specialty drop down"""

        specialty_dropdown = driver.find_elements_by_xpath("//*[@id='id_registrants-0-specialty']/option")
        specialty_list = [specialty_dropdown[i].text for i in xrange(41)]
        assertEqual(specialty_list,
                    [u'---------', u'Anesthesiology', u'Cardiology', u'Case Management', u'Clinical Pathology',
                     u'Clinical Pharmacology', u'Critical Care Medicine', u'Dietician', u'Emergency Medicine',
                     u'Endocrinology', u'Family Practice', u'General Practice', u'Genetic Counseling',
                     u'Genetic Oncologist', u'Hematologist-Oncologist', u'Hematology', u'Hospice', u'Internal Medicine',
                     u'Medical Oncology', u'Neurology', u'Nurse Practitioner', u'Orthopedic Oncology', u'Orthopedics',
                     u'Other', u'Pain Management', u'Palliative Care', u'Pathology', u'Pediatric Oncologist',
                     u'Pediatrician', u'Pharmacist', u'Pharmacy Technician', u'Physician Assistant', u'Primary Care',
                     u'Psychiatry', u'Radiation Oncology', u'Radiology', u'Rehabilitation Therapy', u'Social Worker',
                     u'Sports Medicine', u'Surgical Oncologist', u'Trauma & Acute Care Surgery']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-specialty']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

class TestSupportSection(object):
    """This tests the support section"""

    def test_support_section(self):
        """This tests the attributes of the support section"""

        # location
        support = driver.find_element_by_id("support-copy")
        print('\n')  # adds line break
        print "location of support cell is at:"
        print (support.location)

        # size
        support_cell = driver.find_element_by_id("support-copy")
        size = support_cell.size
        print('\n')  # adds line break
        print "size of the support cell is:"
        print (size)

        assertEqual(support_cell.size["width"], 630)
        assertEqual(support_cell.size["height"], 219)

        # title left
        title_left = driver.find_element_by_css_selector("h4.title.left").text
        if assertEqual(title_left, "ATTENDING AND REPORTING POLICY"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", title_left, "'", " text is present"

        attending = driver.find_element_by_css_selector("h4.title.left")
        assertEqual(attending.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(attending.value_of_css_property("font-family"), '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(attending.value_of_css_property("font-size"), '18px')
        assertEqual(attending.value_of_css_property("font-weight"), '500')

    def test_policy_text(self):
        """This will test the policy text"""

        #policy_text = driver.find_element_by_tag_name("p")
        policy_text = driver.find_element_by_xpath("//*[@id='support-copy']/div/p[1]").text
        policy = "In order to simplify processing on this joint initiative, Celgene and Agios will be utilizing Celgene’s reporting resources. Celgene is committed to adhering to the highest ethical standards and has adopted the revised PhRMA Code on Interactions with Health Care Professionals. In compliance with the US Physician Payments Sunshine Act, Celgene will report to CMS payments and other transfers of value made to US licensed physicians, including honoraria, travel, and meals. To learn more about how Celgene Corporation complies with the Sunshine Act, visit http://www.celgene.com/about/compliance/sunshine-act/."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(policy_text, unicode(policy, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", policy_text, "'", " text is present"

        policy_text2 = driver.find_element_by_css_selector("p")
        assertEqual(policy_text2.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(policy_text2.value_of_css_property("font-family"), '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(policy_text2.value_of_css_property("font-size"), '14px')
        assertEqual(policy_text2.value_of_css_property("font-weight"), 'normal')

        # link
        link = driver.find_element_by_xpath("//*[@id='support-copy']/div/p/a")
        assertEqual(link.value_of_css_property("color"), 'rgba(51, 122, 183, 1)')
        assertEqual(link.value_of_css_property("font-family"), '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(link.value_of_css_property("font-size"), '14px')
        assertEqual(link.value_of_css_property("font-weight"), 'normal')

    def test_click_link(self):
        """This will verify the link, click it, and close the new tab"""

        time.sleep(1)
        driver.find_element_by_link_text("http://www.celgene.com/about/compliance/sunshine-act/").click()
        time.sleep(3)
        # put focus on newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        # close the tab
        driver.close()
        # switch to the main tab
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

    # Footer
    def test_footer(self):
        """Test correct container present"""
        print('\n' * 2)  # adds line break
        footer = driver.find_element_by_id("footer")

        if footer.is_displayed():
            print "footer found"
        else:
            print "footer not found"

    def test_correct_footer_size(self):
        """Is the size correct?"""
        footer = driver.find_element_by_id("footer")
        size = footer.size
        print('\n')  # adds line break
        print "size of the header is:"
        print (size)

        assertEqual(footer.size["width"], 746)
        assertEqual(footer.size["height"], 148)

    def test_footer_placement(self):
        """Is the placement correct"""

        footer = driver.find_element_by_id("footer")
        print('\n')  # adds line break
        print "location of header is at:"
        print (footer.location)

        assertEqual(footer.location, {"y": 2817.0, "x": 76.0})

        # footer background color
        footer = driver.find_element_by_id("footer")
        assertEqual(footer.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')

        # line break
        hr = driver.find_element_by_xpath("//*[@id='footer']/hr")
        size = hr.size
        print('\n')  # adds line break
        print "size of the header is:"
        print (size)

        assertEqual(hr.size["width"], 746)
        assertEqual(hr.size["height"], 2)

        print('\n')  # adds line break
        print "location of header is at:"
        print (hr.location)

        assertEqual(hr.location, {"y": 2857.0, "x": 76.0})

        assertEqual(hr.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(hr.value_of_css_property("border-bottom-color"), 'rgba(51, 51, 51, 1)')
        assertEqual(hr.value_of_css_property("border-left-color"), 'rgba(51, 51, 51, 1)')
        assertEqual(hr.value_of_css_property("border-right-color"), 'rgba(51, 51, 51, 1)')
        assertEqual(hr.value_of_css_property("border-top-color"), 'rgba(161, 161, 161, 1)')
        assertEqual(hr.value_of_css_property("border-top-style"), 'solid')
        assertEqual(hr.value_of_css_property("display"), 'block')

class TestContainerObjects(object):

    # TOP Logo
    def test_logo(self):
        """Test correct logo present"""

        print('\n' * 2)  # adds line break
        logo = driver.find_elements_by_class_name("logo")[0]
        #logo = driver.find_element_by_xpath("//*[@id='header']/header/img")

        if logo.is_displayed():
            print "logo found"
        else:
            print "logo not found"

    def test_correct_logo(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        logo_file = open('utils/logo.txt', 'r').read()
        # this requests the data from the URL again
        svg_url = requests.get("https://va-mosaic-agios.s3.amazonaws.com/logos/agios-logo.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(logo_file, svg_url):
            print "image does not match file"
        else:
            print "image matches file"

    def test_correct_logo_size(self):
        """Is the size correct?"""

        logo = driver.find_elements_by_class_name("logo")[0]
        size = logo.size
        print('\n')  # adds line break
        print "size of the logo is:"
        print (size)

        assertEqual(logo.size["width"], 200)
        assertEqual(logo.size["height"], 86)

    def test_logo_placement(self):
        """Is the placement correct"""

        logo = driver.find_elements_by_class_name("logo")[0]
        print('\n')  # adds line break
        print "location of logo is at:"
        print (logo.location)

        assertEqual(logo.location, {"y": 72.0, "x": 86.0})

    # Header Border
    def test_header_border(self):
        """Test correct header present"""

        print('\n' * 2)  # adds line break
        header = driver.find_element_by_class_name("header-border")

        if header.is_displayed():
            print "header border found"
        else:
            print "header border not found"

    def test_correct_header(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        header_file = open('utils/header_border.txt', 'r').read()
        # this requests the data from the URL again
        header_url = requests.get(
            "https://va-mosaic-agios-beta.s3.amazonaws.com/images/agios/horizontal-bar.png").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(header_file, header_url):
            print "image does not match file"
        else:
            print "image matches file"

    def test_header_size(self):
        """Is the size correct?"""

        header = driver.find_element_by_class_name("header-border")
        size = header.size
        print('\n')  # adds line break
        print "size of the header is:"
        print (size)

        assertEqual(header.size["width"], 746)
        assertEqual(header.size["height"], 20)

    def test_header_placement(self):
        """Is the placement correct"""

        header = driver.find_element_by_class_name("header-border")
        print('\n')  # adds line break
        print "location of header border is at:"
        print (header.location)

        assertEqual(header.location, {"y": 178.0, "x": 76.0})

    # BOTTOM Logo
    def test_bottom_logo(self):
        """Test correct logo present"""

        print('\n' * 2)  # adds line break
        logo = driver.find_elements_by_class_name("logo")[1]
        #logo = driver.find_element_by_xpath("//*[@id='footer']/img")

        if logo.is_displayed():
            print "logo found"
        else:
            print "logo not found"

    def test_correct_bottom_logo(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        logo_file = open('utils/logo.txt', 'r').read()
        # this requests the data from the URL again
        svg_url = requests.get("https://va-mosaic-agios.s3.amazonaws.com/logos/agios-logo.svg").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(logo_file, svg_url):
            print "image does not match file"
        else:
            print "image matches file"

    def test_correct_bottom_logo_size(self):
        """Is the size correct?"""

        logo = driver.find_elements_by_class_name("logo")[1]
        size = logo.size
        print('\n')  # adds line break
        print "size of the logo is:"
        print (size)

        assertEqual(logo.size["width"], 200)
        assertEqual(logo.size["height"], 86)

    def test_bottom_logo_placement(self):
        """Is the placement correct"""

        logo = driver.find_elements_by_class_name("logo")[1]
        print('\n')  # adds line break
        print "location of logo is at:"
        print (logo.location)

        assertEqual(logo.location, {"y": 2879.0, "x": 349.0})

    def test_register_button(self):
        """register button attributes and finally, click register"""

        # button
        register = driver.find_element_by_class_name("button")
        size = register.size
        print('\n')  # adds line break
        print "size of the register button is:"
        print (size)

        assertEqual(register.size["width"], 200)
        assertEqual(register.size["height"], 40)

        assertEqual(register.value_of_css_property("background-color"), 'rgba(4, 75, 123, 1)')
        assertEqual(register.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')
        assertEqual(register.value_of_css_property("border-bottom-color"), 'rgba(255, 255, 255, 1)')
        assertEqual(register.value_of_css_property("border-left-color"), 'rgba(255, 255, 255, 1)')
        assertEqual(register.value_of_css_property("border-right-color"), 'rgba(255, 255, 255, 1)')
        assertEqual(register.value_of_css_property("border-top-color"), 'rgba(255, 255, 255, 1)')
        assertEqual(register.value_of_css_property("box-shadow"), 'rgba(0, 0, 0, 0.156863) 0px 3px 6px 0px, rgba(0, 0, 0, 0.227451) 0px 3px 6px 0px')

        register2 = driver.find_element_by_class_name("btn-wrapper")

        print('\n')  # adds line break
        print "location of registration button is at:"
        print (register2.location)

        assertEqual(register2.location, {"y": 2548.0, "x": 149.0})

        #button text
        reg_button_text = driver.find_element_by_xpath("//*[@id='bttn_register']")
        print('\n')  # adds line break
        if assertEqual(reg_button_text.get_attribute("innerText"), "REGISTER"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", reg_button_text.get_attribute("innerText"), "'", " text is present"

        registration = driver.find_element_by_xpath("//*[@id='bttn_register']")
        assertEqual(registration.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')
        assertEqual(registration.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(registration.value_of_css_property("font-size"), '14px')
        assertEqual(registration.value_of_css_property("font-weight"), 'normal')

        # SUBMIT
        time.sleep(3)
        driver.find_element_by_class_name("button").click()
        time.sleep(3)

    def teardown_class(self):
        driver.quit()

#   def setup_method(method):
#   def teardown_method(method):

#   def setup_class(cls):
#   def teardown_class(cls):