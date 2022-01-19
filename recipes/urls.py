from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('', home),  # home
    path('about/', about),  # /about/
    path('contact/', contact),  # /contact/
]
