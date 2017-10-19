#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Front-end tests for Noisey.

Usage::
    py.test -s -v --tb=line test_noisey_ui.py

-s: No capture. Don't suppress output.

-v: Verbose. Gimme all the info.

--tb=line: Shorten the tracebacks should an error occur.
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from ..utils.exceptions import FunctionalError
from ..utils.log import logger
from assertlib import assertEqual, assertAtleast
base_url = "https://staging-noisey.viceops.net"


def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the fullpage
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    log = logger()
    driver.get(base_url)
    element = driver.find_element_by_tag_name("body")
    element.send_keys(Keys.ESCAPE)
    driver.implicitly_wait(1)

def teardown_module(module):
    driver.quit()

class TestLogo(object):
    def test_verify_logo_is_present(self):
        """Let's make sure the logo is present."""
        assert driver.find_element_by_class_name("site-header__logo")

    def test_logo_src(self):
        """Make sure the logo matches what's expected."""
        logo = driver.find_element_by_class_name("site-header__logo")
        with open('utils/logo.txt', 'r') as f:
            assertEqual(f.read(), logo.get_attribute("src"))

    def test_logo_size(self):
        logo = driver.find_element_by_class_name("site-header__logo")
        assertEqual(logo.size["width"], 105)
        assertEqual(logo.size["height"], 25)

    def test_logo_placement(self):
        logo = driver.find_element_by_class_name("site-header__logo")
        assertEqual(logo.get_attribute("y"), "30")

class TestLocaleMenu(object):
    """Test's that elements appear in the locale menu."""
    def setup_class(cls):
        """Open the locale menu before starting the tests."""
        driver.find_element_by_class_name("current-locale").click()

    def teardown_class(cls):
        """Close the locale menu after finishing the tests."""
        driver.find_element_by_class_name("current-locale").click()

    def test_verify_locale_count(self):
        """Verifies there are 14 elements in the dropdown."""
        assert len(driver.find_elements_by_class_name(
            "locale-dropdown__item")) == 14

    def test_verify_locale_names(self):
        """Verifies the names of the locales in the dropdown."""
        locales = driver.find_elements_by_class_name("locale-dropdown__item__label")
        locales_list = [locales[i].text for i in xrange(14)]
        assertEqual(locales_list,
            [
                'UNITED STATES',
                'CANADA',
                'AUSTRIA',
                'GERMANY',
                'DENMARK',
                'AUSTRALIA',
                'UNITED KINGDOM',
                'MEXICO',
                'COLOMBIA',
                'FRANCE',
                'POLAND',
                'NETHERLANDS',
                'ITALY',
                'BRASIL'
            ]
        )

    def test_verify_locale_languages(self):
        """Verifies the names of the languages in the dropdown."""
        languages = driver.find_elements_by_class_name("locale-dropdown__item__language")
        language_list = [languages[i].text for i in xrange(14)]
        assertEqual(language_list,
            [
                'EN',
                'EN',
                'DE',
                'DE',
                'EN',
                'EN',
                'EN',
                'ES',
                'ES',
                'FR',
                'PL',
                'NL',
                'IT',
                'PT'
            ]
        )

    def test_verify_currently_selected_locale(self):
        """Verifies we start with the US as the active locale."""
        selected = driver.find_element_by_class_name("locale-dropdown__item").text
        assertEqual(selected.encode('utf-8'), 'UNITED STATES EN \xe2\x80\xa2')

    def test_verify_opacity_of_menu_when_open(self):
        """Verifies the opaque overlay is present when the dropdown is open."""
        locale_dropdown = driver.find_element_by_class_name("locale-dropdown")
        assertEqual(locale_dropdown.value_of_css_property("opacity"), "1")

