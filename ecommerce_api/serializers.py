from rest_framework import serializers
from .models import Category, Product, Order, OrderItem,Cart
from drf_writable_nested.serializers import WritableNestedModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    


class ProductSerializer(WritableNestedModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
            queryset=Product.objects.all(),
            write_only=True,
            source="product"
        )
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(WritableNestedModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(WritableNestedModelSerializer):
    items = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'