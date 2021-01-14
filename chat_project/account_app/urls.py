from django.contrib import admin
from django.urls import path,include
from .views import user_login
from django.contrib.auth import views as auth_views

app_name="account_app"
urlpatterns = [
   
    path("login/",user_login,name = "login" ),
    path("logout/", auth_views.LogoutView.as_view(), name= 'logout' )
]