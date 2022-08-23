from urllib.request import Request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import OrderForm
from webapp.models import ItemCart, Product


class CartView(TemplateView):
    template_name = 'item_cart.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        arr = []
        for item in ItemCart.objects.all():
            arr.append(item.product.price * item.quantity)
        context['items'] = ItemCart.objects.all()
        context['total'] = sum(arr)
        context['form'] = OrderForm()
        return context


class CartAddView(View):
    def post(self, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        product_cart = ItemCart.objects.filter(product=product)
        if product_cart:
            cart = product_cart[0]
            reverse_in_stock = product.remainder - (cart.quantity + 1)
            if reverse_in_stock >= 0:
                cart.quantity += 1
                cart.save()
        else:
            new_cart = ItemCart()
            new_cart.product = product
            new_cart.quantity = 1
            new_cart.save()
        return redirect(reverse('webapp:index'))


class CartDeleteView(TemplateView):
    template_name = 'item_cart.html'

    def post(self, *args, **kwargs):
        product_id = kwargs.get('pk')
        product_cart = ItemCart.objects.filter(product_id=product_id)
        if product_cart:
            product_cart.delete()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:cart_view')