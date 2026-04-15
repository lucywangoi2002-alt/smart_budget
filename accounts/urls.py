from django.urls import path
from .views import signup, verify_email
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    path("signup/", signup, name="signup"),

    path('login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=LoginForm
        ),
        name='login'
    ),

    path('logout/',
        auth_views.LogoutView.as_view(
            next_page='login'  
        ),
        name='logout'
    ),

    path('verify/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]