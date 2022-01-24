from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 5})
        self.assertEqual(url, '/recipes/category/5/')

    def test_recipe_specific_url_is_correct(self):
        url = reverse('recipes:specific', kwargs={'id': 12})
        self.assertEqual(url, '/recipes/12/')
