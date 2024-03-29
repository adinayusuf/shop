from django.contrib import admin
from django.contrib.sessions.models import Session

# Register your models here.
from webapp.models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name_product']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['name_product', 'category', 'descr_product', 'remainder', 'price']


class OrderAdmin(admin.ModelAdmin):
    fields = ['user', 'phone', 'address']
    list_display = ('pk', 'phone', 'address', 'created_at')
    readonly_fields = ['created_at']
    ordering = ('-created_at',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Session)
