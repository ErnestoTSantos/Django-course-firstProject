from django.shortcuts import render


# HTTP request
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Ernesto',
    })
    # return HTTP response
