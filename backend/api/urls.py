from django.urls import path
from .auth_views import get_csrf_token, user_login, user_logout
from .managing_api import initialize_village, personal_village_members, list_user_villages, get_village_participants, add_villager, remove_villager
from .registration_view import register_user
from .views import random_string
from .pass_reset import ChangePasswordView

urlpatterns = [ path('register/', register_user, name='register_user'),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('random-string/', random_string, name='random_string'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # Villager management
    path('new-village/', initialize_village, name='initialize_village'),
    path('personal-village-members/', personal_village_members, name='personal_village_members'),
    path('list-user-villages/', list_user_villages, name='list_user_villages'),
    path('get-village-participants/<int:village_id>/', get_village_participants, name='get_village_participants'),
    path('add-village/', add_villager, name='add_village'),
    path('remove-village/<int:village_id>/', remove_villager, name='remove_village'),
    ]