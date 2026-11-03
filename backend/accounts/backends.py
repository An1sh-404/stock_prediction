
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

User = get_user_model()



class EmailVerificationRequired(Exception):
	def __init__(self,user):
		self.user = user

class AccountDisabled(Exception):
    def __init__(self,user):
        self.user = user


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None,strict=False, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)

        if not username or password is None:
            return None

        identifier = username.strip().lower()

        try:
            user = User._default_manager.get(
                Q(username=identifier) | Q(email=identifier)
            )

        except User.DoesNotExist:
            User().set_password(password) # prevent timing attacks/burn comparable CPU time
            return None
        
        if not user.check_password(password):
             return None


        if not user.email_verified:
            if strict:
                 raise EmailVerificationRequired(user)
            return None

        if not user.is_active:
            if strict:
                   raise AccountDisabled(user)
            return None
                        
        
        return user


    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)        
            return user if self.user_can_authenticate(user) else None
        except User.DoesNotExist:
            return None



