from django.contrib.auth import get_user_model,logout

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed,ValidationError, PermissionDenied
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerializer, GoogleAuthenticationSerializer, LogoutSerializer
from .tokens import EmailVerificationToken
from .utils import send_verification_email
from .throttles import LoginThrottle, ResendThrottle, VerifyThrottle, RegistrationThrottle     
from .services import get_or_create_google_account

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

        return Response({"message": f"{user.username} registered successfully. Please check your email to verify your account."}, status=201)


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
            send_verification_email(user)

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



class GoogleLoginView(generics.GenericAPIView):
    serializer_class = GoogleAuthenticationSerializer
    permission_classes = [AllowAny]
    throttle_classes = [LoginThrottle]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        google_identity = serializer.validated_data['google_identity']

        try:
            user, created = get_or_create_google_account(
                email = google_identity['email'],
                google_sub = google_identity['google_sub'],
                display_name = google_identity['display_name'],
            )

        except ValueError as e:
            raise ValidationError({"credential": str(e)})

        if not user.is_active:
            raise AuthenticationFailed(
                "This account has beend disabled. Contact support.",
                code="account_disabled",
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": (
                    "Google account created successfully." if created else "Google login successful."
                ),
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_value = serializer.validated_data['refresh']

        try:
            refresh_token = RefreshToken(refresh_value)

        except TokenError:
            raise ValidationError(
                {
                    "refresh": "Invalid or expired refresh token."
                }
            )

        token_user_id = refresh_token.get('user_id')

        if token_user_id is None:
            raise ValidationError({
                "refresh": "Refresh token does not contain user information."
            })

        if str(token_user_id) != str(request.user.pk):
            raise PermissionDenied(
                "You do not have permission to log out this user."
            )

        try:
            refresh_token.blacklist()

        except TokenError:
            raise ValidationError(
                {
                    "refresh": "Refresh token is already blacklisted."
                }
            )

        logout(request)
        return Response(
            {"message": "Logged out successfully."},
            status=200,
        )


    

