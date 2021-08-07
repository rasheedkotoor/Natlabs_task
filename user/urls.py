from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserRegisterView, UserLoginView, UserHomeView

app_name = 'user'

urlpatterns = [
    path('', UserHomeView.as_view(), name='user_home'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]