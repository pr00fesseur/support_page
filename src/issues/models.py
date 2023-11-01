from django.db import models
from shared.django import TimestampMixin
from django.conf import settings

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()


class Issue(TimestampMixin):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=255)
    status = models.CharField(max_length=10)

    junior = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="junior_issues",
    )
    senior = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="senior_issues",
        null=True,
    )

    class Meta:
        db_table = "issues"


class Message(TimestampMixin):
    content = models.CharField(max_length=100)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="messages"
    )
    issue = models.ForeignKey(
        "issues.Issue", on_delete=models.DO_NOTHING, related_name="messages"
    )

    class Meta:
        db_table = "issues_messages"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('junior', 'Junior'), ('senior', 'Senior')], default='junior')
    issues = models.ManyToManyField(Issue, related_name='user_profiles')
