from django.contrib import admin

from .models import (Category, SubCategory, Product, Manufacturer, )

admin.site.register(Category)

admin.site.register(SubCategory)

admin.site.register(Product)

admin.site.register(Manufacturer)
