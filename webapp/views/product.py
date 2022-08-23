from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models.functions import Lower
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from webapp.models import Product
from webapp.forms import ProductFrom, SearchForm


# Create your views here.
class IndexView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'
    ordering = 'name_product'
    paginate_by = 5
    queryset = Product.objects.filter(remainder__gt=0)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductFrom
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('detail_view', kwargs={"pk": self.object.pk})


class ProductDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'webapp:detail_product'
    model = Product
    template_name = 'product/detail_view.html'
    context_object_name = "product"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp:update_product'
    form_class = ProductFrom
    template_name = 'product/update.html'
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('detail_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp:delete_product'
    template_name = 'product/delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')


class SearchView(ListView):
    model = Product
    form_class = SearchForm
    context_object_name = 'product'
    product = []

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Product.objects.filter(name_product__icontains=form.cleaned_data['name_product'])
        return Product.objects.all()
