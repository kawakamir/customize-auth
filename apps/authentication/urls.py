from django.contrib.auth import views as auth_views
from django.urls import path
from apps.authentication import views

app_name = "authentication"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="authentication/login.html"
    ), name="login"),
    path("index", views.diverge, name="index"),
]
