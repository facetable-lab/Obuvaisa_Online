# Generated by Django 4.2.1 on 2023-05-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_carouselimages_options_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimages',
            name='image',
            field=models.ImageField(upload_to='carousel_images', verbose_name='Изображение'),
        ),
    ]
