from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from serviceless_distributor import Distributor


Distributor.key = getattr(settings, "SECRET_KEY", {})
Distributor.nodes = getattr(settings, "SERVICELESS_DISTRIBUTOR_NODES", [])
Distributor.headers = getattr(settings, "SERVICELESS_DISTRIBUTOR_HEADERS", {})


@csrf_exempt
@require_http_methods(["POST"])
def event_receiver(request):
    """Tries to run function if data supplied"""

    data = request.POST.get("data")
    if data:
        Distributor._run_function(data)
    return HttpResponse()
