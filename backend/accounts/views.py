from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout
from .serializers import UserRegistrationSerializer, UserSerializer
from .tokens import EmailVerificationToken
from .utils import send_verification_email


# Create your views here.

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):

    serializer_class = UserRegistrationSerializer 
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate email verification token
        token = EmailVerificationToken.create_token(user)

        # Send verification email
        send_verification_email(user.email, token)

        return Response({"message": "User registered successfully. Please check your email to verify your account."}, status=201)


class VerifyEmailView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token')
        user = EmailVerificationToken.verify_token(token)

        if user is not None:
            user.email_verified = True
            user.is_active = True
            user.save()
            return Response({"message": "Email verified successfully."}, status=200)
        else:
            return Response({"error": "Invalid or expired token."}, status=400)


class ResendVerificationEmailView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            if user.email_verified:
                return Response({"message": "Email is already verified."}, status=400)

            # Generate a new email verification token
            token = EmailVerificationToken.create_token(user)

            # Send verification email
            send_verification_email(user.email, token)

            return Response({"message": "Verification email resent successfully."}, status=200)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=404)



class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed

    def get_object(self):
        return self.request.user


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Implement token backlisting logic for JWT AUTH later when using JWT Authentication
        logout(request)
        return Response({"message": "Logged out successfully."}, status=200)