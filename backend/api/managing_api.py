from .models import villager, Village ;
############### Retrieving Village Data

# Sends the json of the user's village participants 
def personal_village_members(request): 
    owner_id= request.user.id # Gets the logged-in user's ID
    
    query = villager.objects.filter(owner_id = owner_id).select_related("user")
    
    response_data = [
    {
        "user_id": member.user.id,

    }
    for member in query
    ]
    
    return response_data


# Sends the json of the villages the user is apart of
def list_user_villages(request):
    current_user = request.user  # Get the logged-in user

    # Query villages where the user is a resident
    query = Village.objects.filter(residents=current_user)

    response_data = [
        {
            "village_id": village.id,
            "owner": village.owner.username,
            "description": village.description
        }
        for village in query
    ]
    
    return response_data


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
def add_villager(request):
    response = ""
    if request.method == "POST":
        current_user = request.user  # Get the logged-in user
        village_id = request.POST.get("village_id")  
        villager_id = request.POST.get("villager_id")  

        # Check if the village exists and the current user is the owner
        village = Village.objects.filter(id=village_id, owner=current_user).first()
        if not village:
            return {"error": "You do not own this village or it does not exist."}

        # Check if the villager exists
        villager_to_add = villager.objects.filter(id=villager_id).first()
        if not villager_to_add:
            return {"error": "The villager does not exist."}

        # Add the villager to the village
        village.residents.add(villager_to_add.user)
        village.save()

        response = {"success": f"Villager {villager_to_add.user.username} has been added to the village."}
    else:
        response = {"error": "Invalid request method. Only POST is allowed."}

    return response

    
# Removes a specific villager from the current user's village
def remove_villager(request):
        response = ""
        if request.method == "POST":
            current_user = request.user  
            village_id = request.POST.get("village_id")  
            villager_id = request.POST.get("villager_id")  

            # Check if the village exists and the current user is the owner
            village = Village.objects.filter(id=village_id, owner=current_user).first()
            if not village:
                return {"error": "You do not own this village or it does not exist."}

            # Check if the villager exists in the village
            villager_to_remove = villager.objects.filter(id=villager_id).first()
            if not villager_to_remove or villager_to_remove.user not in village.residents.all():
                return {"error": "The villager is not part of this village."}

            # Remove the villager from the village and save the changes
            village.residents.remove(villager_to_remove.user)
            village.save()

            response = {"success": f"Villager {villager_to_remove.user.username} has been removed from the village."}
        else:
            response = {"error": "Invalid request method. Only POST is allowed."}

        return response
    