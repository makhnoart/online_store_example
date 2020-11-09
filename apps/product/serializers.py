from rest_framework import serializers
from apps.member.serializers import UserDetailSerializer
from apps.product.models import Product, Manufacturer, SubCategory, Category, ProductReview
from apps.member.models import User


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)


class SubCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    category = CategorySerializer()


class ManufacturerSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)


class ProductSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    manufacturer = ManufacturerSerializers()
    price = serializers.DecimalField(max_digits=20, decimal_places=3)
    sub_category = SubCategorySerializer()


class ProductReviewCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    text = serializers.CharField()
    # product = serializers.IntegerField()

    # class Meta:
    #     read_only_fields = ('id', )

    # def validate_product(self, value):
    #     # product = Product.objects.get(id=value)
    #     product = Product.objects.all().filter(id=value).first()
    #     if product is None:
    #         raise serializers.ValidationError('Product does not exists!')
    #     return product

    def create(self, validated_data):
        pass
        review = ProductReview.objects.create(**validated_data)
        # rewiew = ProductReview.objects.create(user=validated_data['user'],
        #                                       product=)
        return review


class ProductReviewUpdateSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    rating = serializers.IntegerField(min_value=1, max_value=5)
    text = serializers.CharField()

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class ProductReviewListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)
    text = serializers.CharField()
    date_create = serializers.DateTimeField(read_only=True)


# same serializers but using ModelSerializer instead of Serializer

# class ManufacturerModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Manufacturer
#         fields = ('id', 'name')
#
#
# class CategoryModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')
#
#
# class SubCategoryModelSerializer(serializers.ModelSerializer):
#     category = CategoryModelSerializer()
#
#     class Meta:
#         model = SubCategory
#         fields = ('id', 'name', 'category')
#
#
# class ProductModelSerializer(serializers.ModelSerializer):
#     sub_category = SubCategoryModelSerializer()
#
#     class Meta:
#
#         model = Product
#         fields = ('id', 'name', 'manufacturer', 'price', 'sub_category')
