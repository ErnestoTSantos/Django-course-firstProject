from django.shortcuts import render


# HTTP request
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP response


def about(request):
    return render(request, 'recipes/about.html')


def contact(request):
    return render(request, 'recipes/contact.html')
