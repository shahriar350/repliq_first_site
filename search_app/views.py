from django.db.models import Q
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .serializers import MerchantProductSearchSerializer
from pharmaco_backend.permissions import IsMerchant
from product_app.models import BaseProduct


# Create your views here.
class BaseProductSearchView(ListAPIView):
    permission_classes = [IsMerchant]
    serializer_class = MerchantProductSearchSerializer
    queryset = BaseProduct.objects.filter(Q(active=True) & Q(deleted_at__isnull=True)).all()
    filter_backends = [SearchFilter]
    search_fields = ['name']
