from django.urls import re_path
from . import views
from .views import UserRegistrationView

urlpatterns = [
    re_path('login/', views.login_view, name='login'),
    re_path(r'register/', UserRegistrationView.as_view(), name='register'),
]
