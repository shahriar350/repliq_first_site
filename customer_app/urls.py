from django.urls import path, include
from . import views

app_name = 'customer'

urlpatterns = [
    path('cart/product/', views.AddToCartView.as_view(), name='cart.add.product'),
    path('cart/product/<uuid:cart_product_uuid>/', views.RemoveUpdateToCartView.as_view(),
         name='cart.update.remove.product'),
    # path('cart/product/<uuid:cart_product_uuid>/', views.UpdateToCartView.as_view(),
    #      name='cart.update.product'),
    path('cart/', views.CartListView.as_view(),
         name='cart.list'),
    path('cart/current/', views.CartCurrentListView.as_view(),
         name='cart.current.list'),

    # User Address
    path('address/', views.AddressListCreateAPIView.as_view(), name='address.list.create'),
    path('address/<uuid:uuid>/', views.AddressRetieveUpdateDestroyAPIView.as_view(),
         name='address.retrieve.update.destroy')

]
