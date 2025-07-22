from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book

# Create your views here.
from .forms import SignUpForm


def home(request):
    new_books = Book.objects.filter(is_new=True)
    popular_books = Book.objects.filter(is_popular=True)

    return render(request, 'Home Page.html',{
        'new_books':new_books, 'popular_books':popular_books
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('sign-in') 
    else:
        form = SignUpForm()
        
    return render(request, 'Sign Up Page.html', {'form': form})


def signin(request):
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