from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =  [
    path('/login', obtain_auth_token),
    path('/register', views.RegisterView.as_view()),
    path('/logout', views.LogoutView.as_view()),
    
]
