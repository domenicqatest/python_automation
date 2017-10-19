"""Usage::
    py.test -s -v --tb=line test_[test_name].py

-s: No capture. Don't suppress output.

-v: Verbose. Gimme all the info.

--tb=line: Shorten the tracebacks should an error occur."""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest

base_url = "https://vice:welcome@staging-video.viceops.net/en_us"

class TestVideoFeatures(object):
        """This is what you're accomplishing with this group"""
        def setup_class(self):
            """This is what the setup needs to be"""
            self.driver = webdriver.Chrome()
            self.driver.set_window_size(1280, 800)
            #self.driver.get("https://video.vice.com/en_us/video/guardian-angels-1/576c539277a2a2485d814464")
            self.driver.get("https://vice:welcome@staging-video.viceops.net/en_us/video/guardian-angels-1/576c539277a2a2485d814464")
            #self.driver.get("https://vice:welcome@dev-video.viceops.net/en_us/video/robot-vs-ied/55d207f423652a5532d4fbf0")

    ##########

        def test_ad_clickthrough_part1(self):
            """this clicks through the ad"""
            ## ADD DURATION TESTS!##
            time.sleep(1)
            advertisement = self.driver.find_element_by_class_name("vp-player-clicks")
            if advertisement.is_displayed():
                time.sleep(1)
                # click out (pauses video)
                self.driver.find_element_by_class_name("vp-player-clicks").click()
                time.sleep(1)
                # put focus on newly opened tab
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # close the tab
                self.driver.close()
                # switch to the main window
                self.driver.switch_to.window(self.driver.window_handles[0])
                # click play when you return from ad
                self.driver.find_element_by_class_name("jw-icon-playback").click()
                time.sleep(1)
                # test mute
                self.driver.find_element_by_class_name("jw-slider-volume").click()
                time.sleep(1)
                # wait rest of the ad out and add sleep if not running countdown test
                print "Waiting for ad..."
                time.sleep(35)

            else:
                print "No ad present... proceeding."
                pass #and proceed with tests
                # refresh to run ad again
            #self.driver.refresh()


        def test_video_controls(self):
            """Testing the video control panel"""
            # wait til ad is done playing (30 second ad is the max.)
            control_menu = self.driver.find_element_by_class_name("jw-media")
            # hover over control menu
            hover = ActionChains(self.driver).move_to_element(control_menu)
            hover.perform()

            # mute
            mute = self.driver.find_element_by_class_name("jw-slider-volume")
            # click 30 second replay button
            thirty_seconds_back = self.driver.find_element_by_class_name("jw-icon-replay")
            # click pause
            pause = self.driver.find_element_by_class_name("jw-icon-playback")
            # click play
            play = self.driver.find_element_by_class_name("jw-icon-playback")
            # click CC
            cc = self.driver.find_element_by_class_name("jw-icon-cc").click()
            # click fullscreen / exit fullscreen
            fullscreen = self.driver.find_element_by_class_name("jw-icon-fullscreen")
            time.sleep(2)

            ActionChains(self.driver).move_to_element(control_menu).click(mute).perform()
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(thirty_seconds_back).perform()
            time.sleep(2)

            ActionChains(self.driver).move_to_element(control_menu).click(cc).perform()
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(pause).perform()
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(play).perform()
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(fullscreen).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        def test_video_quality(self):
            """This tests the video resolutions"""

            print('\n')  # adds line break
            # visual verification in terminal:
            print("Resolution Menu Option Order:")
            for element in self.driver.find_elements_by_class_name("jw-option"):
                print element.get_attribute('innerHTML')
            #
            def verify_locale_languages(self):
                """Verifies the names of the resolutions in the dropdown."""
                resolutions = self.driver.find_elements_by_class_name("jw-option")
                resolutions_list = [resolutions[i].text for i in xrange(8)]
                assertEqual(resolutions_list,
                            [
                                'Auto',
                                '234p',
                                '396p',
                                '504p',
                                '720p',
                                '1080p',
                                '108p',
                                '144p',
                            ]
                            )

            active = self.driver.find_element_by_class_name("jw-active-option")
            control_menu = self.driver.find_element_by_class_name("jw-media")
            quality_menu = self.driver.find_element_by_class_name("jw-menu")
            cog = self.driver.find_element_by_class_name("jw-icon-hd")

            #
            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            ActionChains(self.driver).move_to_element(quality_menu).perform()

            # print first active resolution
            print('\n' * 2)  # adds line break
            print("Detected Resolution:")
            print (active).text

            # click video quality cog
            cog = self.driver.find_element_by_class_name("jw-icon-hd")
            control_menu = self.driver.find_element_by_class_name("jw-media")
            quality_menu = self.driver.find_element_by_class_name("jw-menu")
            seven = self.driver.find_element_by_class_name("jw-item-7")
            #seven = self.driver.find_elements_by_css_selector(".jw-option[value='144p']")
            six = self.driver.find_element_by_class_name("jw-item-6")
            #six = self.driver.find_elements_by_css_selector(".jw-option[value='108p']")
            five = self.driver.find_element_by_class_name("jw-item-5")
            #five = self.driver.find_elements_by_css_selector(".jw-option[value='1080p']")
            four = self.driver.find_element_by_class_name("jw-item-4")
            #four = self.driver.find_elements_by_css_selector(".jw-option[value='720p']")
            three = self.driver.find_element_by_class_name("jw-item-3")
            #three = self.driver.find_elements_by_css_selector(".jw-option[value='504p']")
            two = self.driver.find_element_by_class_name("jw-item-2")
            #two = self.driver.find_elements_by_css_selector(".jw-option[value='396p']")
            one = self.driver.find_element_by_class_name("jw-item-1")
            #one = self.driver.find_elements_by_css_selector(".jw-option[value='234p']")
            auto = self.driver.find_element_by_class_name("jw-item-0")
            #auto = self.driver.find_elements_by_css_selector(".jw-option[value='Auto']")

            # hover over control menu
            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # hover over quality menu
            quality_hover = ActionChains(self.driver).move_to_element(quality_menu)
            quality_hover.perform()

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # click Auto
            ActionChains(self.driver).move_to_element(quality_menu).click(auto).perform()
            # make sure it switches
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # click 234p
            ActionChains(self.driver).move_to_element(quality_menu).click(one).perform()
            # make sure it switches
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # click 396p
            ActionChains(self.driver).move_to_element(quality_menu).click(two).perform()
            # make sure it switches
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # click 504p
            ActionChains(self.driver).move_to_element(quality_menu).click(three).perform()
            # make sure it switches
            time.sleep(1)

            # click 720p
            ActionChains(self.driver).move_to_element(quality_menu).click(four).perform()
            # make sure it switches
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # click 1080p
            ActionChains(self.driver).move_to_element(quality_menu).click(five).perform()
            # make sure it switches
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # click 108p
            ActionChains(self.driver).move_to_element(quality_menu).click(six).perform()
            # make sure it switches
            time.sleep(1)

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            # click 144p
            ActionChains(self.driver).move_to_element(quality_menu).click(seven).perform()
            # make sure it switches
            time.sleep(5)

            # print the last active resolution
            last_active = self.driver.find_element_by_class_name("jw-active-option")
            control_menu = self.driver.find_element_by_class_name("jw-media")
            quality_menu = self.driver.find_element_by_class_name("jw-menu")
            cog = self.driver.find_element_by_class_name("jw-icon-hd")

            ActionChains(self.driver).move_to_element(control_menu).click(cog).perform()

            ActionChains(self.driver).move_to_element(quality_menu).perform()
            print('\n' * 2)  # adds line breaks
            print("Last Active Resolution:")
            print (last_active).text

            def assertEqual(x, y):
                last_chosen = self.driver.find_element_by_class_name("jw-active-option")
                last_resolution = self.driver.find_element_by_class_name("jw-item-7")

                assertEqual(last_chosen, last_resolution)

            ##

            # vp-video-info (make test to make sure it matches the 'video-info')
            def assertEqual(x, y):
                vp_video_title = self.driver.find_element_by_xpath("//div[@id='player']/div/div/div/div[3]/div/div/h2")
                vp_video_summary = self.driver.find_element_by_xpath(
                    "//div[@id='player']/div/div/div/div[3]/div/div/h1")
                video_info_title = self.driver.find_element_by_xpath(
                    "//div[@id='app']/div[2]/section[2]/header/div[1]/div[1]/h2[1]/a")
                video_info_summary = self.driver.find_element_by_xpath(
                    "//div[@id='app']/div[2]/section[2]/header/div[1]/div[1]/h2[2]")

                assertEqual(vp_video_title, video_info_title)
                assertEqual(vp_video_summary, video_info_summary)

        def test_social_links(self):
            """Test Social and Embeds"""

            control_menu = self.driver.find_element_by_class_name("jw-media")
            # hover over control menu
            hover = ActionChains(self.driver).move_to_element(control_menu)
            hover.perform()

            # facebook
            fb = self.driver.find_element_by_class_name("icon-facebook").click()
            ActionChains(self.driver).move_to_element(control_menu).click(fb).perform()

            # if signed in... if not signed in.

            time.sleep(3)
            # new window will be the last object in the window_handles list
            self.driver.switch_to.window(self.driver.window_handles[-1])
            # close the window
            self.driver.close()
            # switch to the main window
            self.driver.switch_to.window(self.driver.window_handles[0])

            # twitter
            twitter = self.driver.find_element_by_class_name("icon-twitter").click()
            ActionChains(self.driver).move_to_element(control_menu).click(twitter).perform()
            time.sleep(3)
            # new window will be the last object in the window_handles list
            self.driver.switch_to.window(self.driver.window_handles[-1])
            # close the window
            self.driver.close()
            # switch to the main window
            self.driver.switch_to.window(self.driver.window_handles[0])

            # embed / embed close - EXPAND ON THIS!
            # open
            embed = self.driver.find_element_by_class_name("icon-embed").click()
            ActionChains(self.driver).move_to_element(control_menu).click(embed).perform()
            time.sleep(1)
            # verify code is present
            assert self.driver.find_element_by_class_name("vp-video-embed-content")
            assert self.driver.find_element_by_class_name("embed-input")
            # close
            self.driver.find_element_by_class_name("vp-video-embed-close").click()
            time.sleep(1)

