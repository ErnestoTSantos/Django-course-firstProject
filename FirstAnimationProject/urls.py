"""FirstAnimationProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import \
    settings  # Forma de importar o settings do projeto da melhor maneira
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # Home do site
]

# Forma de chamar os arquivos no media da raiz
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Forma de chamar os arquivos státicos do programa
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
