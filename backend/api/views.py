from django.http import JsonResponse
import random
from .models import TestData
from django_ratelimit.decorators import ratelimit

# Home view for the root URL
def home(request):
    return JsonResponse({
        "message": "Welcome to the API. Please go to /village/v1/random_string/ for random string."
    })

# Random string view with rate limiting
@ratelimit(key='ip', rate='5/m', method='GET', block=False)
def random_string(request):
    if getattr(request, 'limited', False):
        return JsonResponse({"error": "Rate limit exceeded"}, status=429)

    count = TestData.objects.count()
    if count == 0:
        return JsonResponse({"error": "No data available"}, status=404)

    random_idx = random.randint(0, count - 1)
    test_data = TestData.objects.all()[random_idx]

    return JsonResponse({
        "name": test_data.name,
        "value": test_data.value,
        "created_at": test_data.created_at.isoformat()
    })
