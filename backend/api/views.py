import random
from .models import TestData
from django.shortcuts import render
from django.http import JsonResponse

def random_string(request):
    count = TestData.objects.count()
    if count == 0:
        return JsonResponse({"error": "No data available"}, status=404)
    random_idx = random.randint(0, count-1)
    test_data = TestData.objects.all()[random_idx]
    return JsonResponse({
        "name": test_data.name,
        "value": test_data.value,
        "created_at": test_data.created_at.isoformat()
    })