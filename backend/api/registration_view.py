import json
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse({"error": "Missing username or password"}, status=400)
        
        # django handles password hashing so we don't need to hash it our self
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({"message": "User registered successfully", "user_id": user.id}, staus=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
