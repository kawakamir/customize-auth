from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse as url_reverse
from django.contrib.auth.views import LoginView
from apps.authentication.models import Crew, SuperVisor
from django.urls import reverse as url_reverse


# Create your views here.

def diverge(request):
    if isinstance(request.user, SuperVisor):
        return HttpResponseRedirect(url_reverse("supervisor:index"))

    if isinstance(request.user, Crew):
        return HttpResponseRedirect(url_reverse("crew:index"))
    return HttpResponse("無所属！")


def index(request):
    return HttpResponse("hello!")
