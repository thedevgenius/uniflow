from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from .forms import LoginForm, SignUpForm


class SignInView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm

class SignOutView(LogoutView):
    template_name = 'account/logout.html'

class SignUpView(TemplateView):
    template_name = 'account/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # return redirect('login')
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})