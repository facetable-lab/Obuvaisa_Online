from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Название', max_length=64, unique=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='Изображение')
    description = models.TextField('Описание', blank=True)
    short_description = models.CharField('Краткое описание', max_length=64, blank=True)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('Остаток на складе', default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} | {self.category}'


class CarouselImages(models.Model):
    image = models.ImageField(upload_to='carousel_images', verbose_name='Изображение')

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
