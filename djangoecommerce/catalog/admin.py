from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Category, CategoryAdmin)


class PrductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Product, PrductAdmin)
