import json, sys
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        print(f"Register attempt: email={email}, password={password}, username={username}", file=sys.stderr)

        if not username or not password:
            return JsonResponse({"error": "Missing username or password"}, status=400)
        
        # django handles password hashing so we don't need to hash it our self
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            if not user:
                print('user is not created')
            return JsonResponse({"message": "User registered successfully", "user_id": user.id}, status=201)
        except Exception as e:
            print('Registration Exception:', e, file=sys.stderr)
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
