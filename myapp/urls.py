from django.contrib import admin
from django.urls import path
from . import views

app_name='myapp'
urlpatterns = [
    path('',views.index),
    path('product/',views.product,name="product"),
    #path('product/',views.Productlistview.as_view(),name="product"),
    # path('product/<int:id>',views.product_detail,name="product_detail"),
    path('product/<int:pk>',views.ProductDetailView.as_view(),name="product_detail"),
    # path('product/add',views.add_product,name="add_product"),
    path('product/add',views.ProductCreateView.as_view(),name="add_product"),
    path('product/update/<int:id>',views.update_product,name="update_product"),
    path('product/delete/<int:id>',views.delete_product,name="delete_product"),
    path('product/mylistings',views.my_listings,name="mylistings"),
] 