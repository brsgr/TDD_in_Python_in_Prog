from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):  # organize test into class based on TestCase subclass

    def setUp(self):  # 'setup' method that opens the browser and creates object for it
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  # 'shutdown' method that closes the browser
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it(self):  # Methods that begin with 'test' are run by the test runner
        self.browser.get('http://localhost:8000')  # open browser

        self.assertIn('To-Do', self.browser.title)  # assertin tests if 'To-Do' are in browser.title
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')  # runs the test runner command from unit test