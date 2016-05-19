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
        self.assertTrue(response.content.decode(), expected_html)  # Compare expect html string to content on web page

    def test_home_page_can_save_POST_request(self):
        request = HttpRequest()  # Create http request object
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'  # set request to attempt to post something when called

        response = home_page(request)  # Call request from home_page view
        self.assertIn('A new list item', response.content.decode())  # Check that tested item is in response.content
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertTrue(response.content.decode(), expected_html)
