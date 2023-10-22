import json
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import serializers, permissions

from .models import User


# FBV
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


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]
        # fields = "__all__"

    # def validate_<field>(self, value: Any) -> Any:
    #     return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


# CBF
class UserCreateAPI(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class UserRetrieveAPI(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def get(self, request):
        return super().get(request)