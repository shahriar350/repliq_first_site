from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    path('base/products/', views.BaseProductSearchView.as_view(), name='base.products')

]