##### DO VOLUME SLIDER

        def volume_slider(self):
            """test slider"""
            time.sleep(1)
            self.driver.find_element_by_class_name("jw-icon-playback").click()
            time.sleep(35)
            # control menu
            element = self.driver.find_element_by_class_name("jw-media")
            # hover over control menu
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            # slide slider
            volume_slider = self.driver.find_element_by_class_name("jw-knob")
            #volume_slider = self.driver.find_element_by_class_name("jw-rail")
            width = volume_slider.getSize().getWidth()
            ActionChains(self.driver).drag_and_drop_by_offset(volume_slider, ((width*75)/100), 0).perform()
            time.sleep(5)

        def volume_slider2(self):
            """Test"""
            time.sleep(1)
            self.driver.find_element_by_class_name("jw-icon-playback").click()
            time.sleep(35)
            # control menu
            element = self.driver.find_element_by_class_name("jw-media")
            # hover over control menu
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            # slide slider
            volume_slider = self.driver.find_element_by_class_name("jw-rail")
            width = volume_slider.size['52']
            knob = self.driver.find_element_by_class_name("jw-knob")
            ActionChains(self.driver).click_and_hold(knob).move_by_offset(percent * width / 100, 0).release().perform()
###
        def teardown_class(self):
            self.driver.quit()

##  ADD MID-ROLL ADD TEST
        # scrub to mid-roll ad... verify ad... do clickthrough test... ad wait.
        #https://dev-video.viceops.net/en_us/video/bompton-with-kendrick-lamar/56ba3d2707bdbcd113640fb4
    #####  MOVE ON TO OTHER VIDEO PAGES THEN VICELAND!

