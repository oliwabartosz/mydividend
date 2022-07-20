from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import unittest
import time

"""
Link: https://www.obeythetestinggoat.com/
"""
MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def wait_for_row_in_list_table(self, row_text):
        """
        This function allows handle AssertionError, and WebDriverException that can 
        sometimes occur.
        """
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
