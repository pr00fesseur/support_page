import string
import uuid

from django.core.mail import send_mail
from rest_framework import serializers

from .models import ActivationKey, User


def create_activation_key(user) -> str:
    activation_key = str(uuid.uuid4())
    ActivationKey.objects.create(user=user, key=activation_key)
    return activation_key


def send_user_activation_email(email: str, activation_key: str) -> None:
    activation_link = f"https://frontend.com/users/activate/{activation_key}"

    send_mail(
        subject="User activation",
        message=f"Please activate your account: {activation_link}",
        from_email="admin@admin.com",
        recipient_list=[email],
        fail_silently=False,
    )


class ActivationSerializer(serializers.Serializer):
    key = serializers.UUIDField(default=uuid.uuid4)
