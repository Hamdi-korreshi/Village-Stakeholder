from django.urls import path
from .auth_views import get_csrf_token, user_login, user_logout, delete_profile
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
    ]