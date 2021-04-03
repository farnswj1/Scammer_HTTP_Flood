from django.urls import path
from . import views

app_name = "data"

urlpatterns = [
    path("", views.ListCreateData.as_view())
]