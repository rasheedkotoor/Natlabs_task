from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from .views import AdminHomeView, AdminLoginView

app_name = 'admin'

urlpatterns = [
    path('', AdminHomeView.as_view(), name='admin_home'),
    path('login/', AdminLoginView.as_view(), name='admin_login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]