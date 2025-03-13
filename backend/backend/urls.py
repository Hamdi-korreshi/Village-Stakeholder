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
from .registration_views import register_user
from .auth_views import get_csrf_token, signin, signout
from .views import random_string

urlpatterns = [
    path('admin/', admin.site.urls),
    path('village/v1/csrf/', get_csrf_token, name='get_csrf_token'),
    path('village/v1/login', signin, name='signin'),
    path('village/v1/logout', signout, name='signout'),
    path('village/v1/random-string/', random_string, name='random_string')
]
