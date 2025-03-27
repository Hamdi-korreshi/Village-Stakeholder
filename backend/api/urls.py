from django.urls import path
from .auth_views import get_csrf_token, user_login, user_logout
from .registration_view import register_user
from .views import random_string

urlpatterns = [ path('register/', register_user, name='register_user'),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('random-string/', random_string, name='random_string')]