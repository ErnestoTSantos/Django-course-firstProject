from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):

    def test_recipe_search_uses_correct_view_function(self):
        view_resolved = resolve(reverse('recipes:search'))
        self.assertIs(view_resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:search') + '?search=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?search=Test'
        response = self.client.get(url)
        self.assertIn('Search for&quot;Test&quot;',
                      response.content.decode('utf-8'))


# RED -- GREEN -- REFACTOR
