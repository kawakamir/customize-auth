from apps.authentication.models import Crew, SuperVisor
from django.http import (
    HttpResponseForbidden,
)
from django.urls import reverse as url_reverse

def check_staff_type(staff_types=[]):
    def wrapper(f):
        def _(request, *args, **kwargs):
            staff = request.user
            if staff and staff_types and (True not in [staff.__class__.__name__ == staff_type for staff_type in staff_types]):
                return HttpResponseForbidden("不正なアクセスです")
            return f(request, *args, **kwargs)
        return _
    return wrapper