import sys
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Village, Villager, UserSupportRelation


# === Retrieve the village owned by the current user and its members ===
def personal_village_members(request):
    owner = request.user
    village = Village.objects.prefetch_related("residents").filter(user=owner).first()

    if not village:
        return JsonResponse({"error": "You do not own a village."}, status=404)

    members = [
        {
            "user_id": resident.id,
            "username": resident.username
        }
        for resident in village.residents.all()
    ]

    return JsonResponse({"members": members}, status=200)


# === List villages the current user is a member of ===
def list_user_villages(request):
    current_user = request.user.id
    query = Village.objects.filter(residents=current_user)

    response_data = [
        {
            "owner": village.user.username,
            "description": village.description
        }
        for village in query
    ]

    return JsonResponse({"villages": response_data})


# === Get members of a specific village (only if user is a resident) ===
def get_village_participants(request, village_id):
    current_user = request.user.id
    village = Village.objects.filter(id=village_id, residents=current_user).first()

    if not village:
        return JsonResponse({"error": "You are not a member of this village."}, status=403)

    members = [
        {
            "user_id": member.id,
            "username": member.username
        }
        for member in village.residents.all()
    ]

    return JsonResponse({
        "village_id": village.id,
        "description": village.description,
        "owner": {
            "owner_id": village.user.id,
            "owner_username": village.user.username
        },
        "members": members
    }, status=200)


# === Initialize a village for the current user ===
@csrf_exempt
def initialize_village(request):
    print("=== [INITIALIZE VILLAGE] ===", file=sys.stderr)
    print("Request method:", request.method, file=sys.stderr)
    print("Request user:", request.user, file=sys.stderr)
    print("Request user ID:", getattr(request.user, 'id', 'None'), file=sys.stderr)
    print("Raw request body:", request.body, file=sys.stderr)

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    user = request.user

    if hasattr(user, 'owned_village'):
        return JsonResponse({"error": "User already owns a village."}, status=400)

    try:
        body_data = json.loads(request.body)
        description = body_data.get("description", "Gamel's Village")
    except (json.JSONDecodeError, TypeError):
        description = "Gamel's Village"

    village = Village.objects.create(user=user, description=description)

    return JsonResponse({
        "message": "Village created successfully.",
        "village_id": village.id
    }, status=201)


# === Add a villager to the user's village ===
@csrf_exempt
def add_villager(request):
    print("\n=== [ADD VILLAGER INITIATED] ===", file=sys.stderr)

    if request.method != "POST":
        print("[ERROR] Invalid request method", file=sys.stderr)
        return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=405)

    try:
        body = json.loads(request.body)
        villager_username = body.get("villager_username")
        support_role = body.get("support_role")
        print("Raw body received:", body, file=sys.stderr)
    except (json.JSONDecodeError, AttributeError) as e:
        print("[ERROR] Failed to parse request body:", str(e), file=sys.stderr)
        return JsonResponse({"error": "Invalid request body."}, status=400)

    if not villager_username or not support_role:
        print("[ERROR] Missing username or support role", file=sys.stderr)
        return JsonResponse({"error": "Username and support role are required."}, status=400)

    current_user = request.user
    print("Logged-in user ID:", getattr(current_user, "id", "No ID"), file=sys.stderr)

    village = Village.objects.filter(user=current_user).first()
    if not village:
        print("[ERROR] No village found for user", file=sys.stderr)
        return JsonResponse({"error": "You do not own a village."}, status=400)

    villager_user = User.objects.filter(username=villager_username).first()
    if not villager_user:
        print("[ERROR] Villager username does not exist:", villager_username, file=sys.stderr)
        return JsonResponse({"error": "The specified user does not exist."}, status=404)

    village.residents.add(villager_user)
    print("Added to village residents", file=sys.stderr)

    relation = UserSupportRelation.objects.create(
        user=current_user,
        supporter=villager_user,
        support_role=support_role
    )
    print("Support relation created (ID:", relation.id, ")", file=sys.stderr)

    villager_instance = Villager.objects.create(
        user=current_user,
        associate=villager_user,
        relation=relation,
        status="pending"
    )
    print("Villager relationship created (ID:", villager_instance.id, ")", file=sys.stderr)

    print("=== [ADD VILLAGER COMPLETE] ===\n", file=sys.stderr)
    return JsonResponse({
        "success": f"User {villager_user.username} added to your village with role {support_role}."
    }, status=200)


# === Remove a villager from the user's village ===
@csrf_exempt
def remove_villager(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=405)

    try:
        body = json.loads(request.body)
        villager_username = body.get("villager_username")
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid request body."}, status=400)

    if not villager_username:
        return JsonResponse({"error": "Villager username is required."}, status=400)

    current_user = request.user
    village = Village.objects.filter(user=current_user).first()

    if not village:
        return JsonResponse({"error": "You do not own a village."}, status=400)

    villager_user = User.objects.filter(username=villager_username).first()
    if not villager_user:
        return JsonResponse({"error": "User not found."}, status=404)

    village.residents.remove(villager_user)

    UserSupportRelation.objects.filter(user=current_user, supporter=villager_user).delete()
    Villager.objects.filter(user=current_user, associate=villager_user).delete()

    return JsonResponse({"success": f"{villager_username} removed from your village."}, status=200)
