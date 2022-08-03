from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from webapp.forms import OrderForm
from webapp.models import OrderProduct, Product, ItemCart


class OrderListView(ListView):
    model = OrderProduct
    context_object_name = 'order_products'
    template_name = 'orders.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-order__created_at")


class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart = ItemCart.objects.all()
            for item in cart:
                product = Product.objects.get(pk=int(item.product_id))
                OrderProduct.objects.create(order=order, product_id=item.product_id, amount=item.quantity)
                product.remainder -= int(item.quantity)
                product.save()
            cart.delete()
        return redirect(reverse('index'))