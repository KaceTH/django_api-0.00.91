from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('users/', views.signUp),
    path('users/<str:username>/', views.user_setting),
    path('users/<str:username>/change/', views.change),
    path('email_pass/<str:username>/', views.email_verification),
    path('find_pw/', views.find_pw)
]