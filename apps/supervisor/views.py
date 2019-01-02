from django.shortcuts import render

from apps.authentication.decorators import check_staff_type
from apps.authentication.models import Crew
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from apps.authentication.forms import CrewRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse as url_reverse
from apps.authentication.strings import randstr
from apps.core.utils import union_dict


# Create your views here.
def __generate_initial_password():
    return randstr(8)


@login_required
@check_staff_type(["SuperVisor", ])
@require_http_methods(["GET", "POST"])
def crews(request):
    crews = Crew.object.all()
    return render(request, "supervisor/crew/crews.html", {
        "crews": crews
    })


@login_required
@check_staff_type(["SuperVisor", ])
@require_http_methods(["GET", "POST"])
def register_crew(request):
    if request.method == "GET":
        return render(request, "supervisor/crew/register_crew.html", {
            "form": CrewRegisterForm()
        })
    form = CrewRegisterForm(request.POST)
    if not form.is_valid():
        return render(request, "supervisor/crew/register_crew.html", {
            "form": form
        }, status=400)
    raw_password = __generate_initial_password()
    crew = Crew.object.create_user(**union_dict(form.cleaned_data, {"password": raw_password}))
    return render(request, "supervisor/crew/register_display.html", {
        "crew": crew,
        "raw_password": raw_password,
    })
