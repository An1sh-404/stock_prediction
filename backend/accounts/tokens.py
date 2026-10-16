from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import Token
import jwt



User = get_user_model()

class EmailVerificationToken:
    """
     JWT token for email verification
     """

    @staticmethod
    def create_token(user):
        """
        Create a JWT token for email verification
        """
        expiration = timedelta(hours=24)
        now = timezone.now()
        payload  = {
            'user_id': user.pk,
            'exp': int((now + expiration).timestamp()),
            'iat': int(now.timestamp()),
            'type': 'email_verification'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return token

    @staticmethod
    def verify_token(token):
        """
        Verify the JWT token for email verification
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            if payload.get('type') != 'email_verification':
                return None
            user_id = payload.get('user_id')
            user = User.objects.get(id=user_id)
            return user
        
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
            return None