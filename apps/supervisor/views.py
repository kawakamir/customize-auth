from django.shortcuts import render
from django.http import HttpResponse
from apps.authentication.decorators import check_staff_type

# Create your views here.
@check_staff_type(["SuperVisor",])
def index(request):
    return HttpResponse("supervisorだよ！")


