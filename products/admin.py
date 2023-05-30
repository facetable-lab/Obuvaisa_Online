from django.contrib import admin

from .models import ProductCategory, Product, CarouselImages

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(CarouselImages)
