
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Account created successfully!')

            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "registration/login.html")