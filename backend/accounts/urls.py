from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('verify-email/', views.VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification-email/', views.ResendVerificationEmailView.as_view(), name='resend-verification-email'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('google/', views.GoogleLoginView.as_view(), name='google-login'),
]