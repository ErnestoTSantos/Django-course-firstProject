from django.core.exceptions import ValidationError
from parameterized import parameterized

from ..models import Recipe
from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):

    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        return Recipe(
            category=self.make_category('Strogonoff frango'),
            author=self.make_author(username='Joaquin'),
            title='Strogonoff de carne',
            description='Strogonoff de carne com ketchup e mostarda',
            slug='strogonoff-carne',
            preparation_time=30,
            preparation_time_unit='Minutos',
            servings=2,
            servings_unit='Pessoas',
            preparation_steps='Recipe preparation',
            cover='../static/recipes/img/StrogonoffCarne.jpg',
        )

    # Forma de fazer os testes que necessitariam de um for para realiza-los
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('servings_unit', 65)
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 10))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()

        self.assertFalse(recipe.preparation_steps_is_html,
                         msg='Recipe preparation_steps_is_html is not false')

    def test_recipe_is_publisher_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()

        self.assertFalse(recipe.is_publisher,
                         msg='Recipe is publisher is not false')

    def test_recipe_str_representation(self):
        needed = 'Strogonoff frango'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed,
                         # É estremamente correto colocar mensagens para visualizar os erros # noqa: E501
                         msg=f'Recipe string representation must be "{needed}"'
                         f'but "{str(self.recipe)} was received"')
