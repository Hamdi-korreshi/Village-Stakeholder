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

from datetime import timezone
import json 
from api.models import calendar_event, calendar_invite, user, notification
from django.http import JsonResponse

# ======== Retrieving Calendar Relevant Data ========

def get_notification(request): # gets the notifications directed to the user
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

def get_calendar_events(request): # gets the events the user is a part of
    """
    Get the calendar events for the user
    """
    user = request.user
    query = calendar_event.objects.filter(user=user).order_by("-start_time")

    if not query.exists():
        return JsonResponse({"error": "You have no calendar events"}, status=404)

    events = [
        {
            "event_id": event.event_id,
            "event_name": event.event_name,
            "start_time": event.start_time.isoformat(),
            "end_time": event.end_time.isoformat(),
            "description": event.description,
            "reminder": event.reminder,
        }
        for event in query
    ]

    return JsonResponse({"events": events}, status=200)


# ======== Managing Calendar Events ========


def create_calendar_event(request): # creates a calendar event
    data = json.loads(request.body)
    event_name = data.get("event_name")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    description = data.get("description")
    reminder = data.get("reminder")
    curr_user = request.user
    if not event_name or not start_time or not end_time:
        return JsonResponse({"error": "Event name, start time, and end time are required"}, status=400)
    if start_time >= end_time:
        return JsonResponse({"error": "Start time must be before end time"}, status=400)
    
    event = calendar_event.objects.create(
        user=curr_user,
        event_name=event_name,
        start_time=start_time,
        end_time=end_time,
        description=description,
        reminder=reminder,
    )
    return JsonResponse({"message": "Event created"}, status=200)

def update_calendar_event(request): # updates a calendar event
    data = json.loads(request.body)
    event_id = data.get("event_id")
    event_name = data.get("event_name")         
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    description = data.get("description")
    reminder = data.get("reminder")
    curr_user = request.user
    if not event_id:
        return JsonResponse({"error": "Event ID is required"}, status=400)
    if not event_name and not start_time and not end_time:
        return JsonResponse({"error": "At least one field to update is required"}, status=400)
    if start_time and end_time and start_time >= end_time:  
        return JsonResponse({"error": "Start time must be before end time"}, status=400)
    try:
        event = calendar_event.objects.get(event_id=event_id, user=curr_user)
    except calendar_event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)
    if event_name:
        event.event_name = event_name
    if start_time:
        event.start_time = start_time
    if end_time:
        event.end_time = end_time
    if description:
        event.description = description
    if reminder:
        event.reminder = reminder
    event.save()
    return JsonResponse({"message": "Event updated"}, status=200)

def delete_calendar_event(request): # deletes a calendar event  
    data = json.loads(request.body)
    event_id = data.get("event_id")
    curr_user = request.user
    if not event_id:
        return JsonResponse({"error": "Event ID is required"}, status=400)
    try:
        event = calendar_event.objects.get(event_id=event_id, user=curr_user)
    except calendar_event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)
    event.delete()
    return JsonResponse({"message": "Event deleted"}, status=200)   

# ======== Managing Calendar Invites ========

def calendar_invite_create(request): #creates a calendar invite
    try:#
        data = json.loads(request.body)
        event_id = data.get("event_id")# soon to be changed to id for the event maybe
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
        try:#
            invitee = user.objects.get(username=username)
            calendar_invite.objects.create(event=event, inviter=request.user, invitee=invitee, status="pending")
            notification.objects.create(
                user=invitee,
                event=event,
                message=f"{request.user.username} invited you to '{event.event_name}'",
            )
            invites_created.append(username)
        except user.DoesNotExist:
            continue  #skip

    return JsonResponse({"message": "Invites sent", "invitees": invites_created}, status=200)
   
def calendar_invite_response(request): # accepts or declines a calendar invite
    try:#
        data = json.loads(request.body)
        invite_id = data.get("invite_id")
        response = data.get("response")
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid request body"}, status=400)

    if response not in ["accepted", "declined"]:
        return JsonResponse({"error": "Invalid response. Must be 'accepted' or 'declined'."}, status=400)

    try:# 
        invite = calendar_invite.objects.get(invite_id=invite_id, invitee=request.user)
        invite.status = response
        invite.responded_at = timezone.now()
        invite.save()
        return JsonResponse({"message": f"Invite {response} successfully."}, status=200)
    except calendar_invite.DoesNotExist:
        return JsonResponse({"error": "Invite not found."}, status=404)

