from django.shortcuts import render
from django.contrib.auth import get_user_model,logout

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerializer
from .tokens import EmailVerificationToken
from .utils import send_verification_email
from .throttles import LoginThrottle, ResendThrottle, VerifyThrottle, RegistrationThrottle     

# Create your views here.

User = get_user_model()




class UserRegistrationView(generics.CreateAPIView):

    serializer_class = UserRegistrationSerializer 
    permission_classes = [AllowAny]
    throttle_classes = [RegistrationThrottle]

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
    throttle_classes = [VerifyThrottle]

    def get(self, request):
        token = request.GET.get('token')
        user = EmailVerificationToken.verify_token(token)

        if user is not None:
            user.email_verified = True
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {"message": "Email verified successfully.",
                             "user": UserSerializer(user).data,
                             "tokens":{
                                 "refresh": str(refresh),
                                 "access": str(refresh.access_token)
                                 }
                }, status=200)
        
        else:
            return Response({"error": "Invalid or expired token."}, status=400)


class ResendVerificationEmailView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    throttle_classes = [ResendThrottle]

    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email=email)

        if user and not user.email_verified:

            # Generate a new email verification token
            token = EmailVerificationToken.create_token(user)

            # Send verification email
            send_verification_email(user.email, token)

        return Response({"message": "Verification email resent successfully."}, status=200)
    



class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed

    def get_object(self):
        return self.request.user


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer  # You can create a separate serializer for login if needed
    permission_classes = [AllowAny]
    throttle_classes  = [LoginThrottle]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = RefreshToken.for_user(serializer.validated_data['user'])
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Implement token backlisting logic for JWT AUTH later when using JWT Authentication
        refresh = request.data.get('refresh')
        try:
            token = RefreshToken(refresh)
            token.blacklist()  # Blacklist the refresh token
            logout(request)  # Log out the user from the session
            return Response({"message": "Logged out successfully."}, status=200)
        except Exception as e:
            return Response({"error": "Invalid token or token already blacklisted."}, status=400)
