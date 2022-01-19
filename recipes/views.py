from django.http import HttpResponse
from django.shortcuts import render


# HTTP request
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP response


def about(request):
    return HttpResponse('About page')


def contact(request):
    return render(request, 'recipes/contact.html')
