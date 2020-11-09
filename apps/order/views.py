from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.order.serializers import (OrderSerializer,
                                    OrderItemSerializer,
                                    OrderItemCreateSerializer)
from apps.order.models import Order, OrderItem

from rest_framework.permissions import IsAuthenticated, IsAdminUser


class OrderView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = OrderItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(user=request.user)
        order_serializer = OrderSerializer(instance.order)
        return Response(order_serializer.data)

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

