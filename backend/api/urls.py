from django.urls import path

from api.managing_calendar_api import calendar_invite_create, calendar_invite_response, get_notification

from .managing_api import initialize_village, personal_village_members, list_user_villages, get_village_participants, add_villager, remove_villager
from .auth_views import get_csrf_token, user_login, user_logout, delete_profile, update_profile, get_profile
from .registration_view import register_user
from .views import random_string
from .pass_reset import ChangePasswordView

urlpatterns = [ path('register/', register_user, name='register_user'),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('random-string/', random_string, name='random_string'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('delete-profile/', delete_profile, name='delete_profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('get-profile/', get_profile, name='get_profile'),

    # Villager management
    path('initialize-village/', initialize_village, name='initialize_village'),
    path('get-village-members/', personal_village_members, name='personal_village_members'),
    path('list-user-villages/', list_user_villages, name='list_user_villages'),
    path('get-village-participants/<int:villager_id>/', get_village_participants, name='get_village_participants'), 
    path('add-villager/', add_villager, name='add_villager'),
    path('remove-villager/', remove_villager, name='remove_villager'),
    
    # Calendar Events management
    path('calendar-invite-create/', calendar_invite_create, name='calendar_invite_create'),
    path('calendar-invite-accept/', calendar_invite_response, name='calendar_invite_accept'),
    
    # Notification management
    path('get-notification/', get_notification, name='get_notification'),
    ]