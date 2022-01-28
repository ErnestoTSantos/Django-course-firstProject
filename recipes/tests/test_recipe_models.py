from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):

    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

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
