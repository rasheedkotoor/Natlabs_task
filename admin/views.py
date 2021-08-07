from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView
from user.models import User


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class AdminHomeView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    template_name = "admin/admin_home.html"
    login_url = 'login/'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminHomeView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class AdminLoginView(LoginView):
    template_name = "admin/admin_login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_superuser:
            return '/admin/'
        return '/'

