from .models import villager, Village ;

# Sends the json of the user's village participants 
def personal_village_members(request, villager_id): 
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
