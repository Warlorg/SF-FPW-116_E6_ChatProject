from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # login-section
    path("login/", auth_views.LoginView.as_view
         (template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="chat_app/index.html"), name="logout"),
]
