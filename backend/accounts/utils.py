from django.core.mail import send_mail
from django.conf import settings
import os

def send_verification_email(user, token):
    """
    Send a verification email to the user with the provided token.
    """
    subject = 'Verify your email address'
    verification_link = f"{settings.FRONTEND_URL}/api/auth/verify-email/?token={token}/"
    message = f"Hi {user.username},\n\nPlease verify your email address by clicking the link below:\n{verification_link}\n\nIf you did not sign up for this account, please ignore this email.\n\nThank you!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)