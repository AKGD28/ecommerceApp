from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('shop_single', views.shop_single_view, name='shop_single'),
    path('shop', views.shop_view, name='shop'),
]
