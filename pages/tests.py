from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
#   target page what`s need to test ^
        self.assertEqual(response.status_code, 200)
#            what answer we wait from that page ^

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
#          target page, not url but page name ^
        self.assertEqual(response.status_code, 200)
#            what answer we wait from that page ^

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
#                           target page name ^
        self.assertTemplateUsed(response, "home.html")
# True if this template was used in rendering page ^

    def test_template_content(self):
        response = self.client.get(reverse("home"))
#                           target page name ^
        self.assertContains(response, "<h1>the new \"Hello World!\" update</h1>")
#    whats content must be in this page ^

class AboutPageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")