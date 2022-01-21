from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
