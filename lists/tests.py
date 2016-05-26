from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .models import Item
from .views import home_page, view_list

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

        self.assertEqual(Item.objects.count(), 1)  # Checks that the Item table contains 1 objects
        new_item = Item.objects.first()  # sets variable new_item to first (and only) element in table
        self.assertEqual(new_item.text, 'A new list item')  # Checks that new_item is equal to the str from the request

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_home_page_redirects_after_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'  # set request to attempt to post something when called

        response = home_page(request)  # Call request from home_page view

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The First (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, 'The First (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewTest(TestCase):

    def test_uses_list_template(self): # Checks that url at /lists/ uses the list.html template
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        Item.objects.create(text='item1')
        Item.objects.create(text='item2')

        response = self.client.get('/lists/the-only-list-in-the-world/')
        # Uses Django test client instead of calling view directly, tests superlists/url

        self.assertContains(response, 'item1')  # assertContains functions on bytes, so response.decode() is not needed
        self.assertContains(response, 'item2')