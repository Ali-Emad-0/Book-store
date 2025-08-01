from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from intake import recommend
from mypyc.doc.conf import author

from Ai.recommender.content_based_filtering import *
from .models import Book
from django.db.models import Q

from .forms import SignUpForm, EditProfileForm, ChangePasswordForm

# -------------------------------
# Public Views
# -------------------------------

def home(request):
    new_books = Book.objects.filter(is_new=True)
    popular_books = Book.objects.filter(is_popular=True)

    return render(request, 'Home Page.html',{
        'new_books':new_books, 'popular_books':popular_books
    })

def details(request, slug):
    book = get_object_or_404(Book,  slug=slug)
    similar_isbns = recommend_similar_books(book.isbn)
    similar_books = Book.objects.filter(isbn__in = similar_isbns)
    return render(request, 'Details Page.html', {'book': book, 'similar_books':similar_books})

def searched(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Book.objects.filter(
            Q(title__icontains=query)|Q(description__icontains=query)|Q(author__icontains=query)
        ).distinct()
    return render(request, 'Searched Page.html', {'query' : query, 'results' : results})

def sign_up(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('sign-in')
    else:
        form = SignUpForm()

    return render(request, 'Sign Up Page.html', {'sign_up_form': form})


def sign_in(request):
    """Handles user login by email and password."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'Sign In Page.html')


# -------------------------------
# Authenticated Views
# -------------------------------

@login_required
def logout_user(request):
    """Logs out the current user."""
    logout(request)
    return redirect('home')


@login_required
def user_profile(request):
    """Renders the user's profile page."""
    return render(request, 'Profile-page.html')


@login_required
def edit_profile(request):
    """Handles profile editing."""
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'edit_profile_form': form})


@login_required
def change_password(request):
    """Allows user to change password."""
    if request.method == 'POST':
        change_password_form = ChangePasswordForm(user=request.user, data=request.POST)
        if change_password_form.is_valid():
            user = change_password_form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, 'Password changed successfully!')
    else:
        change_password_form = ChangePasswordForm(user=request.user)

    return render(request, 'change_password.html', {'change_password_form': change_password_form})
