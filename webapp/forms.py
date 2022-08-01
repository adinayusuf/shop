from django import forms
from django.forms import widgets
from webapp.models import CATEGORY


class ProductFrom(forms.Form):
    name_product = forms.CharField(max_length=100, required=True, label='Название')
    descr_product = forms.CharField(max_length=2000, required=False, label='Текст',
                                    widget=widgets.Textarea(attrs={'cols': 20, 'rows': 5}))
    category = forms.ChoiceField(choices=CATEGORY, initial=CATEGORY[0][1], label='Категория')
    remainder = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')


class SearchForm(forms.Form):
    query = forms.CharField(max_length=30, required=False, label="Search")