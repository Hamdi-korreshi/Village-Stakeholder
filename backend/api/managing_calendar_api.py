"""
Calendar API

CALENDAR HANDSHAKE FLOW:

1. A user creates an event.
   -> The backend stores the event in the `calendar_event` model.

2. The user selects one or more usernames to invite to the event.
   -> A `calendar_invite` is created for each invitee to track their RSVP status.
   -> A `notification` is created for each invitee to display the invite in the frontend menu.

3. The frontend retrieves notifications from the `/get_notification/` endpoint.
   -> All notifications (including event invites) are listed in a single UI menu.
   -> Each notification can include information such as the message, event reference, status, and type.

4. The user can respond to an event invite directly from the notification menu.
   -> The frontend sends a POST request to `/respond_to_invite_notification/` with the invite response.
   -> The backend updates the `calendar_invite` and the related `notification` to reflect the response.

PLANNED INTERACTIONS / EXTENSIONS:

- Allow users to update or delete events they created.
  -> Event updates will include `event_id` and any modified fields (name, time, etc.)
  -> Event deletions will include only the `event_id`
  -> On edit/delete, notifications should be sent to all invitees indicating the event was changed or canceled.

- Add support for reminder notifications before an event starts (e.g., 30 minutes prior).
- Allow users to mark notifications as "read" or "cleared" from the frontend.
- Display accepted and declined events differently on the user's calendar.
- Optionally paginate or filter the notification list by type (e.g., only show event-related notifications).
"""

import json 
from api.models import calendar_event, calendar_invite, user, notification
from django.http import JsonResponse


def get_notification(request):
    """
    Get the notifications for the user
    """
    user = request.user
    query = notification.objects.filter(user=user).order_by("-timestamp")

    if not query.exists():
        return JsonResponse({"error": "You have no notifications"}, status=404)

    notifications = [
        {
            "id": note.notification_id,
            "type": getattr(note, "type", "general"),  # Optional if we add a 'type'
            "message": note.message,
            "timestamp": note.timestamp.isoformat(),
        }
        for note in query
    ]

    return JsonResponse({"notifications": notifications}, status=200)

    

def calendar_invite_create(request):
    try:
        data = json.loads(request.body)
        event_id = data.get("event_id")
        invitees = data.get("invitees", [])
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid request data"}, status=400)

    if not event_id or not invitees:
        return JsonResponse({"error": "Event ID and invitees are required"}, status=400)

    try:
        event = calendar_event.objects.get(event_id=event_id)
    except calendar_event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)

    invites_created = []
    for username in invitees:
        try:
            invitee = user.objects.get(username=username)
            calendar_invite.objects.create(event=event, inviter=request.user, invitee=invitee, status="pending")
            # Optional: auto-create notification
            notification.objects.create(
                user=invitee,
                event=event,
                message=f"{request.user.username} invited you to '{event.event_name}'",
            )
            invites_created.append(username)
        except user.DoesNotExist:
            continue  # Skip invalid users

    return JsonResponse({"message": "Invites sent", "invitees": invites_created}, status=200)
   
    
def calendar_invite_response(request):
    try:
        data = json.loads(request.body)
        invite_id = data.get("invite_id")
        response = data.get("response")
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid request body"}, status=400)

    if response not in ["accepted", "declined"]:
        return JsonResponse({"error": "Invalid response. Must be 'accepted' or 'declined'."}, status=400)

    try:
        invite = calendar_invite.objects.get(invite_id=invite_id, invitee=request.user)
        invite.status = response
        invite.responded_at = timezone.now()
        invite.save()
        return JsonResponse({"message": f"Invite {response} successfully."}, status=200)
    except calendar_invite.DoesNotExist:
        return JsonResponse({"error": "Invite not found."}, status=404)