class TestMenu(object):
    """Tests for the left menu."""
    def setup_method(method):
        """Ensures that the menu is open before testing."""
        # We need to make sure the menu is open for all tests in this class.
        try:
            driver.find_element_by_class_name("navbar--open")
        except NoSuchElementException:
            driver.find_element_by_class_name("nav-toggle").click()

    def teardown_method(method):
        try:
            driver.find_element_by_class_name("navbar--open")
        except NoSuchElementException:
            driver.find_element_by_class_name("nav-toggle").click()

    def test_verify_menu_button_position(self):
        menu = driver.find_element_by_class_name("nav-toggle")
        assertEqual(menu.location, {"y": 20, "x": 30})

    def test_verify_overlay_is_present(self):
        """
        Let's make sure the semi-opaque overlay appears when the
        container is opened.
        """
        assert driver.find_element_by_class_name("overlay-show")

    def test_verify_x_icon_is_present(self):
        """
        Let's make sure that the x icon is present.
        """
        assert driver.find_element_by_class_name("nav-toggle")

    def test_verify_x_icon_closes_navigation(self):
        """
        Let's make sure that when navigation panel is closed
        when the x icon is clicked.
        """
        driver.find_element_by_class_name("nav-toggle").click()
        try:
            driver.implicitly_wait(1)
            driver.find_element_by_class_name("navbar--open")
        except NoSuchElementException:
            pass
        else:
            raise FunctionalError("Nav didn't close when clicked.")

    def test_verify_search_box_is_present(self):
        """
        Let's make sure the search input field is present.
        """
        assert driver.find_element_by_id("search")

    def test_verify_search_box_placeholder_text(self):
        """
        Let's make sure the placeholder text is present on the
        search input field.
        """
        search_box = driver.find_element_by_id(
            "search").get_attribute("placeholder")
        assert search_box.encode('utf-8') == 'SEARCH\xe2\x80\xa6'

    def test_verify_search_icon_is_present(self):
        """
        Let's make sure the icon is present on the search field.
        """
        assert driver.find_element_by_class_name("search__icon__wrapper")

    def test_verify_follow_noisey_copy(self):
        """Let's make sure the copy is correct."""
        assert driver.find_element_by_class_name(
            "nav__section__title").text == "Follow Noisey"

    def test_verify_more_vice_copy(self):
        """Let's make sure the copy is correct."""
        assert driver.find_elements_by_class_name(
            "nav__section__title")[1].text == "More VICE"

    def test_verify_read_listen_watch_copy(self):
        """Let's make sure the copy is correct."""
        assert driver.find_elements_by_class_name(
            "nav__section__items")[2].text == 'READ\nLISTEN\nWATCH'

    def test_verify_hover_color_of_nav_section_tier_1(self):
        menu_items = ["READ", "LISTEN", "WATCH"]
        for x in menu_items:
            element = driver.find_element_by_link_text(x)
            assertEqual(element.value_of_css_property("color"), 'rgba(0, 0, 0, 1)')
            ActionChains(driver).move_to_element(element).perform()
            assertEqual(element.value_of_css_property("color"), 'rgba(119, 69, 80, 1)')

    def test_verify_hover_color_of_nav_section_tier_2(self):
        menu_items = ["NOISEY NEWS", "INTERVIEWS", "PHOTOS", "RADIO", "NEXT"]
        for x in menu_items:
            element = driver.find_element_by_link_text(x)
            assertEqual(element.value_of_css_property("color"), 'rgba(170, 170, 170, 1)')
            ActionChains(driver).move_to_element(element).perform()
            assertEqual(element.value_of_css_property("color"), 'rgba(119, 69, 80, 1)')

    def test_verify_upsell_ios_link(self):
        assertEqual(
            driver.find_element_by_link_text("VICE on iOS").get_attribute("href"),
            'https://www.vice.com/pages/app'
        )

    def test_verify_upsell_tv_link(self):
        driver.find_element_by_link_text("VICE on iOS").send_keys(Keys.PAGE_DOWN)
        assertEqual(
            driver.find_element_by_link_text("VICE on TV").get_attribute("href"),
            'https://www.viceland.com/'
        )

    def test_verify_upsell_magazine_link(self):
        assertEqual(
            driver.find_element_by_link_text("VICE Magazine").get_attribute("href"),
            'https://www.vice.com/magazine'
        )

    def test_verify_footer_logo_dimensions(self):
        footer_logo = driver.find_element_by_class_name("nav__footer__logo")
        assertEqual(footer_logo.size, {"width": 347, "height": 22})

    def test_verify_dimensions_of_footer_logo(self):
        footer_logo = driver.find_element_by_class_name("nav__footer__logo")
        assertEqual(footer_logo.find_element_by_tag_name(
            "img").size, {'width': 62, 'height': 15}
        )

    def test_verify_position_of_footer_logo(self):
        footer_logo = driver.find_element_by_class_name("nav__footer__logo")
        footer_image = footer_logo.find_element_by_tag_name("img")
        assertEqual(footer_image.get_attribute("x"), "30")
        assertAtleast(int(footer_image.get_attribute("y")), 500)

    def test_verify_footer_link_colors(self):
        links = ["About", "Careers", "Privacy Policy", "Terms of Use"]
        for link in links:
            element = driver.find_element_by_link_text(link)
            assertEqual(element.value_of_css_property("color"), 'rgba(170, 170, 170, 1)')

    def test_verify_footer_links(self):
        assertEqual(driver.find_element_by_link_text("About").get_attribute("href"),
            base_url + "/en_us/page/about")
        assertEqual(driver.find_element_by_link_text("Careers").get_attribute("href"),
            base_url + "/en_us/page/careers")
        assertEqual(driver.find_element_by_link_text("Privacy Policy").get_attribute("href"),
            base_url + "/en_us/page/privacy-policy")
        assertEqual(driver.find_element_by_link_text("Terms of Use").get_attribute("href"),
            base_url + "/en_us/page/terms-of-use")

    def test_footer_copyright_copy(self):
        copyright_text = driver.find_element_by_class_name(
            "nav__footer__copyright").text
        assertEqual(copyright_text.encode("utf-8"),
            "© 2016 VICE Media LLC")

