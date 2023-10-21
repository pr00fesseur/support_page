from dataclasses import dataclass

from rest_framework import serializers


@dataclass
class UserRegistrationSchema:
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50, allow_null=True)
    last_name = serializers.CharField(max_length=50, allow_null=True)

    def validate_email(self, value: str) -> str:
        # TODO: Do something
        return value


payload = {
    "email": "john@email.com",
    "password": "@Dm1n#LKJ",
    "first_name": "John",
    "last_name": "Doe",
}

schema = UserRegistrationSchema(**payload)
# user = User(email=schema.email, password=schema.password...)
serializer = UserRegistrationSerializer(data=payload)

print(serializer.is_valid(raise_exception=True))
