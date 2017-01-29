from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)


def category(request, slug):
    current_category = Category.objects.get(slug=slug)
    products_list = Product.objects.filter(category=current_category)

    context = {
        'current_category': current_category,
        'products_list': products_list,
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    context = {
        'product': Product.objects.get(slug=slug)
    }
    return render(request, 'catalog/product.html', context)
