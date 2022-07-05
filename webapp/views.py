from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product
from webapp.forms import ProductFrom, SearchForm


# Create your views here.
def index_view(request):
    product = Product.objects.order_by('-name_product')
    context = {'products': product}
    return render(request, 'index.html', context)


def list_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponseNotFound('Page not find')
    return render(request, 'detail_view.html', {'product': product})


def create_product(request):
    if request.method == "GET":
        form = ProductFrom()
        return render(request, 'create.html', {'form': form})
    else:
        form = ProductFrom(data=request.POST)
        if form.is_valid():
            name_product = form.cleaned_data.get('name_product')
            descr_product = form.cleaned_data.get('descr_product')
            category = form.cleaned_data.get('category')
            remainder = form.cleaned_data.get('remainder')
            price = form.cleaned_data.get('price')
    new_desc = Product.objects.create(name_product=name_product, descr_product=descr_product, category=category,
                                      remainder=remainder, price=price)
    new_desc.save()
    return redirect('list_view', pk=new_desc.pk)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'product': product})
    else:
        product.delete()
        return redirect('index')


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductFrom(initial={
            'name_product': product.name_product,
            'descr_product': product.descr_product,
            'category': product.category,
            'remainder': product.remainder,
            'price': product.price
        })
        return render(request, 'update.html', {'form': form})
    else:
        form = ProductFrom(data=request.POST)
        if form.is_valid():
            product.name_product = form.cleaned_data.get('name_product')
            product.descr_product = form.cleaned_data.get('descr_product')
            product.category = form.cleaned_data.get('category')
            product.remainder = form.cleaned_data.get('remainder')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('list_view', pk=product.pk)
        return render(request, 'update.html', {'form': form})


def product_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name_product=query)
    return render(request,
                  'search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
