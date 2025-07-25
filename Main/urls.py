from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<slug:slug>', views.details, name='book_details'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('logout/',views.logout_user, name='logout'),
    path('profile/',views.user_profile, name='profile'),
    path('change-password/',views.change_password, name='change-password'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('searched/', views.searched, name='searched'),
]



