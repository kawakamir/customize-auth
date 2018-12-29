from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse as url_reverse


# Create your views here.

def index(request):
    return HttpResponseRedirect(url_reverse("authentication:login"))
