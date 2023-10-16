from django.contrib import admin
from django.urls import path

# # controller
# def foo(request):
#     data = get_message()  # model
#     response = JsonResponse(data)  # JsonResponse is view
#     # controller
#     return response


urlpatterns = [
    path("admin/", admin.site.urls),
]
