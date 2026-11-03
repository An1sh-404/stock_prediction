from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

from .tokens import EmailVerificationToken

def send_verification_email(user):
    """
    Send a verification email to the user with the provided token.
    """
    token = EmailVerificationToken.create_token(user)

    subject = 'Verify your email address'    
    verification_path = reverse("verify-email")
    verification_link = (
        f"{settings.BACKEND_URL.rstrip('/')}"
        f"{verification_path}?token={token}"
    )

    message = (
        f"Hi {user.username},\n\n"
        "Please verify your email address by clicking the link below:\n"
        f"{verification_link}\n\n"
        "If you did not sign up for this account, please ignore this email.\n\n"
        "Thank you!"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    print(f"Verification link:{verification_link}")

    send_mail(subject, message, from_email, recipient_list)


