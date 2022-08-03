from django.urls import path

from webapp.views.itemcart import CartView, CartAddView, CartDeleteView
from webapp.views.order import OrderListView, OrderCreateView
from webapp.views.product import IndexView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail_view'),
    path('product/add/', ProductCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),

    path('product/<int:pk>/cart/add/', CartAddView.as_view(), name='cart_add'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete'),

    path('order/', OrderListView.as_view(), name='orders'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),

]
