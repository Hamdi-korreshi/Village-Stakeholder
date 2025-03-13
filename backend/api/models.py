from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_settings = models.JSONField(default=dict, null= True, Blank=True)
    profile_picture = models.URLField(max_length=255, null=True, Blank=True)

class Calendar_event(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    event_name = models.CharField(max_length=255, null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class session(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="session")
    expiry = models.DateTimeField(null=False)
    tokens = models.TextField(null=False)

class notification(models.Model):
    notification_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    event = models.ForeignKey(Calendar_event, on_delete=models.CASCADE, null=True, blank=True, related_name="event_notifications")
    message = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class villager(models.Model):
    connection_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends")
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_of")
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("blocked", "Blocked")
    ], null=False)

class message(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class calendar_invite(models.Model):
    invite_id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(Calendar_event, on_delete=models.CASCADE, related_name="invites")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_invites")
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined")
    ], null=False)

class user_support_relation(models.Model):
    support_role_choices = [
        ("academic", "Academic"),
        ("family", "Family"),
        ("college", "College"),
        ("trade_school", "Trade School"),
        ("workforce_recruiter", "Workforce Recruiter"),
        ("health_advisor", "Health Advisor"),
        ("religion_advisor", "Religion Advisor"),
        ("close_friend", "Close Friend"),
        ("mentor", "Mentor"),

    ]

    relation_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="supporters")  
    supporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="supporting")  
    support_role = models.CharField(max_length=50, choices=support_role_choices, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class TestData(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value