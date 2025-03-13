import json, random
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import TestData

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': "CRSF COOKIE SET"})

def signin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        identifier = data.get('identifier')
        password = data.get('pasword')

        user = authenticate(request, username=identifier,password=password)
        if user:
            login(request,user)

            count = TestData.objects.count()

            if count > 0:
                random_index = random.randint(0, count -1)
                test_data = TestData.objects.all()[random_index]
                random_value = test_data.value
            else:
                random_value = None

            return JsonResponse({
                'user_id': user.id,
                'message': "Login success",
                'random_value': random_value
            }, status=201)
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    return JsonResponse({"error": "Invalid request method"}, status=405)

def signout(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logged out successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=405)
