from django.urls import path

from .api import (UserActivateAPI, UserActivationView, UserCreateAPI,
                  UserRetrieveAPI)

urlpatterns = [
    path("create/", UserCreateAPI.as_view(), name="user-create"),
    path("retrieve/", UserRetrieveAPI.as_view(), name="user-retrieve"),
    path("activate-api/", UserActivateApi.as_view(), name="activate-api"),
    path("activate-view/", UserActivationView.as_view(), name="activate-view"),
]
