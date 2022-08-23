from django import forms
from django.forms import Textarea
from webapp.models import Product, Order


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name_product', 'descr_product', 'remainder', 'price']
        widgets = {'descr_product': Textarea(attrs={"rows": 1, "cols": 24})}
    def changed_data(self):
        remainder = self.cleaned_data
        if remainder >= 0:
            raise ValueError('Остаток не может быть отрицательным ')
        return remainder

class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', "phone", "address")
