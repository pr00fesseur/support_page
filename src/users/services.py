import string
import uuid

from django.core.mail import send_mail
from rest_framework import serializers

from .models import ActivationKey, User
from .tasks import send_user_activation_email

def create_activation_key(user) -> str:
    activation_key = str(uuid.uuid4())
    ActivationKey.objects.create(user=user, key=activation_key)
    return activation_key


def send_user_activation_email(email: str, activation_key: str) -> None:
    activation_link = f"https://frontend.com/users/activate/{activation_key}"

for _ in range(1000):
    send_user_activation_email.apply_async(
        args=[create_random_email(), activation_link],
        countdown=10,  # can be different
    )


class ActivationSerializer(serializers.Serializer):
    key = serializers.UUIDField(default=uuid.uuid4)
