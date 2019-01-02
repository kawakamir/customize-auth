from django.shortcuts import render

from apps.authentication.decorators import check_staff_type
from apps.authentication.models import Crew


# Create your views here.
@check_staff_type(["SuperVisor", ])
def crews(request):
    crews = Crew.object.all()
    return render(request, "supervisor/crew/crews.html", {
        "crews": crews
    })
