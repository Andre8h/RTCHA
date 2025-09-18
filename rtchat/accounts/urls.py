from django.urls import path
from .views import login, signup, profile

urlpatterns = [
    path("login/", login.as_view(), name="login"),
    path("signup/", signup.as_view(), name="signup"),
    path("profile/", profile.as_view(), name="profile"),
    path("profile/<int:id>", profile.as_view(), name="profile"),
]