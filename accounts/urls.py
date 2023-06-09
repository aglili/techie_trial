from django.urls import path
from . import views


urlpatterns = [
    path("signup/",views.signUpView,name="sign_up"),
    path("login/",views.loginView,name="login")
]