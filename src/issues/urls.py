from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import IssueApiSet

router = DefaultRouter()
router.register("", IssueApiSet, basename="issues")
urlpatterns = router.urls
