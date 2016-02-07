from django.db import models

# pillow 3.1.1 fix
# http://stackoverflow.com/questions/34631806/fail-during-installation-of-pillow-python-module-in-linux
# https://pillow.readthedocs.org/en/3.0.0/installation.html#os-x-installation
# https://github.com/Homebrew/homebrew-php/issues/205

YEARS = (
            ('6-12', 'Подарки для ребенка 6-12'),
            ('13-17', 'Подарки для подростка 13-17'),
            ('18-25', 'Подарки для парня и студента 18-25'),
            ('26-39', 'Подарки для мужа и коллеги 26-39'),
            ('40+', 'Подарки для мужчины 40+'),
        )

TYPE = (
            ('solo-electric', 'Наборы электроники для самостоятельной сборки'),
            ('prepared-electric', 'Необычные готовые электронные устройства'),
            ('chemistry', 'Безопасные наборы для химических опытов'),
            ('board-games', 'Только избранные настольные игры и приятные сюрпризы'),
        )


class ProductInfo(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    # max 99 999.99
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    quantity_left = models.PositiveIntegerField(default=0)
    # choose types
    product_type = models.CharField(max_length=20, choices=TYPE)
    years = models.CharField(max_length=20, choices=YEARS)
    # additional info
    all_info = models.ManyToManyField(ProductInfo)
    # few photo
    # http://garmoncheg.blogspot.ru/2011/07/django-creating-multi-upload-form.html
    # or http://django-filer.readthedocs.org/en/latest/index.html
    photo = models.ImageField()
