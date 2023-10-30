from rest_framework import serializers
from rest_framework import serializers

from .constants import Status
from .models import Issue, Message


class IssueReadonlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class IssueCreateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)
    junior = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # junior = serializers.ModelField(...)

    class Meta:
        model = Issue
        fields = ["id", "title", "body", "junior", "status"]

    def validate(self, attrs: dict) -> dict:
        attrs["status"] = Status.OPENED
        return attrs


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["issue", "author", "id"]

    def validate(self, attrs: dict) -> dict:
        # attrs = raw_data => {"content": "blablabla..."}
        request = self.context["request"]
        issue_id: int = request.parser_context["kwargs"]["issue_id"]
        issue: Issue = Issue.objects.get(id=issue_id)

        # Augmentation of attrs dictionary
        attrs["issue"] = issue
        attrs["author"] = request.user

        return attrs
