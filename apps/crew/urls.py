from django.urls import path
from apps.crew import views

app_name = "crew"

urlpatterns = [
    path("index", views.index, name="index"),
]
