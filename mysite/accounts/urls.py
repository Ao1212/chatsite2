from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit/", views.ProfileEditView.as_view(), name="prof_edit"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
