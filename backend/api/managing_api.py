from .models import villager, Village,user ;
from django.http import JsonResponse;

############### Retrieving Village Data

# Sends the json of the user's village participants 


def personal_village_members(request):
    owner_id = request.user.id  # Gets the logged-in user's ID

    # Get the village owned by the user
    query = Village.objects.filter(owner=owner_id).prefetch_related("residents")

    response_data = [
        {"user_id": resident.id, "username": resident.username}  
        for village in query
        for resident in village.residents.all()  # Correctly access related residents
    ]

    return JsonResponse(
        {
        "members": response_data
        }
    )


# Sends the json of the villages the user is apart of
def list_user_villages(request):
    current_user = request.user  # Get the logged-in user
    
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
    current_user = request.user  # Get the logged-in user

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


############### Managing Villagers

# Adds/Invites a user to current user's village
def add_villager(request, incoming_user):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=405)

    current_user = request.user  # Get the logged-in user
    village = Village.objects.filter(owner=current_user).first()

    if not village:
        return JsonResponse({"error": "You do not own a village."}, status=400)

    villager_to_add = user.objects.filter(id=incoming_user).first()
    if not villager_to_add:
        return JsonResponse({"error": "The specified user does not exist."}, status=404)

    # Add the villager to the village
    village.residents.add(villager_to_add)
    village.save()

    return JsonResponse({"success": f"User {villager_to_add.username} has been added to the village."}, status=200)

    
# Removes a specific villager from the current user's village
def remove_villager(request):
        if request.method != "POST":
            return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=405)

        current_user = request.user  # Get the logged-in user
        village_id = request.POST.get("village_id")  # Get the village ID from the request
        villager_id = request.POST.get("villager_id")  # Get the villager ID from the request

        # Check if the village exists and the current user is the owner
        village = Village.objects.filter(id=village_id, owner=current_user).first()
        if not village:
            return JsonResponse({"error": "You do not own this village or it does not exist."}, status=400)

        # Check if the villager exists in the village
        villager_to_remove = user.objects.filter(id=villager_id).first()
        if not villager_to_remove or villager_to_remove not in village.residents.all():
            return JsonResponse({"error": "The villager is not part of this village."}, status=404)

        # Remove the villager from the village and save the changes
        village.residents.remove(villager_to_remove)
        village.save()

        return JsonResponse({"success": f"Villager {villager_to_remove.username} has been removed from the village."}, status=200)
    
    
    
def initialize_village(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)
    user = request.user
    # Ensure user doesn't already own a village (OneToOneField constraint)
    if hasattr(user, 'owned_village'):
        return JsonResponse({"error": "User already owns a village."}, status=400)

    # Create the village
    village = Village.objects.create(owner=user, description="Gamel's Village")

    return JsonResponse({"message": "Village created successfully.", "village_id": village.id}, status=201)
    
    