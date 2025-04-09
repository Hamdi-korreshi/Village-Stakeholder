import json
import sys
from django.http import JsonResponse
from .models import user, Village, villager, user_support_relation, JoinRequest, NotificationHistory
from .models import Notification as notification
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
############### Retrieving Village Data

# Sends the json of the user's village participants 


from django.http import JsonResponse

def personal_village_members(request):
    owner = request.user  # Already the user object
    village = Village.objects.prefetch_related("residents").filter(owner=owner).first()

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



# Sends the json of the villages the user is apart of
def list_user_villages(request):
    current_user = request.user.id  # Get the logged-in user
    
    # Query villages where the user is a resident
    query = Village.objects.filter(residents=current_user)

    response_data = [
        {
            "owner": village.owner.username,
            "description": village.description
        }
        for village in query
    ]
    
    return JsonResponse({"villages": response_data})


# Sends json of the village that a specific user is apart of (first response)
def get_village_participants(request, village_id):
    current_user = request.user.id  # Get the logged-in user

    village = Village.objects.filter(id=village_id, residents=current_user).first()
    
    # If the user is not part of the village, return an error to prevent unauthorized access
    if not village:
        return {"error": "You are not a member of this village."} 

    # Get the members of the village
    members = [
        {
            "user_id": member.id,
            "username": member.username
        }
        for member in village.residents.all()
    ]
    
    response_data = {
        "village_id": village.id,
        "description": village.description,
        "owner": {
            "owner_id": village.owner.id,
            "owner_username": village.owner.username
        },
    }
    
    
    # Add members to the response data
    response_data["members"] = members

    return response_data

def add_villager(request):
    print("\n=== [ADD VILLAGER INITIATED] ===", file=sys.stderr)

    print("Request method:", request.method, file=sys.stderr)
    if request.method != "POST":
        print("[ERROR] Invalid request method", file=sys.stderr)
        return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=405)

    try:
        body = json.loads(request.body)
        villager_username = body.get("villager_username")
        support_role = body.get("support_role")
        print("Raw body received:", body, file=sys.stderr)
        print("Parsed villager_username:", villager_username, file=sys.stderr)
        print("Parsed support_role:", support_role, file=sys.stderr)
    except (json.JSONDecodeError, AttributeError) as e:
        print("[ERROR] Failed to parse request body:", str(e), file=sys.stderr)
        return JsonResponse({"error": "Invalid request body."}, status=400)

    if not villager_username or not support_role:
        print("[ERROR] Missing username or support role", file=sys.stderr)
        return JsonResponse({"error": "Username and support role are required."}, status=400)

    current_user = request.user
    print("Logged-in user object:", current_user, file=sys.stderr)
    print("Logged-in user ID:", current_user.id if hasattr(current_user, "id") else "No ID", file=sys.stderr)

    village = Village.objects.filter(owner=current_user).first()
    if not village:
        print("[ERROR] No village found for user", file=sys.stderr)
        return JsonResponse({"error": "You do not own a village."}, status=400)
    print("Village found:", village.id, file=sys.stderr)

    villager_user = user.objects.filter(username=villager_username).first()
    if not villager_user:
        print("[ERROR] Villager username does not exist:", villager_username, file=sys.stderr)
        return JsonResponse({"error": "The specified user does not exist."}, status=404)
    print("Villager user ID:", villager_user.id, file=sys.stderr)

    # got rid of the old pending to use JoinRequest when handling the guardian flow, sorry rodney

    join_request = JoinRequest.objects.create(
        requester=current_user,
        target=villager_user,
        village=village,
        support_role=support_role
    )
    print("Created JoinRequest record with ID:", join_request.id, file=sys.stderr)

    # todo: add notifcaiton and check for guardian
    guardian = user_support_relation.objects.filter(supporter=villager_username, support_role="Guardian")

    if not guardian.exists():
        join_request.approval_status = "approved"
        join_request.save()
        join_content = ContentType.objects.get_for_model(JoinRequest)
        notif = notification.objects.create(
            user=villager_user,
            content_type=join_content,
            object_id=join_request.id,
            message=f"{current_user.username} inviting you to join {village}",
            status="approve"
        )

        NotificationHistory.objects.create(
            notification=notif,
            old_status="waiting",
            new_status="approved",
            message=notif.message,
            changed_by=current_user
        )
        return JsonResponse({'success': f"{current_user.username} has been invited to join {village}"}, status=200)
    else:
        # need to fix later assume one guardian
        join_content = ContentType.objects.get_for_model(JoinRequest)
        notif = notification.objects.create(
            user=guardian,
            content_type=join_content,
            object_id=join_request.id,
            message=f"{current_user.usernamee} is pending your approval to {village}",
            status="waiting"
        )
        NotificationHistory.objects.create(
            notification=notif,
            old_status="no gaurdian", 
            new_status="waiting",
            message=notif.message,
            changed_by=current_user
        )
        return JsonResponse({'success': f"Guardian notified for {villager_username}"}, status=200)
    
