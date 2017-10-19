# -*- coding: utf-8 -*-

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from selenium.webdriver.support.select import Select
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time

base_url = "http://kcentra.reg-portal.va-dev.net/420/"

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

class TestMainPageElements(object):

    # Background
    def test_background(self):
        """Test correct background is present"""

        # first make sure you're on the right page
        assertEqual(driver.title, 'Program Registration')
        print('\n' * 2)  # adds line break
        bg = driver.find_element_by_class_name("container")

        if bg.is_displayed():
            print "background found"
        else:
            print "background not found"

    def save_background(self):
        """print SVG"""

        # this is the SVG text file
        bg_file = open('utils/background.txt', 'w')
        # this requests the data from the URL
        bg_url = requests.get("https://va-mosaic-kcentra-beta.s3.amazonaws.com/images/seb/main-bg.jpg").content
        # this saves the data into the SVG text file
        bg_file.write(bg_url)

    def test_correct_background(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        bg_file = open('utils/background.txt', 'r').read()
        # this requests the data from the URL again
        bg_url = requests.get("https://va-mosaic-kcentra-beta.s3.amazonaws.com/images/seb/main-bg.jpg").content
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
        assertEqual(bg.size["height"], 2653)

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

        assertEqual(header.size["width"], 720)
        assertEqual(header.size["height"], 91)

    def test_header_placement(self):
        """Is the placement correct"""

        header = driver.find_element_by_id("header")
        print('\n')  # adds line break
        print "location of header is at:"
        print (header.location)

        assertEqual(header.location, {"y": 50.0, "x": 89.0})

        # header background color
        header = driver.find_element_by_id("header")
        assertEqual(header.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')

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
        assertEqual(container.size["height"], 2653)

    def test_container_placement(self):
        """Is the placement correct"""

        container = driver.find_element_by_class_name("container")
        print('\n')  # adds line break
        print "location of container is at:"
        print (container.location)

        assertEqual(container.location, {"y": 50.0, "x": 74.0})

        # Container colors and attributes
        container = driver.find_element_by_class_name("container")
        assertEqual(container.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(container.value_of_css_property("background-color"), 'rgba(255, 255, 255, 1)')
        assertEqual(container.value_of_css_property("box-sizing"), 'border-box')

        assertEqual(container.value_of_css_property("line-height"), '20px')
        assertEqual(container.value_of_css_property("margin-bottom"), '0px')
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

        assertEqual(content.size["width"], 720)
        assertEqual(content.size["height"], 2562)

        # Register here...
        register_here = driver.find_element_by_css_selector("h1").text
        if assertEqual(register_here, u"Register here to participate in an upcoming educational program for Kcentra®, Prothrombin Complex Concentrate (Human)."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", register_here, "'", " text is present"

        register_here2 = driver.find_element_by_css_selector("h1")
        assertEqual(register_here2.value_of_css_property("color"), 'rgba(123, 43, 130, 1)')
        assertEqual(register_here2.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(register_here2.value_of_css_property("font-size"), '36px')
        assertEqual(register_here2.value_of_css_property("font-weight"), '500')

class TestProgramDetails(object):

    def test_correct_program(self):
        """See if the program text matches file"""

        # this pulls data from the text file
        program_file = open('utils/program.txt', 'r').read()
        # this requests the data from the URL again
        program_url = driver.find_elements_by_tag_name("div")[12].text
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(program_file, program_url):
            print "text does not match file"
        else:
            print "text matches file"

    def test_program_details(self):
        """This focuses on the program details' attributes"""
        program_info_text = driver.find_elements_by_tag_name("div")[12].text
        print('\n')  # adds line break
        print program_info_text

        print('\n')  # adds line break
        print "Program Information is:"
        print('\n')  # adds line break

        program_info = driver.find_element_by_class_name("labelSection")
        assertEqual(program_info.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(program_info.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(program_info.value_of_css_property("font-size"), '22px')
        assertEqual(program_info.value_of_css_property("font-weight"), 'normal')
        print program_info.text

        date = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[1]/b")
        assertEqual(date.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(date.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(date.value_of_css_property("font-size"), '18px')
        assertEqual(date.value_of_css_property("font-weight"), '900')
        print date.text

        time = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[2]/b")
        assertEqual(time.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(time.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(time.value_of_css_property("font-size"), '18px')
        assertEqual(time.value_of_css_property("font-weight"), '900')

        time2 = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[2]/b/span[1]")
        assertEqual(time2.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(time2.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(time2.value_of_css_property("font-size"), '12px')
        assertEqual(time2.value_of_css_property("font-weight"), '900')

        time3 = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[2]/b/span[2]")
        assertEqual(time3.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(time3.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(time3.value_of_css_property("font-size"), '18px')
        assertEqual(time3.value_of_css_property("font-weight"), '900')
        print time.text

        presenter1 = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[3]")
        assertEqual(presenter1.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(presenter1.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(presenter1.value_of_css_property("font-size"), '18px')
        assertEqual(presenter1.value_of_css_property("font-weight"), '500')

        presenter2 = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[3]/b")
        assertEqual(presenter2.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(presenter2.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(presenter2.value_of_css_property("font-size"), '18px')
        assertEqual(presenter2.value_of_css_property("font-weight"), '900')
        print presenter1.text

        venue = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[4]")
        assertEqual(venue.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(venue.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(venue.value_of_css_property("font-size"), '18px')
        assertEqual(venue.value_of_css_property("font-weight"), '500')
        print venue.text

        host1 = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[5]")
        assertEqual(host1.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(host1.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(host1.value_of_css_property("font-size"), '18px')
        assertEqual(host1.value_of_css_property("font-weight"), '500')

        host2 = driver.find_element_by_xpath("//*[@id='midColumn']/div[2]/div/h4[5]/b")
        assertEqual(host2.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(host2.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(host2.value_of_css_property("font-size"), '18px')
        assertEqual(host2.value_of_css_property("font-weight"), '900')
        print host1.text

class TestProfessionalInformation(object):
    """This tests the professional information section"""

    def test_correct_professional(self):
        """See if the professional information text matches file"""

        # professional information title
        pro_title = driver.find_elements_by_tag_name("div")[16].text
        pro_text = "Professional Information"
        assertEqual(pro_title, pro_text)

        # this pulls data from the text file
        professional_file = open('utils/professional.txt', 'r').read()
        # this requests the data from the URL again
        professional_url = driver.find_elements_by_tag_name("p")[0].text
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(professional_file, professional_url):
            print "text does not match file"
        else:
            print "text matches file"

    def test_professional_information(self):
        """This focuses on the program details' attributes"""

        print('\n')  # adds line break
        print "Professional Information is:"
        print('\n')  # adds line break

        professional_info_text = driver.find_elements_by_tag_name("p")[0].text
        print('\n')  # adds line break
        print professional_info_text

    def test_correct_professional_text1(self):
        """See if the text matches and send keys"""

        professional_info = driver.find_elements_by_tag_name("p")[0]
        assertEqual(professional_info.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(professional_info.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(professional_info.value_of_css_property("font-size"), '18px')
        assertEqual(professional_info.value_of_css_property("font-weight"), 'normal')

        # please complete the following information...
        please_text = driver.find_element_by_xpath("//*[@id='register-form']/div/p[1]")
        assertEqual(please_text.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(please_text.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(please_text.value_of_css_property("font-size"), '18px')
        assertEqual(please_text.value_of_css_property("font-weight"), 'normal')

        # email
        email = driver.find_element_by_xpath("//*[@id='register-form']/div/p[1]/a")
        assertEqual(email.value_of_css_property("color"), 'rgba(176, 186, 54, 1)')
        assertEqual(email.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(email.value_of_css_property("font-size"), '18px')
        assertEqual(email.value_of_css_property("font-weight"), 'normal')

        # phone number...
        phone_text = driver.find_element_by_xpath("//*[@id='register-form']/div/p[1]/br[3]")
        assertEqual(phone_text.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(phone_text.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(phone_text.value_of_css_property("font-size"), '18px')
        assertEqual(phone_text.value_of_css_property("font-weight"), 'normal')

        # star
        assert driver.find_element_by_xpath("//*[@id='register-form']/div/p[2]/star")

        # this is the required field text.
        for element in driver.find_elements_by_xpath("//*[@id='register-form']/div/p[2]"):
            required_text1 = element.get_attribute('innerText')

            if assertEqual(required_text1, " This is a required field."):
                print('\n')  # adds line break
                print "text not found"
            else:
                print('\n')  # adds line break
                print "'","*", required_text1,"'"," text is present"

        # attributes
        required_text1 = driver.find_elements_by_tag_name("p")[1]
        assertEqual(required_text1.value_of_css_property("color"), 'rgba(255, 0, 0, 1)')
        assertEqual(required_text1.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(required_text1.value_of_css_property("font-size"), '18px')
        assertEqual(required_text1.value_of_css_property("font-weight"), 'normal')

    def test_form_titles(self):
        """This will test the drop down form titles"""

        # test correct text for first name, special because of the asterisk
        for element in driver.find_elements_by_xpath("//*[@id='register-form']/div/div[4]"):
            first_text = element.get_attribute('innerText')

            if assertEqual(first_text, "First name : "):
                print('\n')  # adds line break
                print "text not found"
            else:
                print('\n')  # adds line break
                print "'", first_text, "'", " text is present"

        first = driver.find_element_by_css_selector("label")
        assertEqual(first.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(first.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(first.value_of_css_property("font-size"), '14px')
        assertEqual(first.value_of_css_property("font-weight"), 'bold')

        first_term = "First"
        driver.find_element_by_id("id_registrants-0-first_name").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-first_name").send_keys(first_term)
        time.sleep(1)

        # middle name
        middle_text = driver.find_element_by_xpath("//*[@id='register-form']/div/div[5]/label").text
        if assertEqual(middle_text, "Middle name:"):
             print('\n')  # adds line break
             print "text not found"
        else:
             print('\n')  # adds line break
             print "'", middle_text, "'", " text is present"

        middle = driver.find_element_by_xpath("//*[@id='register-form']/div/div[5]/label")
        assertEqual(middle.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(middle.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(middle.value_of_css_property("font-size"), '14px')
        assertEqual(middle.value_of_css_property("font-weight"), 'bold')

        middle_term = "Middle"
        driver.find_element_by_id("id_registrants-0-middle_name").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-middle_name").send_keys(middle_term)
        time.sleep(1)

        # test correct text for last name, special because of the asterisk
        for element in driver.find_elements_by_xpath("//*[@id='lastName']"):
            last_text = element.get_attribute('innerText')

            if assertEqual(last_text, "Last name : "):
                print('\n')  # adds line break
                print "text not found"
            else:
                print('\n')  # adds line break
                print "'", last_text, "'", " text is present"

        last = driver.find_element_by_xpath("//label[@for='id_registrants-0-last_name']")
        assertEqual(last.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(last.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(last.value_of_css_property("font-size"), '14px')
        assertEqual(last.value_of_css_property("font-weight"), 'bold')

        last_term = "Last"
        driver.find_element_by_id("id_registrants-0-last_name").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-last_name").send_keys(last_term)
        time.sleep(1)

        # test correct text for state text, special because of the asterisk
        for element in driver.find_elements_by_xpath("//*[@id='register-form']/div/div[7]"):
            state_text = element.get_attribute('innerText')

            if assertEqual(state_text, "State:\n"):
                print('\n')  # adds line break
                print "text not found"
            else:
                print('\n')  # adds line break
                print "'", state_text, "'", " text is present"

        state = driver.find_element_by_xpath("//*[@id='register-form']/div/div[7]")
        assertEqual(state.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(state.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(state.value_of_css_property("font-size"), '14px')
        assertEqual(state.value_of_css_property("font-weight"), 'normal')

        Select(driver.find_element_by_id("state_dropdown")).select_by_visible_text("AK")

        # BEGIN WITH TESTING ALL THE PROFESSIONAL DROPDOWN OPTIONS AND VERIFYING THOSE REQUIRED FIELDS.
        # THEN LASTLY, SELECT THE 'I AM A PROFESSIONAL LICENSED TO PRESCRIBE' OPTION
        # BECAUSE IT FULFILLS ALL OF THE DROPDOWN REQUIREMENTS. #####

class TestHealthcareNoPrescribe(object):
    """This tests the professional information section if 'I am a healthcare professional, NOT licensed to prescribe' is chosen"""

    def test_stars_section1(self):
        """All that needs checked is the 'required fields'since it's almost the same as the previous option"""

        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am a healthcare professional, NOT Licensed to prescribe")
        time.sleep(3)

        # required field stars
        stars1 = driver.find_elements_by_class_name("star")[0 - 10]
        print('\n')  # adds line break

        if stars1.is_displayed():
            print "Relevant fields all marked as required"
        else:
            print "Relevant fields NOT marked as required"

        stars2 = driver.find_elements_by_class_name("star")[7]
        print('\n')  # adds line break

        if stars2.is_displayed():
            print "Relevant fields all marked as required"
        else:
            print "Relevant fields NOT marked as required"

        stars3 = driver.find_elements_by_class_name("star")[9 - 16]
        print('\n')  # adds line break

        if stars3.is_displayed():
            print "Relevant fields all marked as required"
        else:
            print "Relevant fields NOT marked as required"

    def test_required_forms2(self):
        """Part two of checking the blue required form fields"""
        assert driver.find_elements_by_class_name("not-filled-in")[0 - 11]
        not_filled2 = driver.find_elements_by_class_name("not-filled-in")[0 - 11]
        assertEqual(not_filled2.value_of_css_property("background-color"), 'rgba(173, 216, 230, 1)')

class TestNotHealthcareProfessional(object):
    """This tests the professional information section if 'I am not a healthcare professional' is chosen"""

    def test_stars_section2(self):
        """All that needs checked is the 'required fields'since it's almost the same as the first option"""

        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am not a healthcare professional")
        time.sleep(1)

        # required field stars
        stars1 = driver.find_elements_by_class_name("star")[0 - 5]
        print('\n')  # adds line break

        if stars1.is_displayed():
            print "Relevant fields all marked as required"
        else:
            print "Relevant fields NOT marked as required"

        stars2 = driver.find_elements_by_class_name("star")[10 - 16]
        print('\n')  # adds line break

        if stars2.is_displayed():
            print "Relevant fields all marked as required"
        else:
            print "Relevant fields NOT marked as required"

    def test_required_forms3(self):
        """Part three of checking the blue required form fields"""
        assert driver.find_elements_by_class_name("not-filled-in")[0 - 8]
        not_filled3 = driver.find_elements_by_class_name("not-filled-in")[0 - 8]
        assertEqual(not_filled3.value_of_css_property("background-color"), 'rgba(173, 216, 230, 1)')

class TestCLSBehringSpecialty(object):
    """This tests the professional information section if 'I am not a healthcare professional' is chosen"""

    def test_stars_section2(self):
        """All that needs checked is the 'required fields'since it's almost the same as the first option"""

        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am a CSL Behring Specialty sales force member")
        time.sleep(1)

        # required field stars
        stars1 = driver.find_elements_by_class_name("star")[0 - 4]
        print('\n')  # adds line break

        if stars1.is_displayed():
            print "Relevant fields all marked as required"
        else:
            print "Relevant fields NOT marked as required"

        stars2 = driver.find_elements_by_class_name("star")[10 - 16]
        print('\n')  # adds line break

        if stars2.is_displayed():
            print "Relevant fields all marked as required"
        else:
            print "Relevant fields NOT marked as required"

    def test_required_forms4(self):
        """Part four of checking the blue required form fields"""
        assert driver.find_elements_by_class_name("not-filled-in")[0 - 7]
        not_filled4 = driver.find_elements_by_class_name("not-filled-in")[0 - 7]
        assertEqual(not_filled4.value_of_css_property("background-color"), 'rgba(173, 216, 230, 1)')

class TestHealthcarePrescribe(object):
    """This tests the professional information section if 'I am a healthcare professional, licensed to prescribe' is chosen... This satisfies all dropdown requirements"""

    def test_correct_professional_text1(self):
        """This tests the form scenario when 'I am a healthcare profession, licensed to prescribe' option is chosen"""

        # choose 'I am a healthcare professional, licensed to prescribe'
        healthcare_text = driver.find_element_by_xpath("//label[@for='id_registrants-0-ecp']").text
        if assertEqual(healthcare_text, "Are you a healthcare professional?"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", healthcare_text, "'", " text is present"

        healthcare = driver.find_element_by_xpath("//label[@for='id_registrants-0-ecp']")
        assertEqual(healthcare.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(healthcare.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(healthcare.value_of_css_property("font-size"), '14px')
        assertEqual(healthcare.value_of_css_property("font-weight"), 'bold')

        #Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am a healthcare professional, licensed to prescribe")
        time.sleep(1)

        ###  Having issues with pop up... for now skip the pop up tests by running this area instead:
        Select(driver.find_element_by_id("id_registrants-0-ecp")).select_by_visible_text("I am a healthcare professional, NOT Licensed to prescribe")
        time.sleep(1)

    def record_pop_up(self):
        """This tests the form scenario when 'I am a healthcare profession, licensed to prescribe' option is chosen"""

        choices_text = driver.find_element_by_css_selector("h3").text

        if assertEqual(choices_text, "Please select from the choices below."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", choices_text, "'", " text is present"

        # Please select from the choices below.
        choices = driver.find_element_by_css_selector("h3")
        assertEqual(choices.value_of_css_property("color"), 'rgba(123, 43, 130, 1)')
        assertEqual(choices.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(choices.value_of_css_property("font-size"), '24px')
        assertEqual(choices.value_of_css_property("font-weight"), '500')

        # Name
        name = driver.find_element_by_css_selector("th").text
        if assertEqual(name, "Name"):
            print('\n')
            print "'Name' not found"
        else:
            print('\n')
            print "'", name, "'", " text is present"

        name_text = driver.find_element_by_css_selector("th")
        assertEqual(name_text.value_of_css_property("color"), 'rgba(4, 75, 123, 1)')
        assertEqual(name_text.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(name_text.value_of_css_property("font-size"), '24px')
        assertEqual(name_text.value_of_css_property("font-weight"), '500')

        # Address
        address = driver.find_element_by_xpath("//table[@id='npi_picker_table']/tbody/tr/th[2]").text
        if assertEqual(address, "Address"):
            print('\n')
            print "'Address' not found"
        else:
            print('\n')
            print "'", address, "'", " text is present"

        address_text = driver.find_element_by_xpath("//table[@id='npi_picker_table']/tbody/tr/th[2]")
        assertEqual(address_text.value_of_css_property("color"), 'rgba(4, 75, 123, 1)')
        assertEqual(address_text.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(address_text.value_of_css_property("font-size"), '24px')
        assertEqual(address_text.value_of_css_property("font-weight"), '500')

        # NPI Number
        npi = driver.find_element_by_xpath("//table[@id='npi_picker_table']/tbody/tr/th[3]").text
        if assertEqual(npi, "NPI Number"):
            print('\n')
            print "'NPI Number' text not found"
        else:
            print('\n')
            print "'", npi, "'", " text is present"

        npi_text = driver.find_element_by_xpath("//table[@id='npi_picker_table']/tbody/tr/th[3]")
        assertEqual(npi_text.value_of_css_property("color"), 'rgba(4, 75, 123, 1)')
        assertEqual(npi_text.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(npi_text.value_of_css_property("font-size"), '24px')
        assertEqual(npi_text.value_of_css_property("font-weight"), '500')

        # Note seeing your record?
        not_seeing_text = driver.find_element_by_id("btn_click_to_continue").text
        if assertEqual(not_seeing_text, "Not seeing your record?  Click here to continue."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", not_seeing_text, "'", " text is present"

        not_seeing = driver.find_element_by_id("btn_click_to_continue")
        assertEqual(not_seeing.value_of_css_property("color"), 'rgba(117, 118, 121, 1)')
        assertEqual(not_seeing.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(not_seeing.value_of_css_property("font-size"), '14px')
        assertEqual(not_seeing.value_of_css_property("font-weight"), 'normal')
        assertEqual(not_seeing.value_of_css_property("background-color"), 'rgba(204, 204, 204, 1)')

        # make sure 'X' is there
        x_button = driver.find_element_by_class_name("close").text
        if assertEqual(x_button, u"x"):
            print('\n')
            print "'X' not found"
        else:
            print('\n')
            print "'", x_button, "'", " text is present"

        # click the close button
        x_button.click()
        time.sleep(5)

    def test_required_forms5(self):
        """Part five of checking the blue required form fields"""
        assert driver.find_elements_by_class_name("not-filled-in")[0 - 9]
        not_filled5 = driver.find_elements_by_class_name("not-filled-in")[0 - 9]
        assertEqual(not_filled5.value_of_css_property("background-color"), 'rgba(173, 216, 230, 1)')

    def test_title_sections(self):
        """See if the title section is correct"""

        title_text = driver.find_element_by_xpath("//label[@for='id_registrants-0-salutation']").text
        if assertEqual(title_text, "Title:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", title_text, "'", " text is present"

        title = driver.find_element_by_xpath("//label[@for='id_registrants-0-salutation']")
        assertEqual(title.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(title.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(title.value_of_css_property("font-size"), '14px')
        assertEqual(title.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-salutation")).select_by_visible_text("Sir")
        print('\n')  # adds line break

        # professional designation
        designation_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[2]/label").text
        if assertEqual(designation_text, "Professional designation:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", designation_text, "'", " text is present"

        designation = driver.find_element_by_xpath("//*[@id='main_content_container']/div[3]/label[1]")
        assertEqual(designation.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(designation.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(designation.value_of_css_property("font-size"), '14px')
        assertEqual(designation.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-primary_degree")).select_by_visible_text("RPh")

        # affiliation/practice
        affiliation_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[3]/label[1]").text
        if assertEqual(affiliation_text, "Affiliation/Practice:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", affiliation_text, "'", " text is present"

        affiliation = driver.find_element_by_xpath("//*[@id='main_content_container']/div[3]/label[1]")
        assertEqual(affiliation.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(affiliation.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(affiliation.value_of_css_property("font-size"), '14px')
        assertEqual(affiliation.value_of_css_property("font-weight"), 'bold')

        affiliation_term = "Affiliation/Practice"
        driver.find_element_by_id("id_registrants-0-affiliation").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-affiliation").send_keys(affiliation_term)
        time.sleep(1)

        # specialty
        specialty_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[5]/label[1]").text
        if assertEqual(specialty_text, "Specialty"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", specialty_text, "'", " text is present"

        specialty = driver.find_element_by_xpath("//*[@id='main_content_container']/div[5]/label[1]")
        assertEqual(specialty.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(specialty.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(specialty.value_of_css_property("font-size"), '14px')
        assertEqual(specialty.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_registrants-0-specialty")).select_by_visible_text("Trauma & Acute Care Surgery")

        # NPI number
        npi_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[7]/label[1]").text
        if assertEqual(npi_text, "NPI number:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", npi_text, "'", " text is present"

        npi = driver.find_element_by_xpath("//*[@id='main_content_container']/div[7]/label[1]")
        assertEqual(npi.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(npi.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(npi.value_of_css_property("font-size"), '14px')
        assertEqual(npi.value_of_css_property("font-weight"), 'bold')

        NPI_term = "0123456789"
        driver.find_element_by_id("id_registrants-0-certification_npi_number").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-certification_npi_number").send_keys(NPI_term)
        time.sleep(1)

    def npi_checkbox(self):
        """this will check the npi checkbox functionality"""
        ###  Will check this later when pop up solution is found from above.
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

    def test_title_sections_cont(self):
        """See if the title section is correct (continued)"""

        # click here link - exit out of tab
        click_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[9]/span/a").text
        if assertEqual(click_text, "Click here to search for your NPI number"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", click_text, "'", " text is present"

        click = driver.find_element_by_xpath("//*[@id='main_content_container']/div[9]/span/a")
        assertEqual(click.value_of_css_property("color"), 'rgba(176, 186, 54, 1)')
        assertEqual(click.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
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

        # state license number 1
        license_text = driver.find_element_by_xpath("//*[@id='state-license-form']/div[2]/label[1]").text
        if assertEqual(license_text, "State license number:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", license_text, "'", " text is present"

        license = driver.find_element_by_xpath("//*[@id='state-license-form']/div[2]/label[1]")
        assertEqual(license.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(license.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(license.value_of_css_property("font-size"), '14px')
        assertEqual(license.value_of_css_property("font-weight"), 'bold')

        license_term = "0123456789"
        driver.find_element_by_id("id_registrants-0-state_licenses-0-license_number").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-state_licenses-0-license_number").send_keys(license_term)
        time.sleep(1)

        # add additional license number
        additional_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/a").text
        if assertEqual(additional_text, "Add additional license"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", additional_text, "'", " text is present"

        additional = driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/a")
        assertEqual(additional.value_of_css_property("color"), 'rgba(176, 186, 54, 1)')
        assertEqual(additional.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(additional.value_of_css_property("font-size"), '14px')
        assertEqual(additional.value_of_css_property("font-weight"), 'normal')

        # click additional
        driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/a").click()

        # delete row
        driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/div/div[1]/a").click()

        # click additional again
        driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/a").click()

        # line break
        hr = driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/div/hr")
        size = hr.size
        print('\n')  # adds line break
        print "size of the line break is:"
        print (size)

        assertEqual(hr.size["width"], 600)
        assertEqual(hr.size["height"], 1)

        print('\n')  # adds line break
        print "location of line break is at:"
        print (hr.location)

        assertEqual(hr.location, {"y": 1801.0, "x": 149.0})

        assertEqual(hr.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-bottom-color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-left-color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-right-color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-top-color"), 'rgba(238, 238, 238, 1)')
        assertEqual(hr.value_of_css_property("border-top-style"), 'solid')
        assertEqual(hr.value_of_css_property("display"), 'block')

        # state license number 2
        license_text2 = driver.find_element_by_xpath("//*[@id='state-license-form']/div[2]/label[1]").text
        if assertEqual(license_text2, "State license number:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", license_text2, "'", " text is present"

        license2 = driver.find_element_by_xpath("//*[@id='state-license-form']/div[2]/label[1]")
        assertEqual(license2.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(license2.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(license2.value_of_css_property("font-size"), '14px')
        assertEqual(license2.value_of_css_property("font-weight"), 'bold')

        license_term2 = "0123456789"
        driver.find_element_by_id("id_registrants-0-state_licenses-1-license_number").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-state_licenses-1-license_number").send_keys(license_term2)
        time.sleep(1)

        # click to search license - exit out of tab
        search_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/span/a").text
        if assertEqual(search_text, "Click here to search for your state license number"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", search_text, "'", " text is present"

        search = driver.find_element_by_xpath("//*[@id='main_content_container']/div[11]/span/a")
        assertEqual(search.value_of_css_property("color"), 'rgba(176, 186, 54, 1)')
        assertEqual(search.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
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

        # address 1
        address_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[12]/label").text
        if assertEqual(address_text, "Address 1"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", address_text, "'", " text is present"

        address = driver.find_element_by_xpath("//*[@id='main_content_container']/div[12]/label")
        assertEqual(address.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(address.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(address.value_of_css_property("font-size"), '14px')
        assertEqual(address.value_of_css_property("font-weight"), 'bold')

        address1_term = "123 Test Place"
        driver.find_element_by_id("id_address1").click()
        time.sleep(1)
        driver.find_element_by_id("id_address1").send_keys(address1_term)
        time.sleep(1)

        # address 2
        address2_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[13]/label").text
        if assertEqual(address2_text, "Address 2:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", address2_text, "'", " text is present"

        address2 = driver.find_element_by_xpath("//*[@id='main_content_container']/div[13]/label")
        assertEqual(address2.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(address2.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(address2.value_of_css_property("font-size"), '14px')
        assertEqual(address2.value_of_css_property("font-weight"), 'bold')

        address2_term = "Suite Test"
        driver.find_element_by_id("id_address2").click()
        time.sleep(1)
        driver.find_element_by_id("id_address2").send_keys(address2_term)
        time.sleep(1)

        # city
        city_text = driver.find_element_by_xpath("//*[@id='city']/label").text
        if assertEqual(city_text, "City"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", city_text, "'", " text is present"

        city = driver.find_element_by_xpath("//*[@id='city']/label")
        assertEqual(city.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(city.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(city.value_of_css_property("font-size"), '14px')
        assertEqual(city.value_of_css_property("font-weight"), 'bold')

        city_term = "City Test"
        driver.find_element_by_id("id_city").click()
        time.sleep(1)
        driver.find_element_by_id("id_city").send_keys(city_term)
        time.sleep(1)

        # state
        state_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[15]/label").text
        if assertEqual(state_text, "State"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", state_text, "'", " text is present"

        state = driver.find_element_by_xpath("//*[@id='main_content_container']/div[15]/label")
        assertEqual(state.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(state.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(state.value_of_css_property("font-size"), '14px')
        assertEqual(state.value_of_css_property("font-weight"), 'bold')

        Select(driver.find_element_by_id("id_state")).select_by_visible_text("NY")

        # zip
        zip_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[16]/label").text
        if assertEqual(zip_text, "Zip"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", zip_text, "'", " text is present"

        zip = driver.find_element_by_xpath("//*[@id='main_content_container']/div[16]/label")
        assertEqual(zip.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(zip.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(zip.value_of_css_property("font-size"), '14px')
        assertEqual(zip.value_of_css_property("font-weight"), 'bold')

        zip_term = "10001"
        driver.find_element_by_id("id_zipcode").click()
        time.sleep(1)
        driver.find_element_by_id("id_zipcode").send_keys(zip_term)
        time.sleep(1)

        # phone number
        phone_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[17]/label").text
        if assertEqual(phone_text, "Phone number"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", phone_text, "'", " text is present"

        phone = driver.find_element_by_xpath("//*[@id='main_content_container']/div[17]/label")
        assertEqual(phone.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(phone.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(phone.value_of_css_property("font-size"), '14px')
        assertEqual(phone.value_of_css_property("font-weight"), 'bold')

        phone_term = "2125555555"
        driver.find_element_by_id("id_registrants-0-mobile_phone").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-mobile_phone").send_keys(phone_term)
        time.sleep(1)

        # email address
        email_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[18]/label").text
        if assertEqual(email_text, "Email address"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", email_text, "'", " text is present"

        email = driver.find_element_by_xpath("//*[@id='main_content_container']/div[18]/label")
        assertEqual(email.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(email.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(email.value_of_css_property("font-size"), '14px')
        assertEqual(email.value_of_css_property("font-weight"), 'bold')

        email_term = "test@example.com"
        driver.find_element_by_id("id_registrants-0-email").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-email").send_keys(email_term)
        time.sleep(1)

        # Before continuing, try to submit and test the "Please fill out all fields marked with an *." text.

        # button
        button = driver.find_element_by_class_name("btn-wrapper")
        # hover over the button
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()

    def test_correct_error(self):
        """See if the asterisks text matches"""

        # this pulls data from the text file
        asterisks_file = open('utils/register.txt', 'r').read()
        # this requests the data from the URL again
        #asterisks = driver.find_elements_by_class_name("tooltip-inner")
        for element in driver.find_elements_by_class_name("tooltip-inner"):
            print('\n')  # adds line break
            asterisks = element.get_attribute('innerText')
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
            print('\n')  # adds line break
            if assertEqual(asterisks_file, asterisks):
                print "Asterisks text does not match file"
            else:
                print "Asterisks text matches file"

        # confirm email
        for element in driver.find_elements_by_xpath("//div[@id='main_content_container']/div[19]/label"):
            print('\n')  # adds line break
            confirm_text = element.get_attribute('innerText')

            if assertEqual(confirm_text, "Confirm email"):
                print('\n')  # adds line break
                print "text not found"
            else:
                print('\n')  # adds line break
                print "'", confirm_text, "'", " text is present"

            confirm = driver.find_elements_by_tag_name("label")[21]
            assertEqual(confirm.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
            assertEqual(confirm.value_of_css_property("font-family"),
                        'Montserrat-light, sans-serif')
            assertEqual(confirm.value_of_css_property("font-size"), '14px')
            assertEqual(confirm.value_of_css_property("font-weight"), 'bold')

        confirm_term = "test@example.com"
        driver.find_element_by_id("id_registrants-0-confirm_email").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-confirm_email").send_keys(confirm_term)
        time.sleep(1)

        # dietary restrictions
        dietary_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[20]/label").text
        if assertEqual(dietary_text, "Dietary restrictions:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", dietary_text, "'", " text is present"

        dietary = driver.find_element_by_xpath("//*[@id='main_content_container']/div[20]/label")
        assertEqual(dietary.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(dietary.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(dietary.value_of_css_property("font-size"), '14px')
        assertEqual(dietary.value_of_css_property("font-weight"), 'bold')

        dietary_term = "test test test"
        driver.find_element_by_id("id_registrants-0-dietary_restrictions").click()
        time.sleep(1)
        driver.find_element_by_id("id_registrants-0-dietary_restrictions").send_keys(dietary_term)
        time.sleep(1)

        # opt out of meal / checkbox
        opt_text = driver.find_element_by_xpath("//*[@id='main_content_container']/div[21]/div/label").text
        if assertEqual(opt_text, "Opt out of meal:"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", opt_text, "'", " text is present"

        opt = driver.find_element_by_xpath("//*[@id='main_content_container']/div[21]/div/label")
        assertEqual(opt.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(opt.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(opt.value_of_css_property("font-size"), '14px')
        assertEqual(opt.value_of_css_property("font-weight"), 'bold')

        # check checkbox2
        checkbox2 = driver.find_element_by_name("registrants-0-opt_out_of_meal")
        checkbox2.click()
        time.sleep(1)
        checkbox2.click()
        time.sleep(1)

        # required field stars
        stars = driver.find_elements_by_class_name("star")[0 - 14]
        print('\n')  # adds line break

        if stars.is_displayed():
            print "Relevant fields NOT all marked as required"
        else:
            print "Relevant fields marked as required"

class TestDropdownContents(object):

    def test_state_dropdown(self):
        """verifies the contents of the 1st state drop down"""

        state_dropdown = driver.find_elements_by_xpath("//*[@id='state_dropdown']/option")
        state_list = [state_dropdown[i].text for i in xrange(53)]
        assertEqual(state_list,
                    [u'---------', u'AL', u'AK', u'AR', u'AZ', u'CA', u'CO', u'CT', u'DC', u'DE', u'FL', u'GA', u'HI', u'IA', u'ID', u'IL', u'IN', u'KS', u'KY', u'LA', u'MA', u'MD', u'ME', u'MI', u'MN', u'MO', u'MS', u'MT', u'NC', u'ND', u'NE', u'NH', u'NJ', u'NM', u'NV', u'NY', u'OH', u'OK', u'OR', u'PA', u'PR', u'RI', u'SC', u'SD', u'TN', u'TX', u'UT', u'VA', u'VT', u'WA', u'WI', u'WV', u'WY']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='state_dropdown']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    def test_state_dropdown2(self):
        """verifies the contents of the 2nd state dropdown"""

        state_dropdown2 = driver.find_elements_by_xpath("//*[@id='id_state']/option")
        state_list2 = [state_dropdown2[i].text for i in xrange(53)]
        print state_list2,

        assertEqual(state_list2,
                    [u'------', u'AK', u'AL', u'AR', u'AZ', u'CA', u'CO', u'CT', u'DC', u'DE', u'FL', u'GA', u'HI',
                     u'IA', u'ID', u'IL', u'IN', u'KS', u'KY', u'LA', u'MA', u'MD', u'ME', u'MI', u'MN', u'MO', u'MS',
                     u'MT', u'NC', u'ND', u'NE', u'NH', u'NJ', u'NM', u'NV', u'NY', u'OH', u'OK', u'OR', u'PA', u'PR',
                     u'RI', u'SC', u'SD', u'TN', u'TX', u'UT', u'VA', u'VT', u'WA', u'WI', u'WV', u'WY']
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
                    [u'---------', u'I am a healthcare professional, licensed to prescribe',
                     u'I am a healthcare professional, NOT Licensed to prescribe',
                     u'I am not a healthcare professional', u'I am a CSL Behring Specialty sales force member']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-ecp']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerText')

    def test_title_dropdown2(self):
        """verifies the contents of the title dropdown"""

        title_dropdown = driver.find_elements_by_xpath("//*[@id='id_registrants-0-salutation']/option")
        title_list = [title_dropdown[i].text for i in xrange(9)]
        print title_list,

        assertEqual(title_list,
                    [u'---------', u'Dr.', u'Madam ', u'Miss', u'Mr.', u'Mrs.', u'Ms. ', u'Professor ', u'Sir']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-salutation']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerText')

    def test_pd_dropdown2(self):
        """verifies the contents of the professional designation dropdown"""
        pd_dropdown = driver.find_elements_by_xpath("//*[@id='id_registrants-0-primary_degree']/option")
        pd_list = [pd_dropdown[i].text for i in xrange(29)]
        print pd_list,

        assertEqual(pd_list,
                    [u'---------', u'APNP', u'APRN', u'ARNP', u'BS', u'CRNP', u'DNP', u'DO', u'DO, MSc, FACP, FHM',
                     u'EdD', u'JD', u'LCSW', u'LPN', u'MBBCh', u'MBBS', u'MD', u'MSN', u'MSW', u'N/A', u'NP', u'OD',
                     u'PA', u'PharmD', u'PharmD, BCCCP, BCPS', u'PhD', u'PMHCNS-BC', u'PMHNP-BC', u'PsyD', u'RN']
                    )

        for element in driver.find_elements_by_xpath("//*[@id='id_registrants-0-primary_degree']/option"):
            print('\n')  # adds line break
            print element.get_attribute('innerText')

    def specialty_dropdown(self):
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


class TestPolicy(object):
    """This tests the policy section"""

    def test_policy_as_a_whole_text(self):
        """This tests the same attributes of the 'p' section"""
        all_policy = driver.find_element_by_css_selector("p")
        assertEqual(all_policy.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(all_policy.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(all_policy.value_of_css_property("font-size"), '18px')
        assertEqual(all_policy.value_of_css_property("font-weight"), 'normal')


    def test_policy_titles(self):
        """This tests the attributes of the policy titles"""

        # title tag name 'b' text and weight
        #attendee_text = driver.find_element_by_css_selector("h4.title.left").text
        attendee_text = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/b[1]").text

        if assertEqual(attendee_text, "ATTENDEE POLICY"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text, "'", " text is present"

        # reporting_text = driver.find_element_by_css_selector("h4.title.left").text
        reporting_text = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/b[2]").text

        if assertEqual(reporting_text, "REPORTING POLICY"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", reporting_text, "'", " text is present"

        important_text = driver.find_element_by_css_selector("u").text

        if assertEqual(important_text, "Important Safety Information"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", important_text, "'", " text is present"

        # important underline
        #assertEqual(important_text.value_of_css_property("text-decoration"), 'underline')

        # warning_text = driver.find_element_by_css_selector("h4.title.left").text
        warning_text = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/div/b").text

        if assertEqual(warning_text, "WARNING: ARTERIAL AND VENOUS THROMBOEMBOLIC COMPLICATIONS"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text, "'", " text is present"

        # title tag name 'b' attributes
        attending = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/div/b")
        assertEqual(attending.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(attending.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(attending.value_of_css_property("font-size"), '14px')
        assertEqual(attending.value_of_css_property("font-weight"), '900')


    def test_attendee_policy(self):
        """This will save the policy text"""

        attendee_text1 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[1]").text

        attendee1 = "CSL Behring complies with PhRMA Guidelines; therefore, spouses, partners, or guests may not attend any meeting or social function. Spouses and guests will not be permitted to attend any activities related to this meeting, including meal functions, as these are considered part of the official program. If your spouse or a guest is traveling with you, any charges or expenses related to his or her presence will be your personal responsibility."

        if assertEqual(attendee_text1, unicode(attendee1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text1, "'", " text is present"

        attendee_text2 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[2]").text
        attendee2 = "This program is intended for US healthcare providers only."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(attendee_text2, unicode(attendee2, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text2, "'", " text is present"

    def test_reporting_policy(self):
        """This will save the policy text"""

        reporting_text1 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[3]").text
        reporting1 = "Personal information provided above will not be used for any other purpose beyond this peer-to-peer program and required federal and state-level reporting."

        if assertEqual(reporting_text1, unicode(reporting1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", reporting_text1, "'", " text is present"

        reporting_text2 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[4]").text
        reporting2 = "Consistent with federal and state reporting obligations including, but not limited to, the Federal Physician Payment Sunshine Act, CSL Behring will disclose any transfers of value given to healthcare providers attending our programs."

        if assertEqual(reporting_text2, unicode(reporting2, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", reporting_text2, "'", " text is present"

    def test_safety_policy(self):
        """This will save the policy text"""

        # registered 'R'
        assert driver.find_element_by_css_selector("sup")
        safety_text = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[5]").text
        safety = "Kcentra® Prothrombin Complex Concentrate (Human), is a blood coagulation factor replacement product indicated for the urgent reversal of acquired coagulation factor deficiency induced by Vitamin K antagonist (VKA—eg, warfarin) therapy in adult patients with acute major bleeding or the need for urgent surgery or other invasive procedure. Kcentra is for intravenous use only."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(safety_text, unicode(safety, "utf-8")):
        #if assertEqual(safety_text, safety):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", safety_text, "'", " text is present"

    def test_warning_policy(self):
        """This will save the policy text"""

        warning_text1 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/div/p/b").text
        warning1 = "Patients being treated with Vitamin K antagonist therapy have underlying disease states that predispose them to thromboembolic events. Potential benefits of reversing VKA should be weighed against the risk of thromboembolic events, especially in patients with history of such events. Resumption of anticoagulation therapy should be carefully considered once the risk of thromboembolic events outweighs the risk of acute bleeding. Both fatal and nonfatal arterial and venous thromboembolic complications have been reported in clinical trials and postmarketing surveillance. Monitor patients receiving Kcentra, and inform them of signs and symptoms of thromboembolic events. Kcentra was not studied in subjects who had a thromboembolic event, myocardial infarction, disseminated intravascular coagulation, cerebral vascular accident, transient ischemic attack, unstable angina pectoris, or severe peripheral vascular disease within the prior 3 months. Kcentra might not be suitable for patients with thromboembolic events in the prior 3 months."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text1, unicode(warning1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text1, "'", " text is present"

        warning_text2 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[6]").text
        warning2 = "Kcentra is contraindicated in patients with known anaphylactic or severe systemic reactions to Kcentra or any of its components (including heparin, Factors II, VII, IX, X, Proteins C and S, Antithrombin III and human albumin). Kcentra is also contraindicated in patients with disseminated intravascular coagulation. Because Kcentra contains heparin, it is contraindicated in patients with heparin-induced thrombocytopenia (HIT)."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text2, unicode(warning2, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text2, "'", " text is present"

        warning_text3 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[7]").text
        warning3 = "Hypersensitivity reactions to Kcentra may occur. If patient experiences severe allergic or anaphylactic type reactions, discontinue administration and institute appropriate treatment."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text3, unicode(warning3, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text3, "'", " text is present"

        warning_text4 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[8]").text
        warning4 = u"In clinical trials, the most frequent (≥2.8%) adverse reactions observed in subjects receiving Kcentra were headache, nausea/vomiting, hypotension, and anemia. The most serious adverse reactions were thromboembolic events, including stroke, pulmonary embolism and deep vein thrombosis."

        # Add unicode(----, "utf-8")): to get the characters accepted
        #if assertEqual(warning_text4, unicode(warning4, "utf-8")):
        if assertEqual(warning_text4, warning4):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text4, "'", " text is present"

        warning_text5 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[9]").text
        warning5 = "Kcentra is derived from human plasma. The risk of transmission of infectious agents, including viruses and, theoretically, the Creutzfeldt-Jakob disease (CJD) agent, cannot be completely eliminated."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text5, unicode(warning5, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text5, "'", " text is present"

        warning_text6 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[10]").text
        warning6 = "The safety and efficacy of Kcentra in pediatric use have not been studied, and Kcentra should be used in women who are pregnant or nursing only if clearly needed."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text6, unicode(warning6, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text6, "'", " text is present"

        warning_text7 = driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[11]").text
        warning7 = "Please see full prescribing information for Kcentra."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text7, unicode(warning7, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text7, "'", " text is present"

        # all the sub-text in the policy section
        all_policy_text = driver.find_element_by_css_selector("p")
        assertEqual(all_policy_text.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(all_policy_text.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(all_policy_text.value_of_css_property("font-size"), '18px')
        assertEqual(all_policy_text.value_of_css_property("font-weight"), 'normal')

        # link at the bottom
        link = driver.find_element_by_link_text("full prescribing information")
        assertEqual(link.value_of_css_property("color"), 'rgba(176, 186, 54, 1)')
        assertEqual(link.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(link.value_of_css_property("font-size"), '14px')
        assertEqual(link.value_of_css_property("font-weight"), 'normal')

    def test_click_link(self):
        """This will verify the link, click it, and close the new tab"""

        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='registration-form']/div[2]/div[2]/p[11]/a").click()
        #driver.find_element_by_link_text("full prescribing information").click()
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

        assertEqual(footer.size["width"], 720)
        assertEqual(footer.size["height"], 213)

    def test_footer_placement(self):
        """Is the placement correct"""

        footer = driver.find_element_by_id("footer")
        print('\n')  # adds line break
        print "location of header is at:"
        print (footer.location)

        assertEqual(footer.location, {"y": 3953.0, "x": 89.0})

        # footer background color
        footer = driver.find_element_by_id("footer")
        assertEqual(footer.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')

        assertEqual(footer.size["width"], 720)
        assertEqual(footer.size["height"], 213)

        print('\n')  # adds line break
        print "location of header is at:"
        print (footer.location)

class TestContainerObjects(object):

    # TOP Logo
    def test_logo(self):
        """Test correct logo present"""

        print('\n' * 2)  # adds line break
        logo = driver.find_elements_by_class_name("login-logo")[0]

        if logo.is_displayed():
            print "logo found"
        else:
            print "logo not found"

    def save_logo(self):
        """print SVG"""

        # this is the SVG text file
        logo_file = open('utils/logo.txt', 'w')
        # this requests the data from the URL
        svg_url = requests.get("https://va-mosaic-kcentra-beta.s3.amazonaws.com/images/kcentra-rebrand/Kcentra_logo.png").content
        # this saves the data into the SVG text file
        logo_file.write(svg_url)

    def test_correct_logo(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        logo_file = open('utils/logo.txt', 'r').read()
        # this requests the data from the URL again
        svg_url = requests.get("https://va-mosaic-kcentra-beta.s3.amazonaws.com/images/kcentra-rebrand/Kcentra_logo.png").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(logo_file, svg_url):
            print "image does not match file"
        else:
            print "image matches file"

    def test_correct_logo_size(self):
        """Is the size correct?"""

        #logo = driver.find_elements_by_class_name("login-logo")
        logo = driver.find_elements_by_class_name("login-logo")[0]
        size = logo.size
        print('\n')  # adds line break
        print "size of the logo is:"
        print (size)

        assertEqual(logo.size["width"], 289)
        assertEqual(logo.size["height"], 69)

    def test_logo_placement(self):
        """Is the placement correct"""

        logo = driver.find_elements_by_class_name("login-logo")[0]
        print('\n')  # adds line break
        print "location of logo is at:"
        print (logo.location)

        assertEqual(logo.location, {"y": 50.0, "x": 89.0})

    # Header Border
    def test_header_border(self):
        """Test correct header present"""

        print('\n' * 2)  # adds line break
        header = driver.find_element_by_class_name("header-border")

        if header.is_displayed():
            print "header border found"
        else:
            print "header border not found"

    def save_header(self):
        """print SVG"""

        # this is the SVG text file
        header_file = open('utils/header_border.txt', 'w')
        # this requests the data from the URL
        header_url = requests.get(
            "https://va-mosaic-kcentra-beta.s3.amazonaws.com/images/kcentra-rebrand/kcentra_horizontal_bar.png").content
        # this saves the data into the SVG text file
        header_file.write(header_url)

    def test_correct_header(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        header_file = open('utils/header_border.txt', 'r').read()
        # this requests the data from the URL again
        header_url = requests.get(
            "https://va-mosaic-kcentra-beta.s3.amazonaws.com/images/kcentra-rebrand/kcentra_horizontal_bar.png").content
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

        assertEqual(header.size["width"], 720)
        assertEqual(header.size["height"], 12)

    def test_header_placement(self):
        """Is the placement correct"""

        header = driver.find_element_by_class_name("header-border")
        print('\n')  # adds line break
        print "location of header border is at:"
        print (header.location)

        assertEqual(header.location, {"y": 129.0, "x": 89.0})

    # BOTTOM Logo
    def test_bottom_logo(self):
        """Test correct logo present"""

        print('\n' * 2)  # adds line break
        logo = driver.find_elements_by_tag_name("center")[1]

        if logo.is_displayed():
            print "logo found"
        else:
            print "logo not found"

    def save_bottom_logo(self):
        """print SVG"""

        # this is the SVG text file
        logo_file = open('utils/logo2.txt', 'w')
        # this requests the data from the URL
        svg_url = requests.get("https://va-mosaic-kcentra-beta.s3.amazonaws.com/img/global/kcentra-rebrand/footer-CSLBehring-logo4.png").content
        # this saves the data into the SVG text file
        logo_file.write(svg_url)

    def test_correct_bottom_logo(self):
        """See if the SVG matches"""

        # this pulls data from the text file
        logo_file = open('utils/logo2.txt', 'r').read()
        # this requests the data from the URL again
        svg_url = requests.get("https://va-mosaic-kcentra-beta.s3.amazonaws.com/img/global/kcentra-rebrand/footer-CSLBehring-logo4.png").content
        # this compares the 2   (REPLACE WITH TRY, IF, EXCEPT)
        print('\n')  # adds line break
        if assertEqual(logo_file, svg_url):
            print "image does not match file"
        else:
            print "image matches file"

    def test_correct_bottom_logo_size(self):
        """Is the size correct?"""

        logo = driver.find_elements_by_tag_name("img")[0]
        size = logo.size
        print('\n')  # adds line break
        print "size of the logo is:"
        print (size)

        assertEqual(logo.size["width"], 289)
        assertEqual(logo.size["height"], 69)

    def test_bottom_logo_placement(self):
        """Is the placement correct"""

        logo = driver.find_elements_by_tag_name("img")[0]
        print('\n')  # adds line break
        print "location of logo is at:"
        print (logo.location)

        assertEqual(logo.location, {"y": 50.0, "x": 89.0})

class TestFooterText(object):

    # Centered text
    def test_footer_text(self):
        """Test that the text is present in the footer and centered"""

        footer_text = driver.find_elements_by_css_selector("center")[0].text
        footer1 = "Kcentra is manufactured by CSL Behring GmbH and is distributed by CSL Behring LLC.\nKcentra® is a registered trademark of CSL Behring GmbH.\nBiotherapies for Life® is a registered trademark of CSL Behring LLC.\n©2016 CSL Behring LLC. 1020 First Ave PO Box 61501\nKing of Prussia, PA 19406-0901 USA www.cslbehring-us.com www.kcentra.com\nKCT15-09-0042(1) 10/16"

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(footer_text.encode('utf-8'), footer1):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", footer_text, "'", " text is present"

    def test_correct_footer_attributes(self):
        """This will test the footer text attributes"""

        footer_text = driver.find_elements_by_css_selector("center")[0]
        assertEqual(footer_text.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(footer_text.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(footer_text.value_of_css_property("font-size"), '14px')
        assertEqual(footer_text.value_of_css_property("font-weight"), 'normal')

        # proceed to page 3 (thank you)
        driver.find_element_by_class_name("btn-wrapper").click()
        time.sleep(5)

    def teardown_class(self):
        driver.quit()