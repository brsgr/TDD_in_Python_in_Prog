from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # Create http request object
        response = home_page(request)  # Pass request to homepage view
        expected_html = render_to_string('home.html') # Load template home.html and convert it to html string
        self.assertEqual(response.content.decode(), expected_html)  # Compare expect html string to content on web page



