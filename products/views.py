from django.shortcuts import render


def index(request):
    """Контроллер главной страницы"""
    return render(request, 'products/index.html')


def products(request):
    """Контроллер страницы продукции"""
    return render(request, 'products/products.html')



