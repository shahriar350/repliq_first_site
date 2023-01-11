from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from client_app.models import Tenant
from public_app.documentation_serializers import TenantAvailabilityResponseSerializer


# Create your views here.

class TenantAvailabilityCheckView(APIView):
    @extend_schema(
        summary="Search tenant url if available or not.",
        responses={
            200: OpenApiResponse(response=TenantAvailabilityResponseSerializer,
                                 description='It response 200 because tenant is available.'),
            204: OpenApiResponse(response=TenantAvailabilityResponseSerializer,
                                 description='It response 204 because tenant not is available.'),

        }
    )
    def get(self, request, tenant_url):
        tenant_url = tenant_url.replace(' ', '')  # remove all space from string
        if not Tenant.objects.filter(url=tenant_url).exists():
            return Response({
                "available": True
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "available": False
            }, status=status.HTTP_204_NO_CONTENT)
