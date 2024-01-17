from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog-details/',views.blog_details,name='blog-details'),
    path('shop/',views.shop,name='shop'),
    path('blog/',views.blog,name='blog'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('main/',views.main,name='main'),
    path('shop-details/',views.shop_details,name='shop-details'),
    path('shopping-cart/',views.shopping_cart,name='shopping-cart'),
    path('signin/',views.sign_in, name = 'signin'),
    # path('shop/<int:id>', views.filterCat, name='filterCat'),
    # path('shop/<int:id>', views.filterBrand, name='filterBrand')
]