from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from operator import itemgetter

from apps.product.models import Category, Manufacturer, Product, SubCategory, ProductReview
from apps.product.serializers import (CategorySerializer,
                                      ManufacturerSerializers,
                                      ProductSerializers,
                                      SubCategorySerializer,
                                      ProductReviewCreateSerializer,
                                      ProductReviewUpdateSerializer,
                                      ProductReviewListSerializer)


class ProductsListView(APIView):

    def post(self, request):
        serializer = ProductSerializers()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk, format=None):
        SubCategory.objects.get(pk=pk)
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data)


class ManufacturersDetailView(APIView):

    def post(self, request):
        serializer = ManufacturerSerializers()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        manufacturer = Manufacturer.objects.all()
        serializer = ManufacturerSerializers(manufacturer)
        return Response(serializer.data)


class CategoriesListView(APIView):

    def post(self, request):
        serializer = ProductSerializers()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class SubCategoriesListView(APIView):

    def post(self, request):
        serializer = SubCategorySerializer()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk):
        subcategores = SubCategory.objects.filter(category_id=pk)
        serializer = SubCategorySerializer(subcategores, many=True)
        return Response(serializer.data)


class SubCategoriesDetailView(APIView):

    def get_object(self, pk):
        try:
            return SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        subcategory = self.get_object(pk)
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data)

    def put(self, request, pk):
        subcategory = self.get_object(pk)
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        subcategory = self.get_object(pk)
        serializer = SubCategorySerializer(subcategory, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subcategory = self.get_object(pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsDetailView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subcategory = self.get_object(pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManufacturersListView(APIView):

    def post(self, request):
        serializer = ProductSerializers()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, format=None):
        manufactures = Manufacturer.objects.all()
        serializer = ManufacturerSerializers(manufactures, many=True)
        return Response(serializer.data)


class CategoriesDetailView(APIView):
    # permission_classes = [IsAdminUser, ]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = Category(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#
# class CategoryDetailModelView(APIView):
#     def get(self, request):
#         category = Category.objects.get(id=1)
#         serializer = CategoryModelSerializer(category)
#         return Response(serializer.data)
#
#
# class SubCategoryDetailModelView(APIView):
#     def get(self, request):
#         category = SubCategory.objects.get(id=1)
#         serializer = SubCategoryModelSerializer(category)
#         return Response(serializer.data)
#
#
# class ManufacturerDetailModelView(APIView):
#     def get(self, request):
#         category = Manufacturer.objects.get(id=1)
#         serializer = ManufacturerModelSerializer(category)
#         return Response(serializer.data)
#
#
# class ProductDetailModelView(APIView):
#     def get(self, request):
#         category = Product.objects.get(id=1)
#         serializer = ProductModelSerializer(category)
#         return Response(serializer.data)
#
# from .tasks import send_email_task
# from django.http import HttpResponse
#
#
# class SendEmail(APIView):
#
#     def get(self, request):
#         send_email_task()
#         return HttpResponse('Task is done')


class ProductReviewCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = ProductReviewCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(user=request.user)
        # return Response(serializer.data)
        validated_data = serializer.validated_data
        product = validated_data.pop('product')
        validated_data['product'] = product.id

        return Response('success')


class ProductReviewUpdateView(APIView):
    def get_object(self, pk):
        try:
            return ProductReview.objects.get(pk=pk)
        except ProductReview.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductReviewUpdateSerializer(product, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewListView(APIView):

    def get(self, request, pk):
        product_review = ProductReview.objects.filter(product_id=pk)
        serializer = ProductReviewListSerializer(product_review, many=True)
        return Response(serializer.data)


class ProductReviewListRatingView(APIView):

    def get(self, request, pk):
        ordering = request.query_params.get('ordering', '-rating')
        product_reviews = ProductReview.objects.filter(
            product_id=pk
        ).order_by('-rating')
        if ordering is not None:
            product_reviews = product_reviews.order_by(ordering)
        serializer = ProductReviewListSerializer(product_reviews, many=True)
        return Response(serializer.data)

