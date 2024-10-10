from django.urls import path

from .views import *

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products'),
    path('product/<slug:slug>/', product_detail_view, name='product_detail'),
    path('search/<slug:slug>/', category_list_view, name='category_list'),
]
