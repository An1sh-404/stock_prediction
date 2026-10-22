from django.db import transaction
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import serializers
from rest_framework.exceptions import APIException, AuthenticationFailed

from .backends import EmailOrUsernameModelBackend, EmailVerificationRequired, AccountDisabled   


User = get_user_model()

class EmailNotVerifiedException(APIException):
    status_code = 403
    default_code = 'email_not_verified'

    def __init__(self, email):
        super().__init__(
            detail={
                "detail": "Email not verified. Please verify your email address to proceed.",
                "email": email,
                "resend_url": reverse("resend-verification-email"),
            },
            code = self.default_code,
        )



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username','date_joined', 'email_verified']
        read_only_fields = ['date_joined', 'email_verified']





class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2',]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2') 
        with transaction.atomic():
            user = User.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password']
            )
            transaction.on_commit(lambda: self.send_verification_email(user))

        return user


    class UserLoginSerializer(serializers.Serializer):
        username = serializers.CharField(required=True)
        password = serializers.CharField(write_only=True, required=True)

        def validate(self, attrs):
            username = attrs['username'].lower()
            try:
                user = authenticate(
                    self.context.get('request'),
                    username=username,
                    password=attrs['password'],
                    strict=True,
                )
            except EmailVerificationRequired as exc:
                raise EmailNotVerifiedException(exc.user.email)
            except AccountDisabled:
                raise AuthenticationFailed(
                        "This account has been disabled. Contact support.",
                        code="account_disabled",
                )
            if user is None:
                raise AuthenticationFailed(
                    "Invalid credentials. Please try again.",
                    code="invalid_credentials",
                )
            attrs["user"] = user
            return attrs





