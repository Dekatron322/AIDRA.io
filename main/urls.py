from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("profile/", views.ProfileView, name="profile"),
	path("about/", views.AboutView, name="about"),
	path("vacancy/", views.VacancyView, name="vacancy"),
	path("edit_profile/", views.EditProfileView, name="edit_profile"),

	path("signup/", views.SignUpView, name="signup"),
	path("login/", views.LoginView, name="login"),
	path("forgot_password/", views.ForgotPasswordView, name="forgot_password"),
	
]