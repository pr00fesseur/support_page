from django.urls import path
from .api import UserCreateAPI, UserRetrieveAPI, UserActivateAPI, UserActivationView


urlpatterns = [
    path("", UserCreateAPI.as_view()),
    path("", UserRetrieveAPI.as_view()),
    path("", UserActivateAPI.as_view()),
    path("", UserActivationView.as_view()),
]
