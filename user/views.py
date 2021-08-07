from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView

from .models import User
from .forms import UserSignUpForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        user = form.save()
        # user, created = User.objects.get_or_create(user=user)
        login(self.request, user)
        return redirect('/')


class UserLoginView(LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_superuser:
            return '/admin/'
        return '/'


class UserHomeView(LoginRequiredMixin, TemplateView):
    template_name = "user/home.html"
    login_url = 'login/'