class TestLocaleSwitching(object):
    def setup_class(cls):
        driver.refresh()
        driver.implicitly_wait(10)

    def setup_method(self, method):
        # Close the ad if its shown up.
        element = driver.find_element_by_tag_name("body")
        element.send_keys(Keys.ESCAPE)
        # Open the locale menu.
        driver.find_element_by_class_name("current-locale").click()

    def test_locale_en_us(self):
        # United States is the first item.
        driver.find_elements_by_class_name("locale-dropdown__item")[0].click()
        assert driver.current_url == base_url + "/en_us"

    def test_locale_en_ca(self):
        # Canada is the second item.
        driver.find_elements_by_class_name("locale-dropdown__item__label")[1].click()
        assert driver.current_url == base_url + "/en_ca"

    def test_locale_alps(self):
        # Austria is the third item.
        driver.find_elements_by_class_name("locale-dropdown__item")[2].click()
        assert driver.current_url == base_url + "/alps"

    def test_locale_de(self):
        # Germany is the fourth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[3].click()
        assert driver.current_url == base_url + "/de"

    def test_locale_en_dk(self):
        # Denmark is the fifth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[4].click()
        assert driver.current_url == base_url + "/en_dk"

    def test_locale_en_au(self):
        # Australia is the sixth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[5].click()
        assert driver.current_url == base_url + "/en_au"

    def test_locale_en_uk(self):
        #  United Kingdom is the seventh item.
        driver.find_elements_by_class_name("locale-dropdown__item__label")[6].click()
        assert driver.current_url == base_url + "/en_uk"

    def test_locale_es_mx(self):
        # Mexico is the eighth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[7].click()
        assert driver.current_url == base_url + "/es_mx"

    def test_locale_es_co(self):
        # Columbia is the ninth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[8].click()
        assert driver.current_url == base_url + "/es_co"

    def test_locale_fr(self):
        # France is the tenth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[9].click()
        assert driver.current_url == base_url + "/fr"

    def test_locale_pl(self):
        # Poland is the eleventh item.
        driver.find_elements_by_class_name("locale-dropdown__item")[10].click()
        assert driver.current_url == base_url + "/pl"

    def test_locale_nl(self):
        # Netherlands is the twelvth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[11].click()
        assert driver.current_url == base_url + "/nl"

    def test_locale_it(self):
        # Italy is the thirtheenth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[12].click()
        assert driver.current_url == base_url + "/it"

    def test_locale_pt_br(self):
        # Brazil is the fourteenth item.
        driver.find_elements_by_class_name("locale-dropdown__item")[13].click()
        assert driver.current_url == base_url + "/pt_br"

