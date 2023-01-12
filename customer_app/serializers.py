from django.core.validators import MinValueValidator
from django.db.models import Q
from rest_framework import serializers

from customer_app.models import Cart, CartProduct
from product_app.models import Product
from auth_app.models import UserAddress


class CartProductSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField(read_only=True)
    cart_product_id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(Q(active=True) & Q(deleted_at__isnull=True)).all())
    quantity = serializers.IntegerField(validators=[MinValueValidator(1)])
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        customer = validated_data.get('customer', None)
        quantity = validated_data.get('quantity', None)
        product = validated_data.get('product', None)

        cart, created = Cart.objects.get_or_create(customer=customer, active=True, deleted_at__isnull=True)

        validated_data['cart_id'] = cart.id
        cart_product = CartProduct.objects.create(
            cart=cart, product=product, quantity=quantity
        )
        validated_data['cart_product_id'] = cart_product.id
        return validated_data


class CartDestroySerializer(serializers.Serializer):
    removed = serializers.BooleanField(default=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartProductModelSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = (
            'id',
            'cart',
            'product',
            'quantity',
        )


class CartModelSerialiser(serializers.ModelSerializer):
    get_cart_products = CartProductModelSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'customer',
            'slug',
            'get_cart_products',
        )


class CartProductUpdateSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity')
        instance.save()
        return validated_data


class AddressCRUDSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserAddress
        fields = [
            'uuid',
            'house',
            'user',
            'street',
            'post_office',
            'police_station',
            'city',
            'country',
            'state'
        ]
