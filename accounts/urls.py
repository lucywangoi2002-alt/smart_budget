from django.urls import path
from .views import signup
from django.views.generic.base import TemplateView
from .forms import LoginForm 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm), name="login"),
    path("", TemplateView.as_view(template_name="mybudget/dashboard.html"), name="dashboard"),
    path('login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=LoginForm  # <-- use your custom form
        ),
        name='login'),

]