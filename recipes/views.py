from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from . import models


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': models.Recipe.objects.all().order_by('?'),
    })


def category(request, category_id):
    # Exemplo para pegar valor na query
    # recipes = models.Recipe.objects.filter(
    #     category__id=category_id).order_by('?')

    # if not recipes:
    #     raise Http404('Not found \U0001F606')

    recipes = get_list_or_404(models.Recipe.objects.filter(
        # Mandamos a query inteira, para podermos usar o order_by
        category__id=category_id).order_by('?')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category'
    })


def recipe(request, id):
    recipe = models.Recipe.objects.all().filter(id=id).first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'title': f'{recipe.title}'
    })
