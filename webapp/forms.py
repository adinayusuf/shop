from django import forms
from django.forms import widgets
from webapp.models import CATEGORY


class ProductFrom(forms.Form):
    name_product = forms.CharField(max_length=100, required=False, label='Название')
    descr_product = forms.CharField(max_length=2000, required=True, label='Текст',
                                    widget=widgets.Textarea(attrs={'cols': 20, 'rows': 5}))
    category = forms.CharField(max_length=25, choices=CATEGORY, label='Категория')
    remainder = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, demical_palces=2, label='Цена')
