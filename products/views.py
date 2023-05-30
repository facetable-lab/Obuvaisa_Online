from django.shortcuts import render

from .models import ProductCategory, Product, CarouselImages


def index(request):
    """Контроллер главной страницы"""
    context = {
        'title': 'Обувайся онлайн'
    }

    return render(request, 'products/index.html', context)


def products(request):
    """Контроллер страницы продукции"""
    context = {
        'title': 'Каталог :: Обувайся онлайн',
        'category_qs': ProductCategory.objects.all(),
        'product_qs': Product.objects.all(),
        'carousel_images': [CarouselImages.objects.get(pk=1), CarouselImages.objects.get(pk=2),
                            CarouselImages.objects.get(pk=3)]
    }

    return render(request, 'products/products.html', context)
