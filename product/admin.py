from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.modelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class categoryAdmin(admin.modelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, categoryAdmin)
