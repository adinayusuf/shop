from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_product', 'descr_product', 'category']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['name_product', 'category', 'descr_product', 'remainder', 'price']


admin.site.register(Product, ProductAdmin)
