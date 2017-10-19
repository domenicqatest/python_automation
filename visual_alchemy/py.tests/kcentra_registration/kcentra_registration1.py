#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Front-end tests for Kcentra.

Usage::
    py.test -s -v --tb=line test_noisey_ui.py

-s: No capture. Don't suppress output.

-v: Verbose. Gimme all the info.

--tb=line: Shorten the tracebacks should an error occur.
"""
#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from selenium.webdriver.support.select import Select
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.common.exceptions import NoAlertPresentException
import requests
import time

base_url = "http://kcentra.reg-portal.va-dev.net/"

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

    def test_save_background(self):
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
        assertEqual(bg.size["height"], 1705)

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
        assertEqual(header.size["height"], 111)

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
        assertEqual(container.size["height"], 1705)

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
        assertEqual(content.size["height"], 1331)

        # Please Select An Event
        please_caps = driver.find_element_by_css_selector("h1.caps").text
        if assertEqual(please_caps, "PLEASE SELECT AN EVENT"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'",please_caps,"'"," text is present"

        please = driver.find_element_by_class_name("caps")
        assertEqual(please.value_of_css_property("color"), 'rgba(123, 43, 130, 1)')
        assertEqual(please.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(please.value_of_css_property("font-size"), '36px')
        assertEqual(please.value_of_css_property("font-weight"), '500')

        # select a date **** DO ACTION CHAINS eventually ****
        select_date = driver.find_element_by_css_selector("label").text
        if assertEqual(select_date, "Select a date"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", select_date, "'", " text is present"

        date = driver.find_element_by_id("month")
        assertEqual(date.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(date.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
        assertEqual(date.value_of_css_property("font-size"), '14px')
        assertEqual(date.value_of_css_property("font-weight"), 'normal')

        # select an event **** DO ACTION CHAINS ****
        select_event = driver.find_element_by_css_selector("#event > label").text
        if assertEqual(select_event, "Select an Event"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", select_event, "'", " text is present"

        event = driver.find_element_by_id("event")
        assertEqual(event.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(event.value_of_css_property("font-family"),
                    'Montserrat-light, sans-serif')
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
        assertEqual(button_wrapper.size["height"], 36)

        # button location
        button = driver.find_element_by_class_name("squareButton")
        print('\n')  # adds line break
        print "location of submit button is at:"
        print (button.location)

        # button size
        button = driver.find_element_by_class_name("squareButton")
        size = button.size
        print('\n')  # adds line break
        print "size of the submit button is:"
        print (size)

        assertEqual(button.size["width"], 100)
        assertEqual(button.size["height"], 26)

        # button triangle location
        button_triangle = driver.find_element_by_class_name("btnTriangle")
        print('\n')  # adds line break
        print "location of submit button triangle is at:"
        print (button_triangle.location)

        # button triangle size
        button_triangle = driver.find_element_by_class_name("btnTriangle")
        size = button_triangle.size
        print('\n')  # adds line break
        print "size of the submit button triangle is:"
        print (size)

        assertEqual(button.size["width"], 100)
        assertEqual(button.size["height"], 26)

    def test_button_attributes(self):
        """This tests the attributes of the support section"""

        button_text = driver.find_element_by_class_name("squareButton").text

        if assertEqual(button_text, "Submit"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", button_text, "'", " text is present"

        button_text2 = driver.find_element_by_class_name("button")
        assertEqual(button_text2.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(button_text2.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(button_text2.value_of_css_property("font-size"), '14px')
        assertEqual(button_text2.value_of_css_property("font-weight"), 'normal')

        button = driver.find_element_by_class_name("formBtnWrapper")
        assertEqual(button.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(button.value_of_css_property("display"), 'block')
        assertEqual(button.value_of_css_property("-webkit-tap-highlight-color"), 'rgba(0, 0, 0, 0)')
        assertEqual(button.value_of_css_property("box-sizing"), 'border-box')

        # line break
        hr = driver.find_element_by_xpath("//*[@id='content']/hr")
        size = hr.size
        print('\n')  # adds line break
        print "size of the header is:"
        print (size)

        assertEqual(hr.location, {"y": 461.0, "x": 89.0})

        assertEqual(hr.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-bottom-color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-left-color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-right-color"), 'rgba(102, 102, 102, 1)')
        assertEqual(hr.value_of_css_property("border-top-color"), 'rgba(238, 238, 238, 1)')
        assertEqual(hr.value_of_css_property("border-top-style"), 'solid')
        assertEqual(hr.value_of_css_property("display"), 'block')

class TestPolicy(object):
    """This tests the policy section"""

    def test_policy_as_a_whole_text(self):
        """This tests the same attributes of the 'p' section"""
        all_policy = driver.find_element_by_css_selector("p")
        assertEqual(all_policy.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(all_policy.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(all_policy.value_of_css_property("font-size"), '14px')
        assertEqual(all_policy.value_of_css_property("font-weight"), 'normal')


    def test_policy_titles(self):
        """This tests the attributes of the policy titles"""

        # title tag name 'b' text and weight
        attendee_text = driver.find_element_by_xpath("//*[@id='content']/div[3]/b[1]").text

        if assertEqual(attendee_text, "ATTENDEE POLICY"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text, "'", " text is present"

        # reporting_text = driver.find_element_by_css_selector("h4.title.left").text
        reporting_text = driver.find_element_by_xpath("//*[@id='content']/div[3]/b[2]").text

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
        # assertEqual(important_text.value_of_css_property("text-decoration"), 'underline')

        # warning_text = driver.find_element_by_css_selector("h4.title.left").text
        warning_text = driver.find_element_by_xpath("//*[@id='content']/div[3]/div/b").text

        if assertEqual(warning_text, "WARNING: ARTERIAL AND VENOUS THROMBOEMBOLIC COMPLICATIONS"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text, "'", " text is present"

        # title tag name 'b' attributes
        attending = driver.find_element_by_xpath("//*[@id='content']/div[3]/b")
        assertEqual(attending.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(attending.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(attending.value_of_css_property("font-size"), '14px')
        assertEqual(attending.value_of_css_property("font-weight"), '900')


    def test_attendee_policy(self):
        """This will save the policy text"""

        attendee_text1 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[1]").text

        attendee1 = "CSL Behring complies with PhRMA Guidelines; therefore, spouses, partners, or guests may not attend any meeting or social function. Spouses and guests will not be permitted to attend any activities related to this meeting, including meal functions, as these are considered part of the official program. If your spouse or a guest is traveling with you, any charges or expenses related to his or her presence will be your personal responsibility."

        if assertEqual(attendee_text1, unicode(attendee1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text1, "'", " text is present"

        attendee_text2 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[2]").text
        attendee2 = "This program is intended for US healthcare providers only."

        if assertEqual(attendee_text2, unicode(attendee2, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text2, "'", " text is present"

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(attendee_text2, unicode(attendee2, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text2, "'", " text is present"

    def test_reporting_policy(self):
        """This will save the policy text"""

        reporting_text1 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[3]").text
        reporting1 = "Personal information provided above will not be used for any other purpose beyond this peer-to-peer program and required federal and state-level reporting."

        if assertEqual(reporting_text1, unicode(reporting1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", reporting_text1, "'", " text is present"

        reporting_text2 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[4]").text
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
        safety_text = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[5]").text
        safety = u"Kcentra® Prothrombin Complex Concentrate (Human), is a blood coagulation factor replacement product indicated for the urgent reversal of acquired coagulation factor deficiency induced by Vitamin K antagonist (VKA—eg, warfarin) therapy in adult patients with acute major bleeding or the need for urgent surgery or other invasive procedure. Kcentra is for intravenous use only."

        # Add unicode(----, "utf-8")): to get the characters accepted
        #if assertEqual(safety_text, unicode(safety, "utf-8")):
        if assertEqual(safety_text, safety):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", safety_text, "'", " text is present"

    def test_warning_policy(self):
        """This will save the policy text"""

        warning_text1 = driver.find_element_by_css_selector("p > b").text
        warning1 = "Patients being treated with Vitamin K antagonist therapy have underlying disease states that predispose them to thromboembolic events. Potential benefits of reversing VKA should be weighed against the risk of thromboembolic events, especially in patients with history of such events. Resumption of anticoagulation therapy should be carefully considered once the risk of thromboembolic events outweighs the risk of acute bleeding. Both fatal and nonfatal arterial and venous thromboembolic complications have been reported in clinical trials and postmarketing surveillance. Monitor patients receiving Kcentra, and inform them of signs and symptoms of thromboembolic events. Kcentra was not studied in subjects who had a thromboembolic event, myocardial infarction, disseminated intravascular coagulation, cerebral vascular accident, transient ischemic attack, unstable angina pectoris, or severe peripheral vascular disease within the prior 3 months. Kcentra might not be suitable for patients with thromboembolic events in the prior 3 months."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text1, unicode(warning1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text1, "'", " text is present"

        warning_text2 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[6]").text
        warning2 = "Kcentra is contraindicated in patients with known anaphylactic or severe systemic reactions to Kcentra or any of its components (including heparin, Factors II, VII, IX, X, Proteins C and S, Antithrombin III and human albumin). Kcentra is also contraindicated in patients with disseminated intravascular coagulation. Because Kcentra contains heparin, it is contraindicated in patients with heparin-induced thrombocytopenia (HIT)."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text2, unicode(warning2, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text2, "'", " text is present"

        warning_text3 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[7]").text
        warning3 = "Hypersensitivity reactions to Kcentra may occur. If patient experiences severe allergic or anaphylactic type reactions, discontinue administration and institute appropriate treatment."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text3, unicode(warning3, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text3, "'", " text is present"

        warning_text4 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[8]").text
        warning4 = u"In clinical trials, the most frequent (≥2.8%) adverse reactions observed in subjects receiving Kcentra were headache, nausea/vomiting, hypotension, and anemia. The most serious adverse reactions were thromboembolic events, including stroke, pulmonary embolism and deep vein thrombosis."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text4, warning4):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text4, "'", " text is present"

        warning_text5 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[9]").text
        warning5 = "Kcentra is derived from human plasma. The risk of transmission of infectious agents, including viruses and, theoretically, the Creutzfeldt-Jakob disease (CJD) agent, cannot be completely eliminated."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text5, unicode(warning5, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text5, "'", " text is present"

        warning_text6 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[10]").text
        warning6 = "The safety and efficacy of Kcentra in pediatric use have not been studied, and Kcentra should be used in women who are pregnant or nursing only if clearly needed."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text6, unicode(warning6, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text6, "'", " text is present"

        warning_text7 = driver.find_element_by_xpath("//div[@id='content']/div[3]/p[11]").text
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
        assertEqual(all_policy_text.value_of_css_property("font-size"), '14px')
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
        driver.find_element_by_link_text("full prescribing information").click()
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

        assertEqual(footer.location, {"y": 1542.0, "x": 89.0})

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

    def test_save_logo(self):
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

        assertEqual(logo.location, {"y": 70.0, "x": 89.0})

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

        assertEqual(header.location, {"y": 149.0, "x": 89.0})

    # BOTTOM Logo
    def test_bottom_logo(self):
        """Test correct logo present"""

        print('\n' * 2)  # adds line break
        logo = driver.find_elements_by_tag_name("center")[1]

        if logo.is_displayed():
            print "logo found"
        else:
            print "logo not found"

    def test_save_bottom_logo(self):
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

        assertEqual(logo.location, {"y": 70.0, "x": 89.0})

class TestFooterText(object):

    # Centered text
    def footer_text(self):
        """Test that the text is present in the footer and centered"""

        footer_text = driver.find_elements_by_css_selector("center")[0].text
        footer1 = u"Kcentra is manufactured by CSL Behring GmbH and is distributed by CSL Behring LLC.\nKcentra® is a registered trademark...First Ave PO Box 61501\nKing of Prussia, PA 19406-0901 USA www.cslbehring-us.com www.kcentra.com\nKCT15-09-0042(1) 10/16"
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(footer_text, footer1):
        #if assertEqual(footer_text, unicode(footer1, "utf-8")):
            print('\n')  # adds line break
        #print "text not found"
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

        print('\n')  # adds line break
        print footer_text.text

    def test_date_dropdown(self):
        """verifies the contents of the date drop down"""

        dates = Select(driver.find_element_by_id("id_month"))
        date_list = [o.text for o in dates.options]

        assertEqual(date_list,
                    [
                        u'------------',
                        u'2017 April'
                    ]
                    )

 # Event drop down verification comes AFTER selecting a date

class TestFillingOutForm(object):

    # Filling the form out
    def error_text(self):
        """Negative test the form"""
        # click the button
        driver.find_element_by_class_name("button").click()
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
        """Verify the contents of the event drop down"""

        # To make the events visible you must first select the first part of the form
        time.sleep(1)
        Select(driver.find_element_by_id("id_month")).select_by_visible_text("2017 April")
        time.sleep(3)


        events = Select(driver.find_element_by_id("id_event"))
        event_list = [o.text for o in events.options]

        assertEqual(event_list,
                    [
                    u'Venue: #420'
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
        Select(driver.find_element_by_id("id_month")).select_by_visible_text("2017 April")
        time.sleep(1)
        Select(driver.find_element_by_id("id_event")).select_by_visible_text("Venue: #420")
        driver.find_element_by_css_selector("button").click()
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
