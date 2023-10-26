from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from .models import Issue
from .constants import Status


class IssueReadonlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class IssueCreateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)
    junior = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    # junior = serializers.ModelField(...)

    class Meta:
        model = Issue
        fields = ["id", "title", "body", "junior", "status"]

    def validate(self, attrs: dict) -> dict:
        attrs["status"] = Status.OPENED
        return attrs


class IssueApiSet(ModelViewSet):
    queryset = Issue.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return IssueCreateSerializer
        return IssueReadonlySerializer