class TestResponsiveLayout(object):
    """Test suite for responsive design."""
    def setup_class(cls):
        """Check if we're on en_us, if not, then open it since we're not
        guaranteed content on other locales.
        """
        if not driver.current_url == base_url + "/en_us":
            driver.get(base_url + "/en_us")
            element = driver.find_element_by_tag_name("body")
            element.send_keys(Keys.ESCAPE)


    def test_320_by_480(self):
        """Resize window to 320x480 to check various dimensions.

        Note:
          Resizing the viewport to 320x480 should result in:
            - 400x400 lede
            - 340px width lede content title
            - Latest:   12 rows,  1 column
            - Videos:    2 rows,  1 column
            - Features:  3 rows,  1 column
        """
        driver.set_window_size(320, 480)
        # Lede
        assertEqual(driver.find_element_by_class_name("lede__image").size,
                    {'width': 400, 'height': 400})
        assertEqual(driver.find_element_by_class_name(
            "lede__content__title").size['width'],
                    340)
        # Latest - 12 rows, 1 column
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        assertEqual(len(rows), 12)
        for column in rows:
            card = column.find_elements_by_class_name("grid__wrapper__card")
            assertEqual(len(card), 1)
        # Videos - 2 rows, 1 column
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 2)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 1)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

    def test_480_by_800(self):
        """Resize window to 480x800 to check various dimensions.

        Note:
          Resizing the viewport to 480x800 should result in:
            - 480x480 lede
            - 420px width lede content title
            - Latest:   12 rows, 1 column
            - Videos:    2 rows, 1 column
            - Features:  3 rows, 1 column

        """
        driver.set_window_size(480, 800)
        # Lede
        assertEqual(driver.find_element_by_class_name("lede__image").size,
                    {'width': 480, 'height': 480})
        assertEqual(driver.find_element_by_class_name(
            "lede__content__title").size['width'],
                420)
        # Latest - 12 rows, 1 column
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")),
                    12)
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")),
                    1)
        # Videos - 2 rows, 1 column
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 2)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 1)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

    def test_640_by_960(self):
        """Resize window to 640x960 to check various dimensions.

        Note:
          Resizing the viewport to 640x960 should result in:
            - 640x640 lede
            - 580px width lede content title
            - Latest:   12 rows, 1 column
            - Videos:    2 rows, 1 column
            - Features:  3 rows, 1 column
        """
        driver.set_window_size(640, 960)
        # Lede
        assertEqual(driver.find_element_by_class_name("lede__image").size,
                    {'width': 640, 'height': 640})
        assertEqual(driver.find_element_by_class_name("lede__content__title").size['width'],
                    580)
        # Latest - 12 rows, 1 column
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")),
                    12)

        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")),
                    1)
        # Videos - 2 rows, 1 column
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 2)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 1)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

    def test_768_by_1280(self):
        """Resize window to 768x1280 to check various dimensions.

        Note:
          Resizing the viewport to 768x1280 should result in:
            - 338x338 lede
            - 340px width lede content title
            - Latest:   6 rows, 2 columns
            - Videos:    2 rows, 1 column
            - Features:  3 rows, 1 column
        """
        driver.set_window_size(768, 1280)
        # Lede
        assertEqual(driver.find_element_by_class_name("lede__image").size,
                    {'width': 338, 'height': 338})
        assertEqual(driver.find_element_by_class_name(
            "lede__content__title").size['width'], 340)
        # Latest: 6 rows, 2 column
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")), 6)
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")), 2)
        # Videos - 1 rows, 2 columns
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 1)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 2)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

    def test_1024_by_768(self):
        """Resize window to 1024x768 to check various dimensions.

        Note:
          Resizing the viewport to 1024x768 should result in:
            - 564x564 lede
            - 340px width lede content title
            - Latest:   6 rows,  2 columns
            - Videos:    1 row,  2 columns
            - Featues:   3 rows
        """
        driver.set_window_size(1024, 768)
        # Lede
        assertEqual(driver.find_element_by_class_name("lede__image").size,
                    {'width': 564, 'height': 564})
        assertEqual(driver.find_element_by_class_name("lede__content__title").size['width'],
                    340)
        # Latest: 6 rows, 2 column
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")), 6)
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")), 2)
        # Videos - 1 rows, 2 columns
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 1)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 2)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

    def test_1366_by_768(self):
        """Resize window to 1366x768 to check various dimensions.

        Note:
            Resizing the viewport to 1366x768 should result in:
              - 1366x691 superlede
              - 1306px width superlede content title
              - Latest:     3 rows, 4 columns
              - Videos:     1 row, 2 columns
              - Features:   3 rows
        """
        driver.set_window_size(1366, 768)
        # Lede
        assertEqual(driver.find_element_by_class_name("superlede__content").size,
                    {'width': 1366, 'height': 936})
        assertEqual(driver.find_element_by_class_name("superlede__content__title").size['width'],
                    1306)
        # Latest: 3 rows, 4 columns
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")), 3)
        # 4 pieces of content each
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")), 4)
        # Videos - 1 rows, 2 columns
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 1)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 2)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

    def test_1280_by_800(self):
        """Resize window to 1280x800 to check various dimensions.

        Note:
            Resizing the viewport to 1280x800 should result in:
              - 1280x936 superlede
              - 1306px width superlede content title
              - Latest:     3 rows, 4 columns
              - Videos:     1 row, 2 columns
              - Features:   3 rows
        """
        driver.set_window_size(1280, 800)
        # Lede
        assertEqual(driver.find_element_by_class_name("superlede__content").size,
                    {'width': 1280, 'height': 936})
        assertEqual(driver.find_element_by_class_name("superlede__content__title").size['width'], 1220)
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")), 3)
        # Latest: 3 rows, 4 columns
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")), 4)
        # Videos - 1 rows, 2 columns
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 1)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 2)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

    def test_1280_by_1024(self):
        """Resize window to 1280x1024 to check various dimensions.

        Note:
            Resizing the viewport to 1280x1024 should result in:
              - 1280x936 superlede
              - 1220px width superlede content title
              - Latest:     3 rows, 4 columns
              - Videos:     1 row, 2 columns
              - Features:   3 rows
        """
        driver.set_window_size(1280, 1024)
        # Lede
        assertEqual(driver.find_element_by_class_name("superlede__content").size,
                    {'width': 1280, 'height': 936})
        assertEqual(driver.find_element_by_class_name(
            "superlede__content__title").size['width'], 1220)
        # Latest: 3 rows, 4 columns
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")), 3)
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")), 4)
        # Videos - 1 rows, 2 columns
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 1)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 2)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)


    def test_1680_by_1050(self):
        """Resize window to 1680x1050 to check various dimensions.

        Note:
          Resizing the viewport to 1680x1050 should result in:
            - 1440x936 superlede
            - 1380px width superlede content title
            - Latest:     3 rows, 4 columns
            - Videos:     1 row, 2 columns
            - Features:   3 rows
        """
        driver.set_window_size(1680, 1050)
        # Lede
        assertEqual(driver.find_element_by_class_name("superlede__content").size,
                    {'width': 1440, 'height': 936})
        assertEqual(driver.find_element_by_class_name(
            "superlede__content__title").size['width'],1380)
        assertEqual(len(driver.find_elements_by_class_name("grid__wrapper__row")), 3)
        # Latest: 3 rows, 4 columns
        rows = driver.find_elements_by_class_name("grid__wrapper__row")
        for row in rows:
            assertEqual(
                len(row.find_elements_by_class_name("grid__wrapper__card")), 4)
        # Videos - 1 rows, 2 columns
        rows = driver.find_elements_by_class_name("large-grid__wrapper__row")
        assertEqual(len(rows), 1)
        for column in rows:
            card = column.find_elements_by_class_name("large-grid__wrapper__card")
            assertEqual(len(card), 2)
        # Features - 3 rows
        rows = driver.find_elements_by_class_name("blog-grid__wrapper__card")
        assertEqual(len(rows), 3)

