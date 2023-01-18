from rest_framework import serializers

from product_app.models import BaseProduct


class MerchantProductSearchSerializer(serializers.ModelSerializer):
    manufacturer = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    route_of_administration = serializers.StringRelatedField()
    medicine_physical_state = serializers.StringRelatedField()
    category = serializers.StringRelatedField(many=True)
    active_ingredient = serializers.StringRelatedField(many=True)

    class Meta:
        model = BaseProduct
        fields = (
            'uuid',
            'name',
            'category',
            'active_ingredient',
            'dosage_form',
            'manufacturer',
            'brand',
            'route_of_administration',
            'medicine_physical_state',
        )
