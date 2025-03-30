import json, random, sys
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


Sess_user = get_user_model()

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': "CRSF COOKIE SET"})

def user_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)
        identifier = data.get('identifier').strip() 
        password = data.get('password')

        curr_user = authenticate(request, username=identifier, password=password)

        if curr_user is not None:
            login(request, curr_user)
            return JsonResponse({
                "message": "Login successful!",
                "user": {
                    "id": curr_user.id,
                    "username": curr_user.username,
                    "email": curr_user.email
                }
                                 }, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)

    except Exception as e:
        print("Login error:", e, file=sys.stderr)
        return JsonResponse({'error': 'Internal server error', 'details': str(e)}, status=500)
    
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logged out successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=405)

def delete_profile(request):
    print("Resueat:", request.user, file=sys.stderr)
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)
    try:
        curr_user = request.user
        curr_user.delete()
        return JsonResponse({"message": "Profile deleted successfully"}, status=204)
    except Exception as e:
        print("Error happening:", e, file=sys.stderr)
        return JsonResponse({"error": "User not found"}, status=404)