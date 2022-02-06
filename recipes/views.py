# from django.http import Http404
import os

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination

from . import models

# Forma de chamar o valor a partir do .env, para pegar as constantes
PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):

    recipes = get_list_or_404(models.Recipe.objects.filter(is_publisher=True)
                              .all()
                              .order_by('?'))

    page_object, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_object,
        'pagination_range': pagination_range
    })


def category(request, category_id):

    # Iremos receber uma lista para que possamos pegar o primeiro valor
    recipes = get_list_or_404(models.Recipe.objects.filter(
        # Mandamos a query inteira, para podermos usar o order_by
        category__id=category_id,
        is_publisher=True)
        .order_by('?')
    )

    page_object, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_object,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name} - Category'
    })


def recipe(request, id):

    recipe = get_object_or_404(models.Recipe, id=id, is_publisher=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'title': f'{recipe.title}'
    })


def search(request):

    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()

    recipes = models.Recipe.objects.filter(
        # Coloca um OR para verificar o título e a descrição
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
            # O icontains verifica se tem a palavra que foi enviada em alguma das receitas # noqa: E501
        ),
        is_publisher=True,
    ).order_by('?')

    page_object, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html',
                  {
                      'page_title': f'Search for"{search_term}"',
                      'search_term': search_term,
                      'recipes': page_object,
                      'pagination_range': pagination_range,
                      'additional_url_query': f'&search={search_term}'
                  })
