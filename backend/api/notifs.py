import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Notification as notification

def get_notifs(request):
    if request.method != "GET":
        return JsonResponse({"error": "Invalid request method."}, status=405)
    
    curr_user = request.user
    if not curr_user.is_authenticated:
        return JsonResponse({"error": "Authentication required."}, status=401)
    
    notifications = notification.objects.filter(user=curr_user).order_by('-timestamp')
    notifications_list = []
    for notif in notifications:
        notifications_list.append({
            "notification_id": notif.notification_id,
            "message": notif.message,
            "status": notif.status,
            "timestamp": notif.timestamp.isoformat(),
        })
    return JsonResponse({'notification': notifications_list}, status=200)
