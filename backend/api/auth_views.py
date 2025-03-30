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

def update_profile(request):
    try:
        data = json.loads(request.body)
        
        user = request.user
        
        if 'email' not in data or 'username' not in data or 'full_name' not in data:
            return JsonResponse({"error": "Missing required fields"}, status=400)
        
        if "full_name" in data:
            user.full_name = data["full_name"]
        if "email" in data:
            user.email = data["email"]
        if "username" in data:
            user.username = data["username"]
        if "profile_picture" in data:
            user.profile_picture = data["profile_picture"]
        # for future sprint TODO
        # if "profile_settings" in data:
        #     user.profile_settings = data["profile_settings"]
        if "bio" in data:
            user.bio = data["bio"]

        user.save()

        return JsonResponse({"message": "Profile updated successfully"}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@login_required
@require_http_methods(["GET"])
def get_profile(request):
    print("APIT HIT", file=sys.stderr)
    try:
        user = request.user
        data = {
            "username": user.username,
            "email": user.email,
            "full_name": getattr(user, "full_name", ""),
            "bio": getattr(user, "bio", ""),             
            "profile_picture": getattr(user, "profile_picture", ""),
        }
        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
