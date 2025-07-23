from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<slug:slug>', views.details, name='book_details'),
    path('sign-in/', views.signin, name='sign-in'),
    path('sign-up/', views.signup, name='sign-up'),
]



