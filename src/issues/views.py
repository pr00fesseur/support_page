from rest_framework import generics, viewsets

from users.constants import Role

from .models import Issue, Message
from .permissions import IssueParticipant
from .serializers import IssueSerializer, MessageSerializer


class CreateMessageView(generics.CreateAPIView):
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
