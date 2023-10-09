import json
from django.http import JsonResponse
from django.db import models

from .models import User


def all(request):
    users = User.objects.all()
    attrs = {"id", "email", "first_name", "last_name", "password", "role"}
    results: list[dict] = []

    for user in users:
        payload = {attr: getattr(user, attr) for attr in attrs}
        results.append(payload)

    return JsonResponse({"result": results})


# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
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
