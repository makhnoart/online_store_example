from django.urls import path
from apps.product.views import (CategoriesDetailView, ProductsDetailView,
                                SubCategoriesDetailView,
                                ManufacturersDetailView,
                                CategoriesListView, SubCategoriesListView,
                                ManufacturersListView, ProductsListView,
                                ProductReviewCreateView,
                                ProductReviewUpdateView,
                                ProductReviewListView,
                                ProductReviewListRatingView)


urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('categories/<int:pk>/', CategoriesDetailView.as_view()),
    path('categories/<int:pk>/subcategories/', SubCategoriesListView.as_view()),
    path('subcategories/<int:pk>/', SubCategoriesDetailView.as_view()),
    path('subcategories/<int:pk>/products/', ProductsListView.as_view()),
    path('products/detail/<int:pk>/', ProductsDetailView.as_view()),
    path('manufacturers/', ManufacturersListView.as_view()),
    path('manufacturers/<int:pk>/', ManufacturersDetailView.as_view()),
    path('manufacturers/<int:pk>/', ManufacturersDetailView.as_view()),
    path('review/', ProductReviewCreateView.as_view()),
    path('review/<int:pk>/', ProductReviewUpdateView.as_view()),
    path('product/<int:pk>/review/', ProductReviewListView.as_view()),
    path('product/<int:pk>/review/rating/', ProductReviewListRatingView.as_view()),
]
