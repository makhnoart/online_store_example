"""tranzhira URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.product.urls')),
    path('api/v1/', include('apps.member.urls')),
    path('api/v1/', include('apps.order.urls')),

    # path('category_model/', CategoryDetailModelView.as_view()),
    # path('subcategory_model/', SubCategoryDetailModelView.as_view()),
    # path('product_model/', ProductDetailModelView.as_view()),
    # path('manufacturer_model/', ManufacturerDetailModelView.as_view())
]