def guardian_approval(request, join_request_id):
    if request.method != "PATCH":
        return JsonResponse({"error": "Invalid request method. Only PATCH is allowed"}, status=405)
    
    try:
        data = json.loads(request.body)
        action = data.get("action")
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid request body."}, status=400)
    
    if action not in ['approve', 'deny']:
        return JsonResponse({"error": "Invalid action. Must be 'approve', or 'deny"}, status=400)
    
    join_request = get_object_or_404(JoinRequest, id=join_request_id)
    old_status = join_request.approval_status

    if action == "approve":
        join_request.approval_status = 'approved'
    elif action == "deny":
        join_request.approval_status = 'blocked'
    
    join_request.save()
    join_content = ContentType.objects.get_for_model(JoinRequest)
    if join_request.approval_status == "approved":
        notif = notification.objects.create(
            user=join_request.target,
            content_type=join_content,
            object_id=join_request.id,
            message=f"Your join request for {join_request.village} has been approved. Please accept the invitation.",
            status="approved"
        )
    else:
        notif = notification.objects.create(
            user=join_request.requester,
            content_type=join_content,
            object_id=join_request.id,
            message=f"Your join request for {join_request.target.username} in {join_request.village} has been rejected.",
            status="rejected"
        )
    
    NotificationHistory.objects.create(
        notification=notif,
        old_status=old_status,
        new_status=join_request.approval_status,
        message=notif.message,
        changed_by=request.user
    )

    return JsonResponse({"success": f"Join request has been {join_request.approval_status}."}, status=200)

def decision_village_invite(request, join_request_id):
    if request.method != "PATCH":
        return JsonResponse({"error": "Invalid request method. Only PATCH is allowed"}, status=405)
    
    try:
        body = json.loads(request.body)
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid request body."}, status=400)
    
    join_request = get_object_or_404(JoinRequest, id=join_request_id)

    if join_request.approval_status != "approved":
        return JsonResponse({"error": "Join request has not been approved yet."}, status=400)
    
    village = join_request.village
    village.residents.add(join_request.target)
    
    join_content = ContentType.objects.get_for_model(JoinRequest)
    notif = notification.objects.create(
        user=join_request.target,
        content_type=join_content,
        object_id=join_request.id,
        message=f"You have accepted the invitation to join {village}.",
        status="accepted"
    )

    NotificationHistory.objects.create(
        notification=notif,
        old_status="approved",
        new_status="accepted",
        message=notif.message,
        changed_by=join_request.target  # The invitee is accepting.
    )
    return JsonResponse({"success": f"You have accepted the invitation to join {village}."}, status=200)

    # # Add to village
    # village.residents.add(villager_user)
    # print("Added to village residents", file=sys.stderr)

    # # Create support relation
    # relation = user_support_relation.objects.create(
    #     user=current_user,
    #     supporter=villager_user,
    #     support_role=support_role
    # )
    # print("Support relation created (ID:", relation.id, ")", file=sys.stderr)

    # # Create villager instance
    # villager_instance = villager.objects.create(
    #     user=current_user,
    #     associate=villager_user,
    #     relation=relation,
    #     status="pending"
    # )
    # print("Villager relationship created (ID:", villager_instance.connection_id, ")", file=sys.stderr)

    # print("=== [ADD VILLAGER COMPLETE] ===\n", file=sys.stderr)
    # return JsonResponse({
    #     "success": f"User {villager_user.username} added to your village with role {support_role}."
    # }, status=200)


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
    village = Village.objects.filter(owner=current_user).first()

    if not village:
        return JsonResponse({"error": "You do not own a village."}, status=400)

    villager_user = user.objects.filter(username=villager_username).first()
    if not villager_user:
        return JsonResponse({"error": "User not found."}, status=404)

    village.residents.remove(villager_user)

    # Clean up support relation
    user_support_relation.objects.filter(user=current_user, supporter=villager_user).delete()
    villager.objects.filter(user=current_user, associate=villager_user).delete()

    return JsonResponse({"success": f"{villager_username} removed from your village."}, status=200)

def initialize_village(request):
    print("=== [INITIALIZE VILLAGE] ===", file=sys.stderr)
    print("Request method:", request.method, file=sys.stderr)
    print("Request user:", request.user, file=sys.stderr)
    print("Request user ID:", getattr(request.user, 'id', 'None'), file=sys.stderr)
    print("Raw request body:", request.body, file=sys.stderr)

    if request.method != "POST":
        print("Invalid request method", file=sys.stderr)
        return JsonResponse({"error": "Invalid request method"}, status=405)

    user = request.user

    # Check if the user already owns a village
    if hasattr(user, 'owned_village'):
        print(f"User '{user.username}' already owns a village.", file=sys.stderr)
        return JsonResponse({"error": "User already owns a village."}, status=400)

    # Parse description from request body if available
    try:
        body_data = json.loads(request.body)
        description = body_data.get("description", "Gamel's Village")
    except (json.JSONDecodeError, TypeError):
        description = "Gamel's Village"
        print("Couldn't parse request body. Using default description.", file=sys.stderr)

    # Create the village
    village = Village.objects.create(owner=user, description=description)

    print(f"Village created for user '{user.username}' (Village ID: {village.id})", file=sys.stderr)

    return JsonResponse({
        "message": "Village created successfully.",
        "village_id": village.id
    }, status=201)


