# tasks.py

from celery import shared_task
from django.core.mail import send_mail
from .services import create_random_email

@shared_task
def send_activation_email(email, activation_link):
    send_mail(
        subject='User activation',
        message=f'Please activate your account: {activation_link}',
        from_email='admin@admin.com',
        recipient_list=[email],
        fail_silently=False,
    )
