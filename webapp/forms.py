from django import forms
from django.forms import Textarea
from webapp.models import  Product


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name_product', 'descr_product', 'remainder', 'price']
        widgets = {'descr_product': Textarea(attrs={"rows": 1, "cols": 24})}


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")
