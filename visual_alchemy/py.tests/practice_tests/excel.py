#"""Load Python Console"""
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("http://google.com")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from assertlib import assertEqual, assertAtleast, assertTrue
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from utils.exceptions import FunctionalError
#from utils.log import logger
import urllib2
import requests
import time
import unittest
import xlrd
import xlwt

#base_url = "http://registration.agios.va-dev.net"

def setup_module(module):
    """The setup_module runs only one time.

    Note:
      Here we open the browser, assign log and driver as
      globals and hit the escape key to close the full page
      ad.
    """
    global driver, log
    driver = webdriver.Chrome()
    #driver.set_window_size(898, 800)
    #driver.get(base_url)
    #driver.implicitly_wait(1)

def teardown_module(module):
    driver.quit()

class TestTopPage(object):
    def test_excel(self):
        """excel"""
        wb2 = xlrd.open_workbook('/Users/dsorace/PycharmProjects/visual_alchemy/py.tests/utils/(Project) Test Cases.xls')
        sheet2 = wb2.sheet_by_name('Estimation of Hours')

        #print "Number of rows in sheet 1:", sheet1.nrows
        #print "List of cell values in 1st row:", sheet1.row_values(0)
        #print "Number of columns in sheet 1:", sheet1.ncols
        #print "List of cell values in 2nd column:", sheet1.col_values(1)

        print('\n' * 2)
        print "Data in 3rd row, 2nd col of sheet1:"
        #print('\n' * 2), sheet2.cell(3, 1).value
        print('\n' * 2)
        print sheet2.cell(3, 0).value, "hours for", sheet2.cell(3,1).value
        print sheet2.cell(4, 0).value, "hours for", sheet2.cell(4, 1).value
        print sheet2.cell(5, 0).value, "hours for", sheet2.cell(5, 1).value




    def teardown_class(self):
        driver.quit()