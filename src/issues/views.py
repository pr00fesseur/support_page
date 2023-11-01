

from rest_framework import generics
from .models import Issue
from .serializers import IssueSerializer

class IssueDetailView(generics.RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
