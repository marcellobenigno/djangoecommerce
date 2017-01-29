from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Category, CategoryAdmin)


class PrductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Product, PrductAdmin)
