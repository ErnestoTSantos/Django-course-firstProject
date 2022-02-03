from django.contrib.auth.models import User
from django.test import TestCase
from recipes.models import Category, Recipe

# Quanto mais campos mais testes para realizar as execuções da melhor maneira


class RecipeTestBase(TestCase):

    def setUp(self):
        return super().setUp()

    def make_category(self, name='Meat'):
        return Category.objects.create(name=name)

    def make_author(
            self, first_name='Maria',
            last_name='Silva', username='MariSilva',
            password='123456', email='MariSilva@gmail.com'):
        return User.objects.create_user(first_name=first_name,
                                        last_name=last_name, username=username,
                                        password=password, email=email)

    def make_recipe(
        self,  # noqa: F841
        category_data=None,
        author_data=None,
        title='Strogonoff de carne',
        description='Strogonoff de carne com ketchup e mostarda',
        slug='strogonoff-carne',
        preparation_time=30,
        preparation_time_unit='Minutos',
        servings=2,
        servings_unit='Pessoas',
        preparation_steps='Recipe preparation',
        preparation_steps_is_html=False,
        cover='../static/recipes/img/StrogonoffCarne.jpg',
        is_publisher=True
     ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            cover=cover,
            is_publisher=is_publisher,
        )
