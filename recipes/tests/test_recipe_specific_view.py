from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeSpecificViewTest(RecipeTestBase):

    def test_recipe_specific_view_function_is_correct(self):
        view = resolve(reverse('recipes:specific', kwargs={'id': 7}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_specific_view_returns_404_if_no_recipes_found(self):
        self.make_recipe()
        response = self.client.get(
            reverse('recipes:specific', kwargs={'id': 10000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_specific_template_loads_the_correct_recipe(self):
        self.make_recipe()
        response = self.client.get(
            reverse('recipes:specific', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn('Strogonoff de carne', content)
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    def test_recipe_specific_template_dont_load_recipes_not_publisher(self):
        recipe = self.make_recipe(is_publisher=False)
        response = self.client.get(
            reverse('recipes:specific', kwargs={'id': recipe.id}))

        self.assertEqual(response.status_code, 404)


# RED -- GREEN -- REFACTOR
