import json, random, sys
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .models import User
from django.db.models import Q

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': "CRSF COOKIE SET"})

def user_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)
        identifier = data.get('identifier')
        print("email:", identifier, file=sys.stderr)
        password = data.get('password')

        print(f"Login attempt: identifier={identifier}, password={password}", file=sys.stderr)

        user = authenticate(username=identifier, password=password)

        if user is None:
            try:
                user_obj = User.objects.get(Q(email=identifier))
                print(f"User found by email: username={user_obj.username}, email={user_obj.email}", file=sys.stderr)

                user = authenticate(username=user_obj.username, password=password)

                if user is None:
                    print("Password mismatch for username retrieved from email.", file=sys.stderr)
                    return JsonResponse({'error': 'Incorrect password'}, status=401)

            except User.DoesNotExist:
                print(f"Email not found: {identifier}", file=sys.stderr)
                return JsonResponse({'error': 'Invalid credentials (email not found)'}, status=401)
        if user:
            login(request, user)  # clearly call Django's built-in login
            print(f"User logged in: {user.username}", file=sys.stderr)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            print("Authentication failed (invalid password)", file=sys.stderr)
            return JsonResponse({'error': 'Invalid credentials (incorrect password)'}, status=401)

    except json.JSONDecodeError:
        print("Invalid JSON received", file=sys.stderr)
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    except Exception as e:
        print("Unhandled server error:", e, file=sys.stderr)
        return JsonResponse({'error': 'Internal server error', 'details': str(e)}, status=500)
    
def user_signout(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logged out successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=405)
