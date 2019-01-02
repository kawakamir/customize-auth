from django.urls import path
from apps.supervisor import views

app_name = "supervisor"

urlpatterns = [
    path("crews", views.crews, name="crews"),
    path("register_crew", views.register_crew, name="register_crew"),
]
