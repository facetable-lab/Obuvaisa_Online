from django.shortcuts import render


def index(request):
    """Контроллер главной страницы"""
    context = {
        'title': 'Обувайся онлайн'
    }

    return render(request, 'products/index.html', context)


def products(request):
    """Контроллер страницы продукции"""
    context = {
        'title': 'Каталог :: Обувайся онлайн'
    }

    return render(request, 'products/products.html', context)



