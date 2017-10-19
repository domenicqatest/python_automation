# -*- coding: utf-8 -*-

#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time

base_url = "http://kcentra.reg-portal.va-dev.net/confirmation/420/"

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
        assertEqual(bg.size["height"], 1644)

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
        assertEqual(container.size["height"], 1644)

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
        assertEqual(content.size["height"], 280)

        # Thank you for your registration...
        thanks = driver.find_element_by_xpath("//*[@id='confirmation']/div/div[1]/p").text
        if assertEqual(thanks, "Thank you for your registration.\nWe will be in touch with program details shortly."):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'",thanks,"'"," text is present"

        thanks2 = driver.find_element_by_xpath("//*[@id='confirmation']/div/div[1]/p")
        assertEqual(thanks2.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(thanks2.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(thanks2.value_of_css_property("font-size"), '18px')
        assertEqual(thanks2.value_of_css_property("font-weight"), 'bold')


class TestAddAdditional(object):
    """This tests the button"""

    def test_add_link(self):
        """This tests the attributes of the add button"""

        # button location
        add = driver.find_element_by_class_name("add-another-reg")
        print('\n')  # adds line break
        print "location of submit button is at:"
        print (add.location)

        # button size
        add = driver.find_element_by_class_name("add-another-reg")
        size = add.size
        print('\n')  # adds line break
        print "size of the submit button is:"
        print (size)

        assertEqual(add.size["width"], 720)
        assertEqual(add.size["height"], 20)

        # text hover state (ACTION CHAINS)
        add = driver.find_element_by_class_name("add-another-reg")
        #verify text before hover
        assertEqual(add.value_of_css_property("color"), 'rgba(176, 186, 54, 1)')
        # hover over text
        hover = ActionChains(driver).move_to_element(add)
        hover.perform()
        # verify hover text
        time.sleep(1)
        assertEqual(add.value_of_css_property("color"), 'rgba(35, 82, 124, 1)')

        # add text attributes
        add_text = driver.find_element_by_class_name("add-another-reg").text
        if assertEqual(add_text, "Add Additional Registrant"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", add_text, "'", " text is present"

        add_text2 = driver.find_element_by_class_name("add-another-reg")
        assertEqual(add_text2.value_of_css_property("color"), 'rgba(35, 82, 124, 1)')
        assertEqual(add_text2.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(add_text2.value_of_css_property("font-size"), '14px')
        assertEqual(add_text2.value_of_css_property("font-weight"), 'normal')
        assertEqual(add_text2.value_of_css_property("-webkit-tap-highlight-color"), 'rgba(0, 0, 0, 0)')

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

        assertEqual(support_cell.size["width"], 600)
        #assertEqual(support_cell.size["height"], 219)

class TestPolicy(object):
    """This tests the policy section"""

    def test_policy_as_a_whole_text(self):
        """This tests the same attributes of the 'p' section"""
        all_policy = driver.find_element_by_css_selector("p")
        assertEqual(all_policy.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(all_policy.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(all_policy.value_of_css_property("font-size"), '18px')
        assertEqual(all_policy.value_of_css_property("font-weight"), 'bold')


    def test_policy_titles(self):
        """This tests the attributes of the policy titles"""

        # title tag name 'b' text and weight
        attendee_text = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/b[1]").text

        if assertEqual(attendee_text, "ATTENDEE POLICY"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text, "'", " text is present"

        # reporting_text = driver.find_element_by_css_selector("h4.title.left").text
        reporting_text = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/b[2]").text

        if assertEqual(reporting_text, "REPORTING POLICY"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", reporting_text, "'", " text is present"

        important_text = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/b[3]").text

        if assertEqual(important_text, "Important Safety Information"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", important_text, "'", " text is present"

        warning_text = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/b[4]").text

        if assertEqual(warning_text, "WARNING: ARTERIAL AND VENOUS THROMBOEMBOLIC COMPLICATIONS"):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text, "'", " text is present"

        # title tag name 'b' attributes
        attending = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/b")
        assertEqual(attending.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
        assertEqual(attending.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(attending.value_of_css_property("font-size"), '14px')
        assertEqual(attending.value_of_css_property("font-weight"), '900')


    def test_attendee_policy(self):
        """This will save the policy text"""

        attendee_text1 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[1]").text

        attendee1 = "CSL Behring complies with PhRMA Guidelines; therefore, spouses, partners, or guests may not attend any meeting or social function. Spouses and guests will not be permitted to attend any activities related to this meeting, including meal functions, as these are considered part of the official program. If your spouse or a guest is traveling with you, any charges or expenses related to his or her presence will be your personal responsibility."

        if assertEqual(attendee_text1, unicode(attendee1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", attendee_text1, "'", " text is present"

        attendee_text2 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[2]").text
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

        reporting_text1 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[3]").text
        reporting1 = "Personal information provided above will not be used for any other purpose beyond this peer-to-peer program and required federal and state-level reporting."

        if assertEqual(reporting_text1, unicode(reporting1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", reporting_text1, "'", " text is present"

        reporting_text2 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[4]").text
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
        safety_text = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[5]").text
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

        warning_text1 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[6]/b").text
        warning1 = "Patients being treated with Vitamin K antagonist therapy have underlying disease states that predispose them to thromboembolic events. Potential benefits of reversing VKA should be weighed against the risk of thromboembolic events, especially in patients with history of such events. Resumption of anticoagulation therapy should be carefully considered once the risk of thromboembolic events outweighs the risk of acute bleeding. Both fatal and nonfatal arterial and venous thromboembolic complications have been reported in clinical trials and postmarketing surveillance. Monitor patients receiving Kcentra, and inform them of signs and symptoms of thromboembolic events. Kcentra was not studied in subjects who had a thromboembolic event, myocardial infarction, disseminated intravascular coagulation, cerebral vascular accident, transient ischemic attack, unstable angina pectoris, or severe peripheral vascular disease within the prior 3 months. Kcentra might not be suitable for patients with thromboembolic events in the prior 3 months."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text1, unicode(warning1, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text1, "'", " text is present"

        warning_text2 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[7]").text
        warning2 = "Kcentra is contraindicated in patients with known anaphylactic or severe systemic reactions to Kcentra or any of its components (including heparin, Factors II, VII, IX, X, Proteins C and S, Antithrombin III and human albumin). Kcentra is also contraindicated in patients with disseminated intravascular coagulation. Because Kcentra contains heparin, it is contraindicated in patients with heparin-induced thrombocytopenia (HIT)."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text2, unicode(warning2, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text2, "'", " text is present"

        warning_text3 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[8]").text
        warning3 = "Hypersensitivity reactions to Kcentra may occur. If patient experiences severe allergic or anaphylactic type reactions, discontinue administration and institute appropriate treatment."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text3, unicode(warning3, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text3, "'", " text is present"

        warning_text4 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[9]").text
        warning4 = u"In clinical trials, the most frequent (≥2.8%) adverse reactions observed in subjects receiving Kcentra were headache, nausea/vomiting, hypotension, and anemia. The most serious adverse reactions were thromboembolic events, including stroke, pulmonary embolism and deep vein thrombosis."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text4, warning4):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text4, "'", " text is present"

        warning_text5 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[10]").text
        warning5 = "Kcentra is derived from human plasma. The risk of transmission of infectious agents, including viruses and, theoretically, the Creutzfeldt-Jakob disease (CJD) agent, cannot be completely eliminated."

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text5, unicode(warning5, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text5, "'", " text is present"

        warning_text6 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[11]").text
        warning6 = "The safety and efficacy of Kcentra in pediatric use have not been studied, and Kcentra should be used in women who are pregnant or nursing only if clearly needed."
        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(warning_text6, unicode(warning6, "utf-8")):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", warning_text6, "'", " text is present"

        warning_text7 = driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[12]").text
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
        assertEqual(all_policy_text.value_of_css_property("font-weight"), 'bold')

        # link at the bottom
        link = driver.find_element_by_link_text("full prescribing information")
        assertEqual(link.value_of_css_property("color"), 'rgba(176, 186, 54, 1)')
        assertEqual(link.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(link.value_of_css_property("font-size"), '14px')
        assertEqual(link.value_of_css_property("font-weight"), 'normal')

    def test_click_link(self):
        """This will verify the link, click it, and close the new tab"""
        ### Click out isn't functioning on the site
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='footer-content']/footer/div/p[12]/a").click()
        #driver.find_element_by_link_text("full prescribing information").click()
        #time.sleep(3)
        # put focus on newly opened tab
        #driver.switch_to.window(driver.window_handles[-1])
        # close the tab
        #driver.close()
        # switch to the main tab
        #driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

    # Footer
    def test_footer(self):
        """Test correct footer present"""
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
        assertEqual(footer.size["height"], 1263)

    def test_footer_placement(self):
        """Is the placement correct"""

        footer = driver.find_element_by_id("footer")
        print('\n')  # adds line break
        print "location of header is at:"
        print (footer.location)

        assertEqual(footer.location, {"y": 431.0, "x": 89.0})

        # footer background color
        footer = driver.find_element_by_id("footer")
        assertEqual(footer.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')

        assertEqual(footer.size["width"], 720)
        assertEqual(footer.size["height"], 1263)

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

        assertEqual(logo.location, {"y": 50.0, "x": 95.0})

    # Header Border
    def test_header_border(self):
        """Test correct header present"""

        print('\n' * 2)  # adds line break
        header = driver.find_element_by_id("header")

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
        print "location of header border is at:"
        print (header.location)

        assertEqual(header.location, {"y": 50.0, "x": 89.0})

    # BOTTOM Logo
    def test_bottom_logo(self):
        """Test correct logo present"""

        print('\n' * 2)  # adds line break
        csl_logo = driver.find_elements_by_tag_name("img")[1]

        if csl_logo.is_displayed():
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

        csl_logo = driver.find_elements_by_tag_name("img")[1]
        size = csl_logo.size
        print('\n')  # adds line break
        print "size of the logo is:"
        print (size)

        assertEqual(csl_logo.size["width"], 244)
        assertEqual(csl_logo.size["height"], 53)

    def test_bottom_logo_placement(self):
        """Is the placement correct"""

        csl_logo = driver.find_elements_by_tag_name("img")[1]
        print('\n')  # adds line break
        print "location of logo is at:"
        print (csl_logo.location)

        assertEqual(csl_logo.location, {"y": 1621.0, "x": 361.0})

class TestFooterText(object):

    # Centered text
    def test_footer_text(self):
        """Test that the text is present in the footer and centered"""

        footer_text = driver.find_elements_by_tag_name("center")[0].text
        footer1 = "Kcentra is manufactured by CSL Behring GmbH and is distributed by CSL Behring LLC.\nKcentra® is a registered trademark of CSL Behring GmbH.\nBiotherapies for Life® is a registered trademark of CSL Behring LLC.\n©2016 CSL Behring LLC. 1020 First Ave PO Box 61501\nKing of Prussia, PA 19406-0901 USA www.cslbehring-us.com www.kcentra.com\nKCTXX-XX-XX(X) 10/16"

        # Add unicode(----, "utf-8")): to get the characters accepted
        if assertEqual(footer_text.encode('utf-8'), footer1):
            print('\n')  # adds line break
            print "text not found"
        else:
            print('\n')  # adds line break
            print "'", footer_text, "'", " text is present"

    def test_correct_footer_attributes(self):
        """This will test the footer text attributes"""

        footer_text = driver.find_elements_by_tag_name("center")[0]
        assertEqual(footer_text.value_of_css_property("color"), 'rgba(102, 102, 102, 1)')
        assertEqual(footer_text.value_of_css_property("font-family"), 'Montserrat-light, sans-serif')
        assertEqual(footer_text.value_of_css_property("font-size"), '14px')
        assertEqual(footer_text.value_of_css_property("font-weight"), 'normal')

        time.sleep(5)

    def teardown_class(self):
        driver.quit()