from django.urls import path
from apps.supervisor import views

app_name = "supervisor"

urlpatterns = [
    path("index", views.index, name="index"),
]
