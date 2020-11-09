from django.urls import path
from apps.order.views import OrderView


urlpatterns = [
    path('order/', OrderView.as_view())
]
