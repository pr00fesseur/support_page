from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import IssueApiSet
from .views import CreateMessageView, ListMessagesView

router = DefaultRouter()
router.register("issues", IssueApiSet)

urlpatterns = [
    path(
        "issues/<int:issue_id>/messages/create/",
        CreateMessageView.as_view(),
        name="create-message",
    ),
    path(
        "issues/<int:issue_id>/messages/",
        ListMessagesView.as_view(),
        name="list-messages",
    ),
    path("", include(router.urls)),
]
