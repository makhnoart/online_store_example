from rest_framework import serializers
from apps.member.serializers import UserDetailSerializer
from apps.product.serializers import ProductSerializers
from apps.order.models import OrderItem, Order
from apps.product.models import Product


class OrderItemCreateSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        order = Order.objects.create(customer=validated_data.pop('user'), status=Order.POCKET)
        order_item = OrderItem.objects.create(order=order, **validated_data)
        return order_item


class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = ProductSerializers()
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = UserDetailSerializer()
    items = OrderItemSerializer(many=True)
    status = serializers.IntegerField()

    class Meta:
        fields = ['id', 'customer', 'items', 'status']

