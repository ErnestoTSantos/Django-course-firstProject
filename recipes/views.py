from django.shortcuts import render


# HTTP request
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP response
