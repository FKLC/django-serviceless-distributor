from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .distributor import Distributor


@csrf_exempt
@require_http_methods(["POST"])
def event_receiver(request):
    """Tries to run function if data supplied"""

    data = request.POST.get("data")
    if data:
        Distributor._run_function(data)
    return HttpResponse()
