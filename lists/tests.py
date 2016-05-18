from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # Create httprequest object that django will see when a browser asks for a page
        response = home_page(request) # Pass request to home page view; Httpresponse class whose properties we can call
        self.assertTrue(response.content.startswith(b'<html>'))
        # This checks that the page starts with an html tag. Note that the data type for response.content is raw bytes
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        # This checks for the bytestring for an html title label with the title 'To-Do Lists'
        self.assertTrue(response.content.endswith(b'</html>'))
        # Same as the first check, but searches for the closed tag at the end of the page