class TestNewsletter(object):
    def setup_class(cls):
        x = driver.find_element_by_class_name("homepage__newsletter__text")
        # Hacky way to scroll down to the element.
        x.location_once_scrolled_into_view

    def test_copy(self):
        x = driver.find_element_by_class_name("homepage__newsletter__text")
        p = x.find_element_by_tag_name("p").text
        assertEqual(p, "Like good stuff but hate looking for it?" \
            " Get the best of Noisey delivered to your inbox every day.")
        h2 = x.find_element_by_tag_name("h2").text
        assertEqual(h2, "NOISEY NEWSLETTER")

    def test_placeholder_text(self):
        x = driver.find_element_by_class_name("homepage__newsletter__input")
        i = x.find_element_by_tag_name("input")
        assertEqual(i.get_attribute("placeholder"), "Email@Address.com")

    def test_error_on_blank_email_submission(self):
        x = driver.find_element_by_class_name("homepage__newsletter__input")
        x.find_element_by_tag_name("button").click()
        assertEqual(driver.find_element_by_class_name("newsletter__error").text,
                    "Please enter a valid email address")

    def test_submit_button_image(self):
        button = driver.find_element_by_class_name(
            "homepage__newsletter__submit").value_of_css_property(
            "background-image")
        with open('utils/homepage_submit_button.txt', 'r') as f:
            assertEqual(f.read(), button)

