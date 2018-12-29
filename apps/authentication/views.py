from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse as url_reverse
from django.contrib.auth.views import LoginView
from apps.authentication.models import Crew, SuperVisor


# Create your views here.



def index(request):
    return HttpResponse("hello!")
