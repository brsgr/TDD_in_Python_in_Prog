from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):  # organize test into class based on TestCase subclass

    def setUp(self):  # 'setup' method that opens the browser and creates object for it
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  # 'shutdown' method that closes the browser
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #print(rows, type(rows))
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it(self):  # Methods that begin with 'test' are run by the test runner
        self.browser.get(self.live_server_url)

        # open homepage of the website
        self.assertIn('To-Do', self.browser.title)

        # The title of the webpage should include 'To-Do'
        header_text = self.browser.find_element_by_tag_name('h1').text  # Selenium method for retrieving header name
        self.assertIn('To-Do', header_text)

        # Website prompts user to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User tries to enter 'Buy bananas;
        inputbox.send_keys('Buy bananas')

        # When he hits enter, the page should update and list-
        # "1: Buy bananas" as an item on a to-do list table
        inputbox.send_keys(Keys.ENTER)
        inputbox = self.browser.find_element_by_id('id_new_item')

        inputbox.send_keys('Eat bananas')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy bananas')
        self.check_for_row_in_list_table('2: Eat bananas')
        self.fail('finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')