from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Issue, Message
from .permissions import (IssueParticipant, RoleIsAdmin, RoleIsJunior,
                          RoleIsSenior)
from .serializers import (IssueCreateSerializer, IssueReadonlySerializer,
                          MessageSerializer)


class IssueApiSet(ModelViewSet):
    queryset = Issue.objects.all()

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsSenior | RoleIsJunior | RoleIsAdmin]
        elif self.action == "create":
            permission_classes = [RoleIsJunior]
        elif self.action == "retrieve":
            permission_classes = [IssueParticipant]
        elif self.action == "update":
            permission_classes = [RoleIsSenior | RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return IssueCreateSerializer
        return IssueReadonlySerializer


class MessageCreateAPI(CreateAPIView):
    serializer_class = MessageSerializer
    lookup_field = "issue_id"
    lookup_url_kwarg = "issue_id"


class CreateMessageView(CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IssueParticipant]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, issue=self.get_issue())

    def get_issue(self):
        issue_id = self.kwargs.get("issue_id")
        return Issue.objects.get(pk=issue_id)


class ListMessagesView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IssueParticipant]

    def get_queryset(self):
        issue_id = self.kwargs.get("issue_id")
        return Message.objects.filter(issue=issue_id)
