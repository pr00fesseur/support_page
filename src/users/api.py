import json

from django.db import models
from django.http import JsonResponse

from .models import User


def create(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data: dict = json.loads(request.body)
    user: User = User.objects.create(**data)

    if not user:
        raise Exception("Can not create user")

    # convert to dict
    attrs = {"id", "email", "first_name", "last_name", "password", "role"}
    payload = {attr: getattr(user, attr) for attr in attrs}

    return JsonResponse(payload)
