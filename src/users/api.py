import json
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import serializers, permissions, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User, ActivationKey
from .services import send_user_activation_email
from .services import ActivationSerializer

from rest_framework import status
from rest_framework.views import APIView


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

    def validate(self, attrs: dict) -> dict:
        attrs["password"] = make_password(attrs["password"])

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


# CBF
class UserCreateAPI(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        send_user_activation_email(email=serializer.data["email"])

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserRetrieveAPI(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def get(self, request):
        return super().get(request)


class UserActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid():
            activation_key = serializer.validated_data["key"]
            try:
                activation_obj = ActivationKey.objects.get(key=activation_key)
                user = activation_obj.user
                user.is_active = True
                user.save()
                activation_obj.delete()
                return Response({"message": "Your email is successfully activated."}, status=status.HTTP_200_OK)
            except ActivationKey.DoesNotExist:
                return Response({"message": "Invalid activation key."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
