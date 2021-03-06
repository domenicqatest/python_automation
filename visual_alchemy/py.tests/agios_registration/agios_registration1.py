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

base_url = "http://registration.agios.va-dev.net"

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
        bg_url = requests.get("https://va-mosaic-agios-beta.s3.amazonaws.com/images/main-bg.jpg").content
        # this saves the data into the SVG text file
        bg_file.write(bg_url)

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
        assertEqual(bg.size["height"], 838)

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
        assertEqual(container.size["height"], 838)

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
        assertEqual(content.size["height"], 271)

        # Please Select An Event
        font_large = driver.find_element_by_css_selector("h1.font-large").text
        if assertEqual(font_large, "PLEASE SELECT AN EVENT"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'",font_large,"'"," text is present"

        please = driver.find_element_by_class_name("font-large")
        assertEqual(please.value_of_css_property("color"), 'rgba(3, 78, 128, 1)')
        assertEqual(please.value_of_css_property("font-family"), '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(please.value_of_css_property("font-size"), '25px')
        assertEqual(please.value_of_css_property("font-weight"), '500')

        # select a date **** DO ACTION CHAINS eventually ****
        select_date = driver.find_element_by_css_selector("label").text
        if assertEqual(select_date, "Select a date"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", select_date, "'", " text is present"

        date = driver.find_element_by_id("date")
        assertEqual(date.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(date.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(date.value_of_css_property("font-size"), '14px')
        assertEqual(date.value_of_css_property("font-weight"), 'normal')

        # select an event **** DO ACTION CHAINS ****
        select_event = driver.find_element_by_css_selector("#event > label").text
        if assertEqual(select_event, "Select an event"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", select_event, "'", " text is present"

        event = driver.find_element_by_id("event")
        assertEqual(event.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(event.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(event.value_of_css_property("font-size"), '14px')
        assertEqual(event.value_of_css_property("font-weight"), 'normal')

        # required field stars
        stars = driver.find_elements_by_class_name("star")[0 - 1]
        print('\n')  # adds line break

        if stars.is_displayed():
            print "Relevant fields marked as required"
        else:
            print "Relevant fields NOT all marked as required"

class TestButton(object):
    """This tests the button"""

    def test_submit_button(self):
        """This tests the attributes of the submit button"""

        # wrapper location
        button_wrapper = driver.find_element_by_class_name("formBtnWrapper")
        print('\n')  # adds line break
        print "location of submit button is at:"
        print (button_wrapper.location)

        # wrapper size
        button_wrapper = driver.find_element_by_class_name("formBtnWrapper")
        size = button_wrapper.size
        print('\n')  # adds line break
        print "size of the submit button is:"
        print (size)

        assertEqual(button_wrapper.size["width"], 600)
        assertEqual(button_wrapper.size["height"], 40)

        # button location
        button = driver.find_element_by_class_name("button")
        print('\n')  # adds line break
        print "location of submit button is at:"
        print (button.location)

        # button size
        button = driver.find_element_by_class_name("button")
        size = button.size
        print('\n')  # adds line break
        print "size of the submit button is:"
        print (size)

        assertEqual(button.size["width"], 200)
        assertEqual(button.size["height"], 40)

        # button hover state (ACTION CHAINS)
        button = driver.find_element_by_class_name("button")
        #verify button drop shadow before hover
        assertEqual(button.value_of_css_property("box-shadow"), 'rgba(0, 0, 0, 0.156863) 0px 3px 6px 0px, rgba(0, 0, 0, 0.227451) 0px 3px 6px 0px')
        # hover over control menu
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()
        # verify hover state
        time.sleep(1)
        assertEqual(button.value_of_css_property("box-shadow"), 'rgba(0, 0, 0, 0.247059) 0px 14px 28px 0px, rgba(0, 0, 0, 0.219608) 0px 10px 10px 0px')

        # button attributes
        button_text = driver.find_element_by_css_selector("button.button").text

        if assertEqual(button_text, "SUBMIT"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", button_text, "'", " text is present"

        button_text2 = driver.find_element_by_class_name("button")
        assertEqual(button_text2.value_of_css_property("color"), 'rgba(255, 255, 255, 1)')
        assertEqual(button_text2.value_of_css_property("font-family"), '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(button_text2.value_of_css_property("font-size"), '14px')
        assertEqual(button_text2.value_of_css_property("font-weight"), 'normal')

        button = driver.find_element_by_class_name("formBtnWrapper")
        assertEqual(button.value_of_css_property("color"), 'rgba(51, 51, 51, 1)')
        assertEqual(button.value_of_css_property("display"), 'block')
        assertEqual(button.value_of_css_property("-webkit-tap-highlight-color"), 'rgba(0, 0, 0, 0)')
        assertEqual(button.value_of_css_property("box-sizing"), 'border-box')

    def test_support(self):
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
        """This will save the policy text"""

        policy_text = driver.find_element_by_css_selector("p").text
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

        assertEqual(footer.location, {"y": 688.0, "x": 76.0})

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

        assertEqual(hr.location, {"y": 728.0, "x": 76.0})

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

    def test_save_logo(self):
        """print SVG"""

        # this is the SVG text file
        logo_file = open('utils/logo.txt', 'w')
        # this requests the data from the URL
        svg_url = requests.get("https://va-mosaic-agios.s3.amazonaws.com/logos/agios-logo.svg").content
        # this saves the data into the SVG text file
        logo_file.write(svg_url)

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

    def test_save_header(self):
        """print SVG"""

        # this is the SVG text file
        header_file = open('utils/header_border.txt', 'w')
        # this requests the data from the URL
        header_url = requests.get(
            "https://va-mosaic-agios-beta.s3.amazonaws.com/images/agios/horizontal-bar.png").content
        # this saves the data into the SVG text file
        header_file.write(header_url)

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

        assertEqual(logo.location, {"y": 750.0, "x": 349.0})

class TestContentFunctionality(object):

    # Form
    def test_body_text(self):
        """Please Select An Event"""

    def test_date_dropdown(self):
        """verifies the contents of the date drop down"""

        dates = Select(driver.find_element_by_id("id_date"))
        date_list = [o.text for o in dates.options]

        assertEqual(date_list,
                    [
                        u'------------',
                        u'28 April 2017',
                        u'30 April 2017',
                        u'01 May 2017'
                    ]
                    )

 # Event drop down verification comes AFTER selecting a date

class TestFillingOutForm(object):

    # Filling the form out
    def test_error_text(self):
        """Negative test the form"""
        # click the button
        driver.find_element_by_css_selector("button.button").click()
        time.sleep(1)

        # If alert is present, close it
        try:
            driver.switch_to_alert().accept()
        except NoAlertPresentException as e:
            print('\n')  # adds line break
            print("no alert")
        time.sleep(1)

        # this is the event error text file
        error_text = open('utils/error.txt', 'r').read()
        # this requests the error data from the URL
        error = driver.find_element_by_id("event").text

        if assertEqual(error_text, error):
            print('\n')  # adds line break
            print "error text not found"
        else:
            print('\n')  # adds line break
            print "'", error_text, "'", " error text is present"
        print('\n')  # adds line break

        # ERROR Text ATTRIBUTES
        error_text1 = driver.find_element_by_name("event")
        assertEqual(error_text1.value_of_css_property("color"), 'rgba(85, 85, 85, 1)')
        assertEqual(error_text1.value_of_css_property("font-family"),
                    '"Helvetica Neue", Helvetica, Arial, sans-serif')
        assertEqual(error_text1.value_of_css_property("font-size"), '14px')
        assertEqual(error_text1.value_of_css_property("font-weight"), 'normal')

    def test_verify_drop_down(self):
        """Verify the contents of the event drop down: There will be 3 instances of this"""
    #1
        # To make the events visible you must first select the first part of the form
        time.sleep(1)
        Select(driver.find_element_by_id("id_date")).select_by_visible_text("28 April 2017")
        time.sleep(3)


        events = Select(driver.find_element_by_id("id_event"))
        event_list = [o.text for o in events.options]

        assertEqual(event_list,
                    [
                    u'Test venue - NEW WINDSOR, FL',
                    ]
                    )

        # verify the options in the date drop down AND event drop down AFTER activating the event drop down.
        print('\n')  # adds line break
        print "All options in the dropdowns are:"
        for element in driver.find_elements_by_css_selector("option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    #2
        # To make the events visible you must first select the first part of the form
        time.sleep(1)
        Select(driver.find_element_by_id("id_date")).select_by_visible_text("30 April 2017")
        time.sleep(3)

        events = Select(driver.find_element_by_id("id_event"))
        event_list = [o.text for o in events.options]

        assertEqual(event_list,
                    [
                        u"Del Frisco's Double Eagle Steak House - New York, NY",
                    ]
                    )

        # verify the options in the date drop down AND event drop down AFTER activating the event drop down.
        print('\n')  # adds line break
        print "All options in the dropdowns are:"
        for element in driver.find_elements_by_css_selector("option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    #3
        # To make the events visible you must first select the first part of the form
        time.sleep(1)
        Select(driver.find_element_by_id("id_date")).select_by_visible_text("01 May 2017")
        time.sleep(3)

        events = Select(driver.find_element_by_id("id_event"))
        event_list = [o.text for o in events.options]

        assertEqual(event_list,
                    [
                        u'SJ Steak House - ANN ARBOR, CT',
                    ]
                    )

        # verify the options in the date drop down AND event drop down AFTER activating the event drop down.
        print('\n')  # adds line break
        print "All options in the dropdowns are:"
        for element in driver.find_elements_by_css_selector("option"):
            print('\n')  # adds line break
            print element.get_attribute('innerHTML')

    def test_form(self):
        """Filling out the rest of the form"""

        time.sleep(1)
        Select(driver.find_element_by_id("id_date")).select_by_visible_text("30 April 2017")
        time.sleep(1)
        Select(driver.find_element_by_id("id_event")).select_by_visible_text("Del Frisco's Double Eagle Steak House - New York, NY")
        driver.find_element_by_css_selector("button.button").click()
        time.sleep(2)

        try:
            driver.switch_to_alert().accept()
        except NoAlertPresentException as e:
            print('\n')  # adds line break
            print("no alert")
            print('\n')  # adds line break

        driver.get(base_url)
        time.sleep(2)

    def teardown_class(self):
        driver.quit()
