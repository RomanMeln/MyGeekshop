import json
import random

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page, never_cache

from mainapp.models import ProductCategory, Product
from basketapp.models import Basket
from django.core.cache import cache


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_hot_product():
    products_list = Product.objects.all()

    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    same_products_list = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)

    return same_products_list[:3]


def index(request):

    #products_list = Product.objects.all()[:4]
    products_list = Product.objects.all().select_related()[:4]
    print(products_list.query)

    context = {
        'title': 'Мой магазин',
        'products': products_list,

    }
    return render(request, 'mainapp/index.html', context=context)


#@never_cache
#@cache_page(3600)
def products(request, pk=None, page=1):

    links_menu = get_links_menu()

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products_list, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'links_menu': links_menu,
            'category': category_item,
            'products': products_paginator,

        }
        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()

    context = {
        'links_menu': links_menu,
        'title': 'Товары',
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),

    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')


def product(request, pk):
    links_menu = get_links_menu()
    context = {
        'links_menu': links_menu,
        'product': get_object_or_404(Product, pk=pk),

    }
    return render(request, 'mainapp/product.html', context)

