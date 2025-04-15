from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email address', unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_settings = models.JSONField(default=dict, null=True, blank=True)
    profile_picture = models.URLField(max_length=255, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name="api_users_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="api_users_permissions", blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CalendarEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="events")
    event_name = models.CharField(max_length=255, null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    description = models.TextField(null=True, blank=True)
    reminder = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MemberEventAttendee(models.Model):
    id = models.BigAutoField(primary_key=True)
    member_event = models.ForeignKey("CalendarEvent", on_delete=models.CASCADE, related_name="event_attendees")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="attending_events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('member_event', 'user')

class FeedbackSurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="feedback_surveys")
    rating = models.IntegerField(null=True, blank=True)  # Optional 1–5 score
    comments = models.TextField(null=True, blank=True)   # Optional open feedback
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} for event {self.event.event_name}"

class StudentInterestForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="interest_forms")
    interests = models.TextField(null=True, blank=True)  # Open-ended or comma-separated input
    goals = models.TextField(null=True, blank=True)      # What they want to achieve
    availability = models.CharField(max_length=255, null=True, blank=True)  # e.g., “Weekends”
    preferred_contact = models.CharField(max_length=100, null=True, blank=True)  # e.g., “Email”
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interest Form from {self.user.username}"

class Session(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="user_session")
    expiry = models.DateTimeField(null=False)
    tokens = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_notifications")
    event = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE, null=True, blank=True, related_name="event_notifications")
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Villager(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_villagers")
    associate = models.ForeignKey("User", on_delete=models.CASCADE, related_name="associate_villagers")
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("blocked", "Blocked")
    ], null=False)
    relation = models.ForeignKey('UserSupportRelation', on_delete=models.CASCADE, related_name='villager_relation')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Village(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name='owned_village')
    description = models.TextField(null=True, blank=True)
    residents = models.ManyToManyField("User", related_name='village_members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Village owned by {self.user.username}"

class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey("User", on_delete=models.CASCADE, related_name="messages_sent")
    receiver = models.ForeignKey("User", on_delete=models.CASCADE, related_name="messages_received")
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CalendarInvite(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE, related_name="invites")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_event_invites")
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined")
    ], null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserSupportRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
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

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_supporters")
    supporter = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_supported")
    support_role = models.CharField(max_length=50, choices=support_role_choices, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TestData(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value
