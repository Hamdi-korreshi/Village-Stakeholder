"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.registration_view import register_user
from api.auth_views import get_csrf_token, user_login, user_signout
from api.views import random_string

urlpatterns = [
    path('admin/', admin.site.urls),
    path('village/v1/register/', register_user, name='register_user'),
    path('village/v1/csrf/', get_csrf_token, name='get_csrf_token'),
    path('village/v1/login/', user_login, name='login'),
    path('village/v1/logout/', user_signout, name='user_signout'),
    path('village/v1/random-string/', random_string, name='random_string')
]
