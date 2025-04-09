import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
# Create your models here.

class user(AbstractUser):
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

class calendar_event(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("user", on_delete=models.CASCADE, related_name="events")
    event_name = models.CharField(max_length=255, null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    description = models.TextField(null=True, blank=True)
    reminder = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class session(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField("user", on_delete=models.CASCADE, related_name="user_session")
    expiry = models.DateTimeField(null=False)
    tokens = models.TextField(null=False)

class notification(models.Model):
    notification_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("user", on_delete=models.CASCADE, related_name="user_notifications")
    event = models.ForeignKey(calendar_event, on_delete=models.CASCADE, null=True, blank=True, related_name="event_notifications")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveBigIntegerField(null=True, blank=True)
    message = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
            ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("blocked", "Blocked")
        ], null=False)

class notification_history(models.Model):
    history_id = models.BigAutoField(primary_key=True)
    notification = models.ForeignKey(notification, on_delete=models.CASCADE, related_name="history")
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    message = models.TextField(null=False)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey("user", on_delete=models.SET_NULL, null=True, blank=True)

class villager(models.Model):
    connection_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("user", on_delete=models.CASCADE, related_name="user_villagers")
    associate = models.ForeignKey("user", on_delete=models.CASCADE, related_name="associate_villagers")
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("blocked", "Blocked")
    ], null=False)
    relation = models.ForeignKey('user_support_relation', on_delete=models.CASCADE, related_name='villager_relation')
    approve_by = models.ForeignKey('user', on_delete=models.SET_NULL, null=True,blank=True,related_name='approved_villagers')
    approved_at = models.DateTimeField(null=True, blank=True)

class Village(models.Model):
    owner = models.OneToOneField("user", on_delete=models.CASCADE, related_name='owned_village')
    description = models.TextField(null=True, blank=True)
    residents = models.ManyToManyField("user", related_name='village_members')

    def __str__(self):
        return f"Village owned by {self.owner.username}"

class message(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey("user", on_delete=models.CASCADE, related_name="messages_sent")
    receiver = models.ForeignKey("user", on_delete=models.CASCADE, related_name="messages_received")
    message = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class calendar_invite(models.Model):
    invite_id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(calendar_event, on_delete=models.CASCADE, related_name="invites")
    user = models.ForeignKey("user", on_delete=models.CASCADE, related_name="user_event_invites")
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
    
    user = models.ForeignKey("user", on_delete=models.CASCADE, related_name="user_supporters")
    supporter = models.ForeignKey("user", on_delete=models.CASCADE, related_name="user_supported")
    support_role = models.CharField(max_length=50, choices=support_role_choices, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class TestData(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value
