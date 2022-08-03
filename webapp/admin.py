from django.contrib import admin

# Register your models here.
from webapp.models import Product, ItemCart


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name_product']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['name_product', 'category', 'descr_product', 'remainder', 'price']


admin.site.register(Product, ProductAdmin)
admin.site.register(ItemCart)