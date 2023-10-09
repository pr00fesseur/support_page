from django.contrib import admin
from django.urls import path
from .exchange_rates import exchange_rates
from users import api


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("exchange-rates/", exchange_rates),
    path("users/all", api.all),
    path("users/create", api.create),
]
