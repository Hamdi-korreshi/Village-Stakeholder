from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

user_model = get_user_model()

# new auth for allowing login by email or username
class email_or_username_backend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)
        
        try:
            user = user_model.objects.get(Q(username=username) | Q(email=username))
        except user_model.DoesNotExist:
            user_model().set_password(password)
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user