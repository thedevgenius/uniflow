from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class SignInView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True

class SignOutView(LogoutView):
    template_name = 'account/logout.html'