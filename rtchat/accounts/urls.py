from django.urls import path
from .views import login, signup, profile, auth

urlpatterns = [
    path("login/", login.as_view(), name="login"),
    path("auth/",auth.as_view(),name="auth"),
    path("signup/", signup.as_view(), name="signup"),
    path("profile/<int:id>", profile.as_view(), name="profile"),
]