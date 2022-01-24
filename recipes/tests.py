from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


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


class RecipeViewsTest(TestCase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 3}))
        self.assertIs(view.func, views.category)

    def test_recipe_specific_view_function_is_correct(self):
        view = resolve(reverse('recipes:specific', kwargs={'id': 7}))
        self.assertIs(view.func, views.recipe)
