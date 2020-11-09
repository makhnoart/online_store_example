from django.db import models
from apps.member.models import User
from apps.product.models import Product


class Order(models.Model):

    POCKET = 1
    NEW = 2
    IN_PROGRESS = 3
    DONE = 4
    CANCELED = 5

    STATUS_CHOICES = (
        (POCKET, "Pocket"),
        (NEW, "New"),
        (IN_PROGRESS, "In progress"),
        (DONE, "Done"),
        (CANCELED, "Canceled")
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=1
    )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
