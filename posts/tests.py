from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.


class PostTests(TestCase):  # subclass of TestCase to test with
    @classmethod
    def setUpTestData(cls):  # develop initial data
        cls.post = Post.objects.create(text="This is a test!")

    # Check that model contains data developed above
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    # Note: only functions that begin with the word 'test' will be run

    # Check that URL exists at "/" and returns 200 status code
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    """
    # Check that URL is available by name of "home"
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # Check that correct template is used called "home.html"
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    # Check that homepage content matches what we expect in database
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
    """

    # Combining above 3 tests
    def test_homepage(self):
        response = self.client.get(reverse("home"))

        # Check that URL is available by name of "home"
        self.assertEqual(response.status_code, 200)

        # Check that correct template is used called "home.html"
        self.assertTemplateUsed(response, "home.html")

        # Check that homepage content matches what we expect in database
        self.assertContains(response, "This is a test!")
