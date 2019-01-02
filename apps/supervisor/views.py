from django.shortcuts import render

from apps.authentication.decorators import check_staff_type
from apps.authentication.models import Crew
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from apps.authentication.forms import CreateCrewForm
from django.http import HttpResponseRedirect
from django.urls import reverse as url_reverse


# Create your views here.
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
            "form": CreateCrewForm()
        })
    form = CreateCrewForm(request.POST)
    if not form.is_valid():
        return render(request, "supervisor/crew/register_crew.html", {
            "form": form
        }, status=400)
    Crew.object.create_user(**form.cleaned_data)
    return HttpResponseRedirect(url_reverse("supervisor:crews"))

