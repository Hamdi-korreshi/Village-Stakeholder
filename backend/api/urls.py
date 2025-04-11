from django.urls import path

# Village management views
from .managing_api import (
    initialize_village,
    personal_village_members,
    list_user_villages,
    get_village_participants,
    add_villager,
    remove_villager
)

# Auth views
from .auth_views import (
    get_csrf_token,
    user_login,
    user_logout,
    delete_profile,
    update_profile,
    get_profile
)

# Registration
from .registration_view import register_user

# General views
from .views import random_string, home

# Password reset
from .pass_reset import ChangePasswordView

urlpatterns = [
    # Root/home view
    path('', home, name='home'),

    # Authentication & user profile
    path('register/', register_user, name='register_user'),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('delete-profile/', delete_profile, name='delete_profile'),
    path('update-profile/', update_profile, name='update_profile'),
    path('get-profile/', get_profile, name='get_profile'),

    # Utility
    path('random_string/', random_string, name='random_string'),

    # Village operations
    path('initialize-village/', initialize_village, name='initialize_village'),
    path('get-village-members/', personal_village_members, name='personal_village_members'),
    path('list-user-villages/', list_user_villages, name='list_user_villages'),
    path('get-village-participants/<int:village_id>/', get_village_participants, name='get_village_participants'),
    path('add-villager/', add_villager, name='add_villager'),
    path('remove-villager/', remove_villager, name='remove_villager'),
]