class TestLatest(object):
    def setup_class(cls):
        x = driver.find_element_by_class_name("section-header__wrapper__title")
        x.location_once_scrolled_into_view

    def test_latest_copy(self):
        assertEqual(driver.find_element_by_class_name("section-header__wrapper__title").text,
                    "Latest")

    def test_section_header_background_color(self):
        assertEqual(
            driver.find_element_by_class_name(
                "section-header__wrapper__title").value_of_css_property(
                "background-color"),
            'rgba(119, 69, 80, 1)'
        )

    def test_section_header_wrapper_color(self):
        assertEqual(
            driver.find_element_by_class_name(
                "section-header__wrapper").value_of_css_property(
                "background-color"),
            'rgba(225, 225, 225, 1)'
        )

    def test_section_header_wrapper_height(self):
        assertEqual(
            driver.find_element_by_class_name("section-header__wrapper").size['height'],
            28
        )

class TestVideos(object):
    def setup_class(cls):
        x = driver.find_elements_by_class_name("section-header__wrapper__title")[1]
        x.location_once_scrolled_into_view

    def test_videos_copy(self):
        assertEqual(driver.find_elements_by_class_name("section-header__wrapper__title")[1].text,
                    "Videos")

    def test_section_header_background_color(self):
        assertEqual(
            driver.find_elements_by_class_name(
                "section-header__wrapper__title")[1].value_of_css_property(
                "background-color"),
            'rgba(119, 69, 80, 1)'
        )

    def test_section_header_wrapper_color(self):
        assertEqual(
            driver.find_elements_by_class_name(
                "section-header__wrapper")[1].value_of_css_property(
                "background-color"),
            'rgba(225, 225, 225, 1)'
        )

    def test_section_header_wrapper_height(self):
        assertEqual(
            driver.find_elements_by_class_name("section-header__wrapper")[1].size['height'],
            28
        )

class TestFeatures(object):
    def setup_class(cls):
        x = driver.find_elements_by_class_name("section-header__wrapper__title")[2]
        x.location_once_scrolled_into_view

    def test_features_copy(self):
        assertEqual(driver.find_elements_by_class_name("section-header__wrapper__title")[2].text,
                    "Features")

    def test_section_header_background_color(self):
        assertEqual(
            driver.find_elements_by_class_name(
                "section-header__wrapper__title")[2].value_of_css_property(
                "background-color"),
            'rgba(119, 69, 80, 1)'
        )

    def test_section_header_wrapper_color(self):
        assertEqual(
            driver.find_elements_by_class_name(
                "section-header__wrapper")[2].value_of_css_property(
                "background-color"),
            'rgba(225, 225, 225, 1)'
        )

    def test_section_header_wrapper_height(self):
        assertEqual(
            driver.find_elements_by_class_name("section-header__wrapper")[2].size['height'],
            28
        )