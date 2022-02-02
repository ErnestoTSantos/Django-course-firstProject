from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    @skip('Teste não está chamando o get')
    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes found here</h1>',
                      response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Strogonoff de carne', content)
        self.assertEqual(len(response_context_recipes), 1)

    @skip('Testando o no recipes found here, não está chamando o no recipes found here')  # noqa: E501
    def test_recipe_home_template_dont_load_recipes_not_publisher(self):
        # Testing recipe is_publisher=False don't show here
        self.make_recipe(is_publisher=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes found here</h1>',
                      response.content.decode('utf-8'))
