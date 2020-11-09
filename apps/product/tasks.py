from celery import shared_task

from django.core.mail import send_mail
from time import sleep
from tranzhira.celery import app
from rest_framework.response import Response
from apps.product.models import ProductReview
from apps.member.models import User
from django.shortcuts import render


@shared_task
def send_email_task(user_id):
    user = User.objects.get(id=user_id)
    send_mail(
        subject='Tranzhira',
        message='Coming Soon',
        from_email='makhnoarthur@gmail.com',
        recipient_list=[user.email],
        )



